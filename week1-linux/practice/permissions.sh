#!/bin/bash

echo "Creating secure file..."
touch prod_file.txt

echo "Setting restricted permissions..."
chmod 600 prod_file.txt

echo "Done"
ls -l prod_file.txt
