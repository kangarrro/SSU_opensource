#!/bin/bash


name="$1"

if [ ! -d "$name" ]; then
    mkdir "$name"
fi

cd "$name"
for i in {1..5}; do
    touch "file$i.txt"
done

tar -czvf "$name.tar.gz" ./*

mkdir "$name"
tar -xzvf "$name.tar.gz" -C "$name"
