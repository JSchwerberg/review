#!/usr/bin/env bash

eval vagrantfile_location="~/.vagrantfile_processed"

if [ -f $vagrantfile_location ]; then
  echo "Vagrantfile already processed.  Exiting..."
  exit 0
fi

#==================================================================
# install dependencies
#==================================================================

/usr/bin/yes | pip install --upgrade pip
/usr/bin/yes | pip install --upgrade virtualenv

/usr/bin/yes | sudo apt-get install python-software-properties

#==================================================================
# set up the local dev environment
#==================================================================

if [ -f "/home/vagrant/.profile" ]; then
    echo -n "removing .profile for user vagrant..."
    rm /home/vagrant/.bash_profile
    echo "done!"
fi

echo -n "creating new .profile for user vagrant..."
ln -s /vagrant/.profile /home/vagrant/.profile
source /home/vagrant/.profile
echo "done!"

#==================================================================
# set up virtual env
#==================================================================
cd /vagrant;
echo -n "Creating virtualenv..."
virtualenv workenv;
echo "done!"

echo -n "Activating virtualenv..."
source /vagrant/workenv/bin/activate
echo "done!"

echo -n "installing project dependencies via pip..."
/usr/bin/yes | pip install -r /vagrant/requirements/dev.txt
echo "done!"

#==================================================================
# cleanup
#==================================================================

echo -n "marking vagrant as processed..."
touch $vagrantfile_location
echo "done!"
