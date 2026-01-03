# Projet SDA



## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://git.unistra.fr/wolfsohn/projet-sda.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://git.unistra.fr/wolfsohn/projet-sda/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Set auto-merge](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing (SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thanks to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README

Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.


## Dataset bruts

stockunitelegale : 
nombre lignes : 29 045 566
Proportion de survivants : 0.5829311778603316



## Préparation des données

### StockUniteLegale : 

- Suppression de toutes les colonnes non explicatives telles que 'prenom1UniteLegale', 'denominationUsuelle1UniteLegale'
- Suppression de toutes les colonnes ayant un pourcentage de valeurs null à 100% (ex: caractereEmployeuUniteLegale)
- Sélection des catégories juridiques et des activités principales typiques d'une startup 
    Catégories juridiques retenues : 
        5710 — SAS (Société par actions simplifiée)

   Activités principales retenues : 
        Numérique / Logiciel
        "58.21Z",  # Édition de jeux électroniques
        "58.29A",  # Édition de logiciels système et réseau
        "58.29B",  # Édition de logiciels outils de développement et de langages
        "62.01Z",  # Programmation informatique
        "62.02A",  # Conseil en systèmes et logiciels informatiques
        "62.02B",  # Tierce maintenance de systèmes et d’applications informatiques
        "62.09Z",  # Autres activités informatiques

        Données / plateformes / cloud
        "63.11Z",  # Traitement de données, hébergement et activités connexes
        "63.12Z",  # Portails Internet
        "63.99Z",  # Autres services d’information n.c.a.

        R&D / Deeptech
        "72.11Z",  # R&D en biotechnologie
        "72.19Z",  # R&D en autres sciences physiques et naturelles

        Industrie technologique / hardware
        "26.11Z",  # Fabrication de composants électroniques
        "26.20Z",  # Fabrication d’ordinateurs et d’équipements périphériques
        "26.51A",  # Fabrication d'équipements d'aide à la navigation
        "26.51B"   # Fabrication	d'instrumentation	scientifique	et	technique

        Conseil technologique à forte intensité innovation
        "70.22Z",  # Conseil pour les affaires et autres conseils de gestion (tech / SaaS)



- Encodage des variables catégorielles avec substitution des valeurs manquantes au passage


### StockUniteEtablissement

- Filtrage des sirens de sorte à ce que StockUniteEtablissement ne contienne que les siren de StockUniteLegale
- Comptage du nombre d'établissements pour chaque entreprise
- Calcul de la proportion d'établissements ouverts pour chaque entreprise

### Ratios INPI BCE

- Au départ, un dataset contenant les détails des données financières des entreprises a été utilisé pour la préparation des données.
Mais du fait du nombre de variables financières et de la proportion d'entre elles qui contiennent des variables manquantes, nous avons remplacé
ce dataset par un dataset de bilan financier sur le même site internet que l'ancien dataset et qui est beaucoup synthétique au niveau des données financières. En particulier, ces données ont été calculées par les auteurs à partir du dataset détaillé que nous avons exploité initialement. 

- Filtrage des sirens de sorte à ce que le dataset sur les bilans financiers ne contiennent que les sirens du dataset StockUniteLegale

- Nous avons découvert que seul 4% des 280 000 entreprises  (donc 36388 entreprises environ) a déclaré au moins un bilan financier dans le dataset. Ainsi, nous avons fait deux versions du dataset afin de ne pas biaiser les résultats si nous n'avions étudié que les entreprises ayant déclaré au moins un bilan 
(dans la base de données filtrée de StockUniteLegale, le taux de survie est 74% tandis que parmi ces entreprises qui ont déclaré au moins un bilan financier, ce taux arrive à 82%). 
La première version consiste à garder toutes les entreprises de la base de données filtrée de StockUniteLegale (ayant déclaré un bilan ou non) et à ne pas étudier le détail des bilans financier et à ajouter dans le dataset une variable qui indique si une certaine entreprise à déclaré au moins un bilan financier dans les 3 premières années de vie de l'entreprise (année de creéation incluse). 

La deuxième version consiste à n'étudier que les entreprises ayant déclaré au moins un bilan financier dans un certain intervalle d'années situé au début de la vie de l'entreprise. Afin d'avoir un taux de survie le plus similaire à celui des entreprises de la base de données filtrée de StockUniteLegale, nous choisi l'intervalle des 3 premières annnées de l'entreprise (dont l'année de création de celle-ci). Ainsi nous obtenons un taux de survie, avec ces critères de 76%. 
    - Dans cette version, nous avons retiré toutes les lignes qui concernent les bilans financiers postérieurs à cette intervalle
    - nous avons, pour chaque variable calculé sa moyenne des 3 valeurs, son tcam (taux de croissance annuel moyen) et son écart-type.
    - Pour les valeurs manquantes, nous avons décidé que, si une entreprise à 1 ou deux valeurs manquantes sur 3, alors nous recopions la même valeur combler les valeurs manquantes, ce qui permet de prendre en compte la valeur déclarée dans la moyenne et d'assurer un taux de croissance nul. 
    - Si les trois valeurs sont manquantes, alors les valeurs associées au tcam, moyenne et écart type seront manquantes et après le processus de calculs pour toutes les lignes, nous substituons ces valeurs manquantes par la médiane de chaque colonne. 


A l'issue de cela, selon les deux versions en termes de nombre de lignes et des variables, nous fusionnons 3 datasets finaux. 


## Sources : 

Nomenclature catégories juridiques : 
https://www.insee.fr/fr/information/2028129

Nomenclature activités principales : 
https://www.insee.fr/fr/information/2120875

Taux de croissance :
https://www.mathplace.fr/calcul-de-taux-de-croissance/
