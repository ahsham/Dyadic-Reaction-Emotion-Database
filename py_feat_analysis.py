# pip install -q py-feat

from feat.detector import Detector
import os
import os.path
import os,glob

detector = Detector(verbose=False)
folder_path = 'out3/'
output_path = 'py_feat_analysis/csv/'
gen = ['male','female']
for scenario in range(5):
  sc = scenario+1
  for g in gen:
    folder= folder_path+str(sc)+'/'+g+'/'
    outputf = output_path+str(sc)+'/'+g+'/'
    for filename in glob.glob(os.path.join(folder, '*.mp4')):
      print(filename)
      filef = filename.split("/")
      print(filef)
      filef = filef[-1].split("\\")
      print(filef)
      out1 = outputf+str(filef[-1])+".csv"
      print(out1)
      file_exists = os.path.exists(out1)
      if file_exists == False:
        video_prediction = detector.detect_video(filename, outputFname = out1)
