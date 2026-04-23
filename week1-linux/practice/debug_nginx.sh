#!/bin/bash

echo "Checking nginx status..."
systemctl status nginx | head -n 10

echo "Recent nginx errors:"
tail -n 5 /var/log/nginx/error.log
