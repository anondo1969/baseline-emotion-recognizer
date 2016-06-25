#!/bin/bash

#=====================================================================================
#this script install and build opensmile toolkit. if the
#download link does not work then please refer to
#http://audeering.com/research/opensmile/#download

# Written by Mahbub Ul Alam
#=====================================================================================

export LC_ALL=C


if [[ "$1" == "" ]]
then
		dir_name=default_installation_folder
else
		dir_name=$1
fi

if [[ ! -d "$1" ]]
then
        if [[ ! -L $dir_name ]]
        then
                echo "Directory doesn't exist. Creating now"
                mkdir $dir_name
                echo "Directory created"
        else
                echo "Directory exists"
        fi
fi
cd $dir_name

install_dir=$(pwd)

cd ..

wget http://www.audeering.com/research-and-open-source/files/openSMILE-2.1.0.tar.gz

tar -zxvf openSMILE-2.1.0.tar.gz

cd openSMILE-2.1.0

sh buildStandalone.sh -p $install_dir >> install_log

cd $install_dir
bin/SMILExtract -h