#!/bin/bash

echo "===== SYSTEM STATUS ====="

echo "Nginx Status:"
systemctl is-active nginx

echo ""
echo "Open Ports:"
ss -tuln | grep :80

echo ""
echo "Last 5 Access Logs:"
tail -n 5 /var/log/nginx/access.log

echo ""
echo "Memory Usage:"
free -h
