#!/bin/bash

#=====================================================================================
#this script is a step by step procedure to extract the features
#and classify them using SCI-Kit tool in SVM.
#for details pleasee see the readme section.

# Written by Mahbub Ul Alam
#=====================================================================================

export LC_ALL=C

echo "==============================================================
this script is to extract the features

You must give 3 inputs to run the script as follows,
audio_files_location
configuration_file_name
output_csv_file_location

otherwise it will cause error

for details please see the readme section.
====================================================================

"

#this script takes 3 input for the feature extraction.
input_audio_files_location=$1
configuration_file_name=$2 #caution: only put the name here, not the full location.
output_csv_file_location=$3


cd openSMILE-2.1.0/scripts/modeltrain/

#this script will extract the features from audio file
#for different featurer and different configuration files-
#please see the read-me section
perl stddirectory_smileextract.pl $input_audio_files_location $configuration_file_name $output_csv_file_location

echo "
===============================================
Features Successfully Extracted from audio files
=====================================================

"

cd ../../../