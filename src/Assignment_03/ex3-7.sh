#!/bin/bash

name="$1"

mkdir "$name"

cd "$name" || exit 1

for i in {0..4}; do
    touch "file$i.txt" 

    folder="$name$i"
    mkdir "$folder"

    ln -s "../file$i.txt" "$folder/file$i.txt"
done
