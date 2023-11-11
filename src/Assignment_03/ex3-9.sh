#!/bin/bash

name="$1"

line=$(grep -n "$name" "DB.txt")

echo $line