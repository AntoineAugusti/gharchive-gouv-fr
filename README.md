[![goodtables.io](https://goodtables.io/badge/github/AntoineAugusti/gharchive-gouv-fr.svg)](https://goodtables.io/github/AntoineAugusti/gharchive-gouv-fr)

# GH Archive Gouv FR
Download data from [GH Archive](https://www.gharchive.org) and extract push events done with `@*.gouv.fr` email addresses.

## Requirements
This works with a single Bash script. Dependencies are :
- `gunzip`
- `jq`
- `wget`

This should be straightforward to run on a UNIX machine.

## Usage
You can download the GitHub archive for a given month, extract log files and process them with the following command:

```sh
./run.sh 2017-01
```

Be aware that this will take a good amount of bandwidth, storage and processing power. For example, the compressed log files for 2018-01 weight 95 GB.

## Schema details

- Auteur : Antoine Augusti <antoine.augusti@data.gouv.fr>
- Schéma créé le : 2019-04-02
- Clé primaire : `id`

### Modèle de données

|Nom|Type|Description|Exemple|Propriétés|
|-|-|-|-|-|
|id|nombre entier|Identifiant unique de l'événement|2489811994||
|repository_name|chaîne de caractères|Le nom du répertoire GitHub|openchordcharts/openchordcharts-sample-data||
|ref|chaîne de caractères|La branche concernée|refs/heads/master||
|author_email|chaîne de caractères|L'adresse e-mail de l'auteur du commit|b445c0e632270b31bc0c900a39de4fc4159fb695@data.gouv.fr|Motif : `.*@.*\.gouv\.fr$`|
|author_domain|chaîne de caractères|Le nom de domaine de l'adresse e-mail de l'auteur du commit|data.gouv.fr|Motif : `.*\.gouv\.fr$`|
|author_name|chaîne de caractères|Le nom de l'auteur du commit|Jean Dupont||
|message|chaîne de caractères|Le message de commit|WIP||
|sha|chaîne de caractères|Le SHA1 du commit|288e534ef881c3973bc413a60370dfa59caf7fbe||
|organisation_name|chaîne de caractères|Le nom de l'organisation|betagouv||
|created_at|date et heure|La date de création du commit, en ISO8601|2015-01-01T20:40:32Z||

## License
MIT. See the license file.
