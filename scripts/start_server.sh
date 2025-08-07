#!/bin/bash

echo "Starting Python web server..."

cd /home/ec2-user/webapp
nohup python3 app.py > server.log 2>&1 &
