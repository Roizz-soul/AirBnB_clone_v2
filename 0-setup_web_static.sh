#!/usr/bin/env bash
# A script to set up my web servers for the deployment of web_static

apt-get update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo 'Holberton School' > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data/
chgrp -R ubuntu /data/
echo '# server config
server {
    listen 80;

    location /hbnb_static {
        root /data/web_static/current/;
        alias /data/web_static/current/hbnb_static;
    }
}' | sudo tee -a /etc/nginx/sites-available/default > /dev/null
nginx -s reload
