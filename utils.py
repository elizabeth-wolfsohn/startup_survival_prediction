import pyarrow.parquet as pq
import pyarrow as pa
import pyarrow.compute as pc
import os
import numpy as np

def count_nb_lines(dataset):
    return sum(dataset.metadata.row_group(i).num_rows for i in range(dataset.num_row_groups))
    



#affiche le noms des colonnes
def show_columns(dataset):
    if dataset is not None:
        print(f"Columns : {dataset.schema.names}")
    

def count_target_value(target_value, column_name, dataset, proportion=False):
    count=0
    for i in range(dataset.num_row_groups):
        
        group=dataset.read_row_group(i,columns=[column_name])
        list_values=group.to_pylist()
        for line in list_values:
            if(line[column_name]==target_value):
                count+=1
    if(proportion==True):
        total_lines=count_nb_lines(dataset)
        if(total_lines!=0):
            target_proportion=count/total_lines
            return count, target_proportion
        else:
            return count,None
    
    return count


def count_target_list(list_target_values, column_name, dataset, proportion=False):
    count = 0
    total_rows = 0

    for i in range(dataset.num_row_groups):
        group = dataset.read_row_group(i, columns=[column_name])
        total_rows += group.num_rows
        mask = pc.is_in(group[column_name], pa.array(list_target_values))
        count += pc.sum(mask).as_py()

    if proportion:
        target_proportion=count/total_rows if total_rows > 0 else None
        return count, target_proportion

    return count
    



def compute_null_values(columns, dataset, proportion=False):
    total_rows = count_nb_lines(dataset)
  
    list_count_null_values=[]
    for j in range(len(columns)):
        total_null_vals=0

        for i in range(dataset.num_row_groups): 
            dataset_group=dataset.read_row_group(i, columns=[columns[j]]) 
            filter=pc.is_null(dataset_group[columns[j]]) 
            total_null_vals+= pc.sum(filter).as_py() 
        list_count_null_values.append(total_null_vals)
    if(proportion==True):
        null_val_proportions=[list_count_null_values[i]/total_rows for i in range(len(list_count_null_values))]
        return  list_count_null_values,null_val_proportions

    return list_count_null_values


def compute_null_proportions(columns, dataset):
    print("Proportion de valeurs nulles pour :")
    total_rows = 0 
    for i in range(dataset.num_row_groups): 
        total_rows += dataset.metadata.row_group(i).num_rows 

    null_val_proportions=[]
    for j in range(len(columns)):
        total_null_vals=0

        for i in range(dataset.num_row_groups): 
            dataset_group=dataset.read_row_group(i, columns=[columns[j]]) 
            filter=pc.is_null(dataset_group[columns[j]]) 
            total_null_vals+= pc.sum(filter).as_py() 
        proportion=total_null_vals/total_rows
        print(f"     {columns[j]} : {proportion}")
        null_val_proportions.append(proportion)
    return null_val_proportions


def extract_division_names(dataset, column_name):
    list_divisions = set()  

    for i in range(dataset.num_row_groups):
        dataset_g = dataset.read_row_group(i, columns=[column_name])
        group_divisions = pc.unique(dataset_g[column_name])
        # Ajout uniquement des uniques du row group
        list_divisions.update(group_divisions.to_pylist())

    return list_divisions 


def column_filter(dataset,out_file_name,columns):
    out_file = None
    for i in range(dataset.num_row_groups):

     
        dataset_g = dataset.read_row_group(i,columns=columns)

        if out_file is None:
            out_file = pq.ParquetWriter(out_file_name,dataset_g.schema)
        out_file.write_table(dataset_g)

    if out_file is not None:
        out_file.close()

def year_simplified(dataset, out_file_name, column_name, new_column_name, columns=None):
    out_file = None

    for i in range(dataset.num_row_groups):
        if columns is None:
            dataset_g = dataset.read_row_group(i)
        else:
            dataset_g = dataset.read_row_group(i, columns=columns)

        dates = dataset_g[column_name]
        annees = pc.year(dates)
        dataset_g = dataset_g.append_column(new_column_name, annees)

        if out_file is None:
            out_file = pq.ParquetWriter(out_file_name, dataset_g.schema)

        out_file.write_table(dataset_g)

    if out_file is not None:
        out_file.close()

def siren_filter(dataset, column_name, out_file_name, list_siren):
    set_siren = set(list_siren)
    sirens_array = pa.array(list(set_siren))  
    out_file = None

    for i in range(dataset.num_row_groups):
        dataset_g = dataset.read_row_group(i)
        
       
        valid_mask = pc.is_in(dataset_g[column_name], sirens_array)
        dataset_g_filtered = dataset_g.filter(valid_mask)

        if len(dataset_g_filtered) == 0:
            continue
            
        if out_file is None:
            out_file = pq.ParquetWriter(out_file_name, dataset_g_filtered.schema)

        out_file.write_table(dataset_g_filtered)

    if out_file is not None:
        out_file.close()



def var_filter(dataset, column_name, out_file_name, list_var):
    sirens_array = pa.array(list(set(list_var)))  # unique values
    out_file = None

    for i in range(dataset.num_row_groups):
        dataset_g = dataset.read_row_group(i)

        valid_mask = pc.is_in(dataset_g[column_name], sirens_array)
        dataset_g_filtered = dataset_g.filter(valid_mask)

        if dataset_g_filtered.num_rows == 0:
            continue

        if out_file is None:
            out_file = pq.ParquetWriter(out_file_name, dataset_g_filtered.schema)

        out_file.write_table(dataset_g_filtered)

    if out_file is not None:
        out_file.close()


def compute_stats(dataset, column_name):
    total = 0
    count = 0
    sum_squares = 0
    values = []

    for i in range(dataset.num_row_groups):
        group = dataset.read_row_group(i, columns=[column_name])
        
        # filtrer les valeurs nulles
        mask = pc.is_valid(group[column_name])
        group_valid = group.filter(mask)
        
        if len(group_valid) == 0:
            continue

        # convertir ChunkedArray en numpy array
        arr = group_valid[column_name].to_numpy(zero_copy_only=False)
        
        total += arr.sum()
        count += len(arr)
        sum_squares += (arr ** 2).sum()
        values.append(arr)

    if count == 0:
        return None

    moyenne = total / count
    variance = (sum_squares / count) - moyenne ** 2
    ecart_type = np.sqrt(variance)

    all_values = np.concatenate(values)
    minimum = all_values.min()
    maximum = all_values.max()
    q1 = np.percentile(all_values, 25)
    mediane = np.median(all_values)
    q3 = np.percentile(all_values, 75)

    return {
        "count": count,
        "moyenne": moyenne,
        "ecart_type": ecart_type,
        "min": minimum,
        "q1": q1,
        "mediane": mediane,
        "q3": q3,
        "max": maximum
    }





def filter_null_rows(dataset,out_file_name, column_a_filtrer,columns_retenues=None):

    out_file = None

    for i in range(dataset.num_row_groups):

 
        if columns_retenues is None:
            group = dataset.read_row_group(i)
        else:
            group = dataset.read_row_group(i, columns=columns_retenues)

        mask = pc.invert(pc.is_null(group[column_a_filtrer]))
        group_new = group.filter(mask)

        # si le row group est vide, on passe
        if group_new.num_rows == 0:
            continue

        # initialisation du writer
        if out_file is None:
            out_file = pq.ParquetWriter(
                out_file_name,
                group_new.schema
            )

        out_file.write_table(group_new)

    if out_file is not None:
        out_file.close()
