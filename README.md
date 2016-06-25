Baseline Emotion Recognizer
===============================
Written By- Mahbub Ul Alam

This system recognizes emotion from audio files. It uses openSMILE tool kit to extract the features. For classification it uses SVM machine learning technique. For the classification it uses scikit-learn library.

To know about the features please view the "Feature Description" section.


Dependency
===========
scikit-learn package in python.
For details please see-
http://scikit-learn.org/stable/install.html


Installation
===============
Run the "install_open_smile.sh" script. It will install the openSMILE tool-kit under the current directory. If the download link in the script does not work then please refer to the following download link and install it manually.
 http://audeering.com/research/opensmile/#download

    Example:
    sh install_open_smile.sh


Data Preparation
=================
In order to automatically extract features and build a classifier model from these features the emotion corpus you want to use must be in a simple, standard format which will be briefly described in the following:

• All audio recordings must be available in uncompressed wave format, preferably 16kHz sampling rate and mono or stereo.
	
• All turns for one emotion class should be in a folder named after the class.
	
• To make the automation process easier in my scripts, I have used a specific file naming convention. It is as follows-  

    <ClassNumber>_<ClassName>_<FileNumber>
		
    Example:
    
    Class folders: 
	    sad, anger, fear
	
    File Names:
        (inside "sad" folder)
        	0_sad_0
        	0_sad_1
        	0_sad_2
        	...
	
        (inside "anger" folder)
        	1_anger_0
        	1_anger_1
        	1_anger_2
        	1_anger_3
        	...

        (inside "fear" folder)
        	2_fear_0
        	2_fear_1
        	2_fear_2
        	2_fear_3
        	2_fear_4
        	...
	

Feature Extraction
====================
Run the "feature_extraction.sh" script in the parent directory of openSMILE-x.x.x directory. It takes 3 inputs as follows-

1. Input directory
-----------------
This is the parent directory of the class folders.

2. Configure File name
----------------------
This file contains the information about different types of features. Please provide only the file name without any path inclusion.

To know more about the configuration files please view the "Feature Description" section.

3. Output directory
--------------------
Here output will be generated in Weka ARFF format.

    Example:
    
    sh feature_extraction.sh /mount/projekte15/slu/Projects/Hiwis/Mahbub/emotion_recognizer/sample_input IS13_ComParE.conf 
    /mount/projekte15/slu/Projects/Hiwis/Mahbub/emotion_recognizer/sample_output/batch_output.IS13_ComParE.conf.csv


Data Preprocessing
===================
Run the "data_pre-processing.py" script. It will extract the required data from the feature file(generated in previous section ). This data can be stored  in three different files, based on your choice. The files are,

1. "training_data.txt"
----------------------
If you want to extract and store the training data.

2. "development_data.txt"
-------------------------
If you want to store as test data.

3. "processed_data.txt"
-----------------------
If you want to store it as a whole. This may be useful if you want to perform the cross-validation operation on the data.

    Example:

    chmod +x data_pre-processing.py
    python data_pre-processing.py


SVM Classification
==================
Run the "SVM_Classification.py" script. This script takes "training_data.txt" and "development_data.txt" as input and calculate the predicted class and the accuracy score.

    Example:

    chmod +x SVM_Classification.py
    python SVM_Classification.py


K-fold Cross-Validation
========================
Run the "SVM_cross_validation.py" script. It takes "processed_data.txt" as input and asks the number of fold(k) from the user. It calculates the accuracy score.

    Example:

    chmod +x SVM_cross_validation.py
    python SVM_cross_validation.py


Feature Description
====================

The following subsections will give the details idea about different features.


------------------------------------------------------------------------
The INTERSPEECH 2009 Emotion Challenge feature set The INTERSPEECH 2009
------------------------------------------------------------------------

Emotion Challenge feature set is represented by the configuration file,

    config/emo_IS09.conf


It contains 384 features as statistical functionals applied to low-level descriptor contours. The features are saved in Arff format (for WEKA), whereby new instances are appended to an existing file (this is used for batch processing, where openSMILE is repeatedly called to extract features from multiple files to a single feature file). The names of the 16 low-level descriptors, as they appear in the Arff file, are documented in the following list: 

pcm_RMSenergy 
-------------
    Root-mean-square signal frame energy
mfcc
-----
    Mel-Frequency cepstral coefficients 1-12
pcm_zcr
-------
    Zero-crossing rate of time signal (frame-based)
voiceProb
----------
    The voicing probability computed from the ACF.
F0
----
    The fundamental frequency computed from the Cepstrum.


The suffix "_sma" appended to the names of the low-level descriptors indicates that they were smoothed by a moving average filter with window length 3. The suffix "_de" appended to "_sma" suffix indicates that the current feature is a 1st order delta coefficient (differential) of the smoothed low-level descriptor. The names of the 12 functionals, as they appear in the Arff file, are documented in the following list:

max
----
    The maximum value of the contour
min
---
    The minimum value of the contour
range
-----
    max-min
maxPos
-------
    The absolute position of the maximum value (in frames)
minPos
------
    The absolute position of the minimum value (in frames)
amean
-----
    The arithmetic mean of the contour
linregc1
--------
    The slope (m) of a linear approximation of the contour
linregc2
--------
    The offset (t) of a linear approximation of the contour
linregerrQ
----------
    The quadratic error computed as the difference of the linear approximation and the actual contour
stddev
------
    The standard deviation of the values in the contour
skewness
--------
    The skewness (3rd order moment).
kurtosis
--------
    The kurtosis (4th order moment).

--------------------------------------------------------------------------
The INTERSPEECH 2010 Paralinguistic Challenge feature set
--------------------------------------------------------------------------

The INTERSPEECH 2010 Paralinguistic Challenge feature set (see Proceedings of INTERSPEECH 2010) is represented by the configuration file,

    config/IS10_paraling.conf

The set contains 1 582 features which result from a base of 34 low-level descriptors (LLD) with 34 corresponding delta coefficients appended, and 21 functionals applied to each of these 68 LLD contours (1 428 features). In addition, 19 functionals are applied to the 4 pitch-based LLD and their four delta coefficient contours (152 features). Finally the number of pitch onsets (pseudo syllables) and the total
duration of the input are appended (2 features). The features are saved in Arff format (for WEKA), whereby new instances are appended to an existing file (this is used for batch processing, where openSMILE is repeatedly called to extract features from multiple files to a single feature file). The names of the 34 low-level descriptors, as they appear in the Arff file, are documented in the following list:

pcm loudness
------------
    The loudness as the normalised intensity raised to a power of 0.3.
mfcc
----
    Mel-Frequency cepstral coefficients 0-14
logMelFreqBand
--------------
    logarithmic power of Mel-frequency bands 0 - 7 (distributed over a range from 0 to 8 kHz)
lspFreq
-------
    The 8 line spectral pair frequencies computed from 8 LPC coefficients.
F0finEnv
--------
    The envelope of the smoothed fundamental frequency contour.
voicingFinalUnclipped
----------------------
    The voicing probability of the final fundamental frequency candidate. Unclipped means, that it was not set to zero when is falls below the voicing threshold.

The suffix "_sma" appended to the names of the low-level descriptors indicates that they were smoothed by a moving average filter with window length 3. The suffix "_de "appended to "_sma" suffix indicates that the current feature is a 1st order delta coefficient (differential) of the smoothed low-level descriptor. The names of the 21 functionals, as they appear in the Arff file, are documented in the following list:

maxPos
------
    The absolute position of the maximum value (in frames)
minPos
------
    The absolute position of the minimum value (in frames)
amean
-----
    The arithmetic mean of the contour
linregc1
--------
    The slope (m) of a linear approximation of the contour
linregc2
--------
    The offset (t) of a linear approximation of the contour
linregerrA
----------
    The linear error computed as the difference of the linear approximation and the actual contour
linregerrQ
----------
    The quadratic error computed as the difference of the linear approximation and the actual contour
stddev
------
    The standard deviation of the values in the contour
skewness
--------
    The skewness (3rd order moment).
kurtosis
--------
    The kurtosis (4th order moment).
quartile1
---------
    The first quartile (25% percentile)
quartile2
---------
    The first quartile (50% percentile)
quartile3
---------
    The first quartile (75% percentile)
iqr1-2
------
    The inter-quartile range: quartile2-quartile1
iqr2-3
------
    The inter-quartile range: quartile3-quartile2
iqr1-3
------
    The inter-quartile range: quartile3-quartile1
percentile1.0
-------------
    The outlier-robust minimum value of the contour, represented by the 1% percentile.
percentile99.0
--------------
    The outlier-robust maximum value of the contour, represented by the 99% percentile.
pctlrange0-1
------------
    The outlier robust signal range ‘max-min’ represented by the range of the 1% and the 99% percentile.
upleveltime75
-------------
    The percentage of time the signal is above (75% * range + min).
upleveltime90
--------------
    The percentage of time the signal is above (90% * range + min).

The four pitch related LLD (and corresponding delta coefficients) are as follows (all are 0 for unvoiced regions, thus functionals are only applied to voiced regions of these contours):

F0final
-------
    The smoothed fundamental frequency contour
jitterLocal
-----------
    The local (frame-to-frame) Jitter (pitch period length deviations)
jitterDDP
---------
    The differential frame-to-frame Jitter (the ‘Jitter of the Jitter’)
shimmerLocal
------------
    The local (frame-to-frame) Shimmer (amplitude deviations between pitch periods)

19 functionals are applied to these 4+4 LLD, i.e. the set of 21 functionals mentioned above without the minimum value (the 1% percentile) and the range.

-----------------------------------------------------------------
The INTERSPEECH 2011 Speaker State Challenge feature set
-----------------------------------------------------------------

The configuration file for this set can be found in,

        config/IS11_speaker_state.conf

For details feature set please see the Challenge paper:


    Bjrn Schuller, Anton Batliner, Stefan Steidl, Florian Schiel, Jarek Krajewski: 
    ”The INTERSPEECH 2011 Speaker State Challenge”, Proc. INTERSPEECH 2011,
    ISCA, Florence, Italy, pp. 3201-3204, 28.-31.08.2011.


---------------------------------------------------------
The INTERSPEECH 2012 Speaker Trait Challenge feature set
---------------------------------------------------------

The configuration file for this set can be found in,

    config/IS12_speaker_trait.conf

For details feature set please see the Challenge paper:

    Bjrn Schuller, Stefan Steidl, Anton Batliner, Elmar Nth, Alessandro Vinciarelli, Felix Burkhardt, Rob van Son,
    Felix Weninger, Florian Eyben, Tobias Bocklet, Gelareh Mohammadi, Benjamin Weiss: 
    ”The INTERSPEECH 2012 Speaker Trait Challenge”, Proc. INTERSPEECH 2012, ISCA, Portland, OR, USA, 09.-13.09.2012.

--------------------------------------------------
The INTERSPEECH 2013 ComParE Challenge feature set 
--------------------------------------------------
The configuration file for this set can be found in,

    config/IS13_ComParE.conf
    
A configuration that extracts only the low-level descriptors of the ComParE feature set is provided in,

    config/IS13_ComParE_lld.conf
    
The configuration for the vocaliations (laughter, etc.) sub-challenge is also included in,
   
    config/IS13_ComParE_Voc.conf

For details feature set please see the Challenge paper:

    Bjrn Schuller, Stefan Steidl, Anton Batliner, Alessandro Vinciarelli, Klaus Scherer,
    Fabien Ringeval, Mohamed Chetouani, Felix Weninger, Florian Eyben, Erik Marchi, Marcello Mortillaro, 
    Hugues Salamin, Anna Polychroniou, Fabio Valente, Samuel Kim: 
    ”The INTERSPEECH 2013 Computational Paralinguistics Challenge: Social Signals, Conflict, Emotion, Autism”, 
    to appear in Proc. INTERSPEECH 2013, ISCA, Lyon, France, 2013.

----------------------------------------------------------------------
The MediaEval 2012 TUM feature set for violent video scenes detection
----------------------------------------------------------------------

The feature set for the work on violent scenes detection in popular Hollywood style movies as presented in:

    Florian Eyben, Felix Weninger, Nicolas Lehment, Gerhard Rigoll, Bjrn Schuller: 
    ”Violent Scenes Detection with Large, Brute-forced Acoustic and Visual Feature Sets”, 
    Proc. MediaEval 2012 Workshop, Pisa, Italy, 04.-05.10.2012.

