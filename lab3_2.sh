#!/bin/bash
set -e

# Store command line parameters in variables
input_file=$1
output_file=$2

# Remove blank lines and save to output file
grep -v '^[[:space:]]*$' "$input_file" > "$output_file"

echo "Have a great day!"