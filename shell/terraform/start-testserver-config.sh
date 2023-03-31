#/bin/bash

echo -e "\e[1;34mStarting configuration...\e[0m"

echo -e "\e[1;34mUpdating packages...\e[0m"
sudo apt upgrade && sudo apt update


# Docker Installation
echo -e "\e[1;34mInstalling Docker...\e[0m"

sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable" -y

sudo apt update
sudo apt install docker-ce -y

echo -e "\e[1;32mDocker Installed!\e[0m"

# Docker Compose Installation
echo -e "\e[1;34mInstalling Docker Compose...\e[0m"

mkdir -p ~/.docker/cli-plugins/
curl -SL https://github.com/docker/compose/releases/download/v2.15.1/docker-compose-linux-x86_64 -o ~/.docker/cli-plugins/docker-compose
chmod +x ~/.docker/cli-plugins/docker-compose


echo -e "\e[1;32mDocker Compose Installed!\e[0m"

# Installing make
sudo apt install make -y


# Installing Nginx
echo -e "\e[1;34mInstalling Nginx...\e[0m"

sudo apt install curl gnupg2 ca-certificates lsb-release ubuntu-keyring -y

curl https://nginx.org/keys/nginx_signing.key | gpg --dearmor \
    | sudo tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/null

echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] \
http://nginx.org/packages/ubuntu `lsb_release -cs` nginx" \
    | sudo tee /etc/apt/sources.list.d/nginx.list

sudo apt update && sudo apt install nginx -y

echo -e "\e[1;32mNginx is successfully installed!\e[0m"
echo -e "\e[1;32mConfiguration is now finished!\e[0m"