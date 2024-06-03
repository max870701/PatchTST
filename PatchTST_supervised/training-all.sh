#!/bin/bash

SCRIPT_PATH="./scripts/PatchTST"
START_LEVEL=5
END_LEVEL=10

echo "Training benchmark model..."
sh "$SCRIPT_PATH/stock-norm.sh"

# Correct the variable names in the seq command
for i in $(seq $START_LEVEL $END_LEVEL); do
	echo "Training symlet wavelet model level $i"
	sh "$SCRIPT_PATH/stock-wavelet-lv$i.sh"
done

for i in $(seq $START_LEVEL $END_LEVEL); do
	echo "Training db wavelet model level $i"
	sh "$SCRIPT_PATH/stock-db-wavelet-lv$i.sh"
done

for i in $(seq $START_LEVEL $END_LEVEL); do
	echo "Training haar wavelet model level $i"
	sh "$SCRIPT_PATH/stock-haar-wavelet-lv$i.sh"
done
