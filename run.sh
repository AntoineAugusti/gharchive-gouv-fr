#!/bin/sh
set -e

MONTH=$1

cd data
rm -f $MONTH.json

for i in $(seq -f "%02g" 1 28)
do
  wget -nc https://data.gharchive.org/$MONTH-$i-{0..23}.json.gz
  gunzip -f $MONTH-$i-*.json.gz
  cat $MONTH-$i-*.json | jq -c 'select( .type == "PushEvent" ) | select(.payload.commits[0].author.email // "" | endswith(".gouv.fr"))' >> $MONTH.json
  rm -f $MONTH-$i-*.json
done

wget -nc https://data.gharchive.org/$MONTH-{29..31}-{0..23}.json.gz || true
gunzip -f $MONTH-*.json.gz
cat $MONTH-*.json | jq -c 'select( .type == "PushEvent" ) | select(.payload.commits[0].author.email // "" | endswith(".gouv.fr"))' >> $MONTH.json
rm -f $MONTH-*
