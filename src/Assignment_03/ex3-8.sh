#!/bin/bash

read data

if [ -f "DB.txt" ]; then
    echo "$data" >> "DB.txt"
else
    echo "$data" > "DB.txt"
fi