# Dyadic-Reaction-Emotion-Database
This repository contains the codes that enables researchers to collect facial expressions of a person via a webcam while watching a video. Also provided the codes that can be used to separate them if needed.

## To get started with python

Kindly make sure to have the following libraries
```
pip install opencv-python, numpy, imutils, random2, sys, os, moviepy, time
```

## Data collection
To collect data, you can run the following below:
```
python pilot.py
```
After collecting the data, if you wish to separate all the subjects and participants, then alter the file location in the vsplit.py and run the following:
```
python vsplit.py
```
## Py-Feat Toolkit

We added the codes for analyzing the videos using the py-feat facial expression analysis toolkit. To generate the analysis from video to csv file, run:
```
python py_feat_analysis.py
```

#### Make sure to change the input and destination folders before running it. The same applies for the code below.

Once the analysis is over, you can use the following script to separate the people's facial expressions accordingly using the following:
``` 
python analyse_csv_pyfeat.py
```

