#!/bin/bash
set -e

# Part 1 #
# Download the TAR bundle using curl
#curl -O https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz
curl -O $1

# Part 2 #
# Extract the downloaded TAR bundle
tar -xzf lab3-bundle.tar.gz

# Part 3 #
# Convert all TSV files to CSV
for file in *.tsv; do
    tr '\t' ',' < "$file" > "${file%.tsv}.csv"
done