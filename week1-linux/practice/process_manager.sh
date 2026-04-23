#!/bin/bash

echo "Starting process..."
sleep 300 &

PID=$!

echo "Process started with PID: $PID"

sleep 2

echo "Stopping process..."
kill $PID

echo "Process stopped"
