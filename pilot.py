import cv2
import numpy as np
import imutils
import random
import sys
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
import time

def emergevid(name, iteration, path, path1):
	c1 = 'records/'+name+'/'+iteration+"/video_0_"+path+".mp4"
	c2 = 'records/'+name+'/'+iteration+"/video_1_"+path1+".mp4"
	clips = []
	clips.append(c1)
	clips.append(c2)
	pname = []
	for clip in clips:
		pname.append(VideoFileClip(clip))

	final_clip = concatenate_videoclips(pname)
	final_clip.write_videofile('records/'+name+"/"+name+"_"+path+"_"+path1+"_0"+iteration+".mp4")

def msgdis(count):
	count=count -1

	arr = ["Suppose these people are your best friends", "Suppose these people are your colleagues/acquitances",
	 "Suppose these people are strangers", "Suppose these people are people you hate", "Suppose these people are dangerous and you are afraid of them"]

	return arr[count]

def manage_process(name, iteration, path, path1):

	for i in range(2):
		if i == 0: 
			path = path
			pname = 'records/'+name+'/'+iteration+"/video_"+str(i)+"_"+path+".mp4"
			# print("video 1")
			
			

		elif i ==1:
			path = ""
			path = path1
			pname = ""
			pname = 'records/'+name+'/'+iteration+"/video_"+str(i)+"_"+path+".mp4"
			# print("video 2")


		# Create a VideoCapture object and read from input file 
		path = 'all/'+path+".mp4"
		# cap1 = cv2.VideoCapture(path)

		cap= cv2.VideoCapture(0+cv2.CAP_DSHOW)
		cap1 = cv2.VideoCapture(path,0)
		

		width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
		# print("width and height: ",width,height)

		writer= cv2.VideoWriter(pname, cv2.VideoWriter_fourcc(*'DIVX'), 25.0, (1280,480))

		if (cap1.isOpened()== False): 
			print("Error opening video file")

		while(cap1.isOpened()):

		    ret, frame = cap.read()
		    ret1, frame1 = cap1.read()
		    
		    if ret1 == True:
		    	rerese = cv2.resize(frame1, (640,480))
		    	both = np.concatenate((frame, rerese), axis=1)
		    	rame1 = 'cap1'
		    	cv2.namedWindow(rame1,cv2.WND_PROP_FULLSCREEN)
		    	cv2.setWindowProperty(rame1,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
		    	# cv2.imshow('Frame', both)
		    	cv2.imshow(rame1,frame1)
		    	writer.write(both)

		    	if cv2.waitKey(19) & 0xFF == ord('q'):
		        	break


		    else: 
		        break

		if i == 0:
			cap.release()
		elif i == 1:
			cap.release()
			# Closes all the frames 
			cv2.destroyAllWindows()


if __name__ == '__main__':
	while True:
		aa = input("Press s to start or q to quit: ")
		if aa == 's' or aa == 'S':
			name = input("Enter name: ")
			if not os.path.exists('records/'+name):
			    os.makedirs('records/'+name)
			else:
				print("Name already exists!")

			count = 1
			while count<6:
				# print(count)
				iteration = str(count)
				if not os.path.exists('records/'+name+'/'+iteration):
					os.makedirs('records/'+name+'/'+iteration)
				else:
					print("Iteration already exists! WARNING:: You may lose data if you proceed!!")
					sss = input("Proceed? (y/n): ")
					if sss == 'y' or sss == 'Y':
						print("loading...")
					elif sss == 'n' or sss == 'N':
						print("Abort!!")
						sys.exit()

				if count==1:
					print("\033[H\033[J",end="")
					msg = msgdis(count)
					print("**************************************************************************************************************************************")
					print("**************************************************************************************************************************************")
					print("\t \t \t \t"+msg)
					print("\t \t \t \t Scenario: "+ str(count) +" of 5")
					print("**************************************************************************************************************************************")
					print("**************************************************************************************************************************************")
					time.sleep(15)
					print("\033[H\033[J",end="")

				num1 = str(random.randint(1,6))
				num2 = str(random.randint(1,6))
				# print(num1,num2)

				path = "pilot_s1_g1_v"+num1
				path1 = "pilot_s2_g2_v"+num2

				# print(path,path1)

				manage_process(name,iteration,path,path1)

				count=count+1
				if count < 6:
					msg = msgdis(count) 
				

					print("**************************************************************************************************************************************")
					print("**************************************************************************************************************************************")
					print("\t \t \t \t"+msg)
					print("\t \t \t \t Scenario: "+ str(count) +" of 5")
					print("**************************************************************************************************************************************")
					print("**************************************************************************************************************************************")
					
				emergevid(name, iteration, path, path1)
				print("\033[H\033[J",end="")
				# input()
				
		elif aa == 't' or aa == 'T':
			name = input("Enter name: ")
			name = 'training_'+name
			if not os.path.exists('records/'+name):
			    os.makedirs('records/'+name)
			else:
				print("Name already exists!")

			count = 1
			while count<2:
				# print(count)
				iteration = str(count)
				if not os.path.exists('records/'+name+'/'+iteration):
					os.makedirs('records/'+name+'/'+iteration)
				else:
					print("Iteration already exists! WARNING:: You may lose data if you proceed!!")
					sss = input("Proceed? (y/n): ")
					if sss == 'y' or sss == 'Y':
						print("loading...")
					elif sss == 'n' or sss == 'N':
						print("Abort!!")
						sys.exit()
				
				if count==1:
					print("\033[H\033[J",end="")
					msg = msgdis(count)
					print("**************************************************************************************************************************************")
					print("**************************************************************************************************************************************")
					print("\t \t \t \t"+msg)
					print("**************************************************************************************************************************************")
					print("**************************************************************************************************************************************")
					time.sleep(15)
					print("\033[H\033[J",end="")



				num1 = str(random.randint(1,6))
				num2 = str(random.randint(1,6))
				# print(num1,num2)

				path = "training_s1_g1_v"+num1
				path1 = "training_s2_g2_v"+num2

				manage_process(name,iteration,path,path1)
				count=count+1
				
				if count<6:
					msg = msgdis(count)

					print("**************************************************************************************************************************************")
					print("**************************************************************************************************************************************")
					print("\t \t \t \t"+msg)
					print("**************************************************************************************************************************************")
					print("**************************************************************************************************************************************")
					
				emergevid(name, iteration, path, path1)
				print("\033[H\033[J",end="")
				# input()

		elif aa == 'q' or aa == 'Q':
			print("Exiting script!!")
			sys.exit()


	



	

	