can be found for various settings in,

    config/mediaeval2012_tum_affect

The file,

    MediaEvalAudio_IS12based_subwin2.conf
    
contains the configuration which extracts the static audio features from 2 second sub-windows.

    MediaEval_Audio_IS12based_subwin2_step0.5.conf

extracts the same features, but for overlapping 2 second windows with a shift of 0.5 seconds. 

For the video features the file,

    MediaEval_VideoFunctionals.conf
is provided, which requires a CSV file containing the low-level descriptors (can be extracted with "openCV") as input and outputs and ARFF file with the video features as used in the paper.

-------------------------------------
The openSMILE/openEAR ‘emobase’ set
-------------------------------------

The old baseline set (see the ‘emobase2’ set or the new baseline set) of 988 acoustic features for emotion recognition can be extracted using the following command:

    SMILExtract -C config/emobase.conf -I input.wav -O output.arff

This will produce an ARFF file with a header containing all the feature names and one instance, containing a feature vector for the given input file. To append more instances to the same ARFF file, simply run the above command again for different (or the same) input files. The ARFF file will have a dummy class label called emotion, containing one class unknown by default. To change this behaviour and assign custom classes and class labels to an individual instance, use a command-line like the following:

    SMILExtract -C config/emobase.conf -I inputN.wav -O output.arff -instname
    inputN -classes {anger,fear,disgust} -classlabel anger

Thereby the parameter "-classes" specifies the list of nominal classes including the {} characters, or can be set to numeric for a numeric (regression) class. The parameter "-classlabel" specifies the class label/value of the instance computed from the currently given input ("-I"). For further information on these parameters, please take a look at the configuration file "emobase.conf" where these command-line parameters are defined.

The feature set specified by "emobase.conf" contains the following low-level descriptors (LLD):

    Intensity, Loudness, 12 MFCC, Pitch (F0), Probability of voicing, F0 envelope, 8 LSF (Line Spectral Frequencies), 
    Zero-Crossing Rate. Delta regression coefficients are computed from these LLD, 
    and the following functionals are applied to the LLD and the delta coefficients: Max./Min. value 
    and respective relative position within input, range, arithmetic mean, 2 linear regression coefficients 
    and linear and quadratic error, standard deviation, skewness, kurtosis, quartile 1–3, and 3 inter-quartile ranges.


----------------------------------------
The large openSMILE emotion feature set
----------------------------------------

For extracting a larger feature set with more functionals and more LLD enabled (total 6552 features), use the configuration file,

    config/emo large.conf

Please read the configuration file and the header of the generated arff file for details on the contained feature set.

-----------------------------------------
The openSMILE ‘emobase2010’ reference set
-----------------------------------------

This feature set is based on the INTERSPEECH 2010 Paralinguistic Challenge feature set. It is represented by the file,

    config/emobase2010.conf

A few tweaks have been made regarding the normalisation of duration and positional features. This feature set contains a greatly enhanced set of low-level descriptors, as well as a carefully selected list of functionals compared to the older ‘emobase’ set. This feature set is recommended as a reference for comparing new emotion recognition feature sets and approaches to, since it represents a current state-of-the-art feature set for affect and paralinguistic recognition.

The set contains 1582 features (same as the INTERSPEECH 2010 Paralinguistic Challenge set) which result from a base of 34 low-level descriptors (LLD) with 34 corresponding delta coefficients appended, and 21 functionals applied to each of these 68 LLD contours (1428 features). In addition, 19 functionals are applied to the 4 pitch-based LLD and their four delta coefficient contours (152 features). Finally the number of pitch onsets (pseudo syllables) and the total duration of the input are appended (2 features). The only difference to the INTERSPEECH 2010 Paralinguistic Challenge set is the normalisation of the ‘maxPos’ and ‘minPos’ features which are normalised to the segment length in the present set.

Further Reading
================

For gaining a deeper knowledge these links can be helpful,

1. http://www.audeering.com/research-and-open-source/files/openSMILE-book-latest.pdf

2. http://scikit-learn.org/stable/index.html