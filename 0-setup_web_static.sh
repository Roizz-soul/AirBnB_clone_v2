#!/usr/bin/env bash
# A script to set up my web servers for the deployment of web_static

sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo echo -e "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
update="\\\n\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}"
sudo sed -i "55i $update" /etc/nginx/sites-available/default
sudo service nginx restart
