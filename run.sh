#!/bin/sh
set -e

MONTH=$1

cd data && rm -f $MONTH-* && rm -f $MONTH.json && cd ..
python main.py $MONTH

cd data
gunzip -f $MONTH-*.json.gz
cat $MONTH-*.json | jq -c 'select( .type == "PushEvent" ) | select(.payload.commits[0].author.email // "" | endswith(".gouv.fr"))' > $MONTH.json
rm -f $MONTH-*
