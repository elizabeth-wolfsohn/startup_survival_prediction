import pyarrow.parquet as pq
import pyarrow as pa
import pyarrow.compute as pc



#Renvoie le nombre de lignes d'un dataset
def count_nb_lines(dataset):
    return sum(dataset.metadata.row_group(i).num_rows for i in range(dataset.num_row_groups))
    

#Compte le nombre de lignes contenant une certaine valeur (target_value) dans une colonne donnée (column_name) dans le dataset
#Possibilité de donner également la proportion d'apparition de cette valeur dans la colonne donnée du dataset
def count_target_value(target_value, column_name, dataset, proportion=False):
    count=0
    total_lines=count_nb_lines(dataset) 
    if(total_lines ==0):
        if(proportion==True):
            return 0,0
        else:
            return 0
    
    for i in range(dataset.num_row_groups): #lecture de tous les groupes du dataset
        group=dataset.read_row_group(i,columns=[column_name]) #lecture de la colonne qui nous intéresse
        list_values=group[column_name].to_pylist() 
        for value in list_values:
            if(value==target_value):
                count+=1

    if(proportion==True):
        target_proportion=count/total_lines
        return count, target_proportion
    
    return count


def compute_null_values(columns, dataset, proportion=False):
    total_lines = count_nb_lines(dataset)
    list_count_null_values=[]
    for j in range(len(columns)):
        total_null_values=0

        for i in range(dataset.num_row_groups): 
            dataset_group=dataset.read_row_group(i, columns=[columns[j]]) 
            filter=pc.is_null(dataset_group[columns[j]]) 
            total_null_values+= pc.sum(filter).as_py() 
        list_count_null_values.append(total_null_values)
    if(proportion==True):
        null_val_proportions=[list_count_null_values[i]/total_lines for i in range(len(list_count_null_values))]
        return  list_count_null_values,null_val_proportions

    return list_count_null_values



def extract_division_names(dataset, column_name):
    list_divisions = set()  

    for i in range(dataset.num_row_groups):
        dataset_g = dataset.read_row_group(i, columns=[column_name])
        group = pc.unique(dataset_g[column_name])
        # Ajout uniquement des uniques du row group
        list_divisions.update(group.to_pylist())

    return list_divisions 



def siren_filter(dataset, column_name, out_file_name, list_siren):

    sirens_array = pa.array(set(list_siren), type=pa.int64())
    
    writer = None

    for i in range(dataset.num_row_groups):
        group = dataset.read_row_group(i)
        
      
        if group.schema.field(column_name).type != pa.int64():
            group = group.set_column(
                group.schema.get_field_index(column_name),
                column_name,
                pc.cast(group[column_name], pa.int64())
            ) #on convertit la colonne en int64 si elle n'est pas de ce type
        
       
        filtre= pc.is_in(group[column_name], sirens_array)
        group_new = group.filter(filtre)

        if group_new .num_rows > 0:
            if writer is None:
                writer = pq.ParquetWriter(out_file_name, group_new .schema)
            writer.write_table(group_new )

    if writer is not None:
        writer.close()



def var_filter(dataset, column_name, out_file_name, list_var):
    array_values = pa.array(list(set(list_var)))  # unique values

    out_file = None

    for i in range(dataset.num_row_groups):
        group = dataset.read_row_group(i)

        filtre = pc.is_in(group[column_name], array_values)
        group_new=group.filter(filtre)

        if group_new.num_rows == 0:
            continue

        if out_file is None:
            out_file = pq.ParquetWriter(out_file_name, group_new.schema)

        out_file.write_table(group_new)

    if out_file is not None:
        out_file.close()

