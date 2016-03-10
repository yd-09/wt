sudo apt-get update && sudo apt-get install mc && sudo apt-get install tree

ls
cd wt
sudo ./msd.sh

cd /home/box/web

sudo django-admin startproject ask
cd ask
sudo python ./manage.py startapp qa
tree /home/box/web

