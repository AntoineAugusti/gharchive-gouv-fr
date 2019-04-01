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

## Licence
MIT. See the license file.
