import pandas as pd
import numpy as np
import csv
from datetime import datetime
def clean_csv(f):

	data = pd.read_csv(f)
	p1frame = []
	p1angry = []
	p1disgust = []
	p1fear = []
	p1happy = []
	p1sad = []
	p1surprise = []
	p1neutral = []
	p2frame = []
	p2angry = []
	p2disgust = []
	p2fear = []
	p2happy = []
	p2sad = []
	p2surprise = []
	p2neutral = []

	max_frame = int(len(data['frame'])/2)
	count = 0
	frame = 0
	for idx in range(len(data['frame'])):
		if frame == data['frame'][idx]:
			if data['x_0'][idx] < 500:

				count+=1
				p1frame.append(data['frame'][idx])
				p1angry.append(data['anger'][idx])
				p1disgust.append(data['disgust'][idx])
				p1fear.append(data['fear'][idx])
				p1happy.append(data['happiness'][idx])
				p1sad.append(data['sadness'][idx])
				p1surprise.append(data['surprise'][idx])
				p1neutral.append(data['neutral'][idx])
			elif data['x_0'][idx] >= 500:
				count+=1
				p2frame.append(data['frame'][idx])
				p2angry.append(data['anger'][idx])
				p2disgust.append(data['disgust'][idx])
				p2fear.append(data['fear'][idx])
				p2happy.append(data['happiness'][idx])
				p2sad.append(data['sadness'][idx])
				p2surprise.append(data['surprise'][idx])
				p2neutral.append(data['neutral'][idx])
		if count == 2:
			count=0
			frame+=1

	for i in p1frame:
		if i not in p2frame:
			del p1frame[i]
			del p1angry[i]
			del p1disgust[i]
			del p1fear[i]
			del p1happy[i]
			del p1sad[i]
			del p1surprise[i]
			del p1neutral[i]
			

	for i in p2frame:
		if i not in p1frame:
			del p2frame[i]
			del p2angry[i]
			del p2disgust[i]
			del p2fear[i]
			del p2happy[i]
			del p2sad[i]
			del p2surprise[i]
			del p2neutral[i]

	p1 = [p1frame,p1angry,p1disgust,p1fear,p1happy,p1sad,p1surprise,p1neutral]
	p2 = [p2frame,p2angry,p2disgust,p2fear,p2happy,p2sad,p2surprise,p2neutral]

	return p1, p2

def vas_emote(p):
	frame, anger, disgust, fear, happy, sad, surprise, neutral = p
	count = 0
	countp = 0
	countn = 0
	for i in range(len(frame)):
		# print(i,frame[i],round(anger[i],4),round(disgust[i],4),round(fear[i],4),round(happy[i],4),round(sad[i],4),round(surprise[i],4),round(neutral[i],4),round(anger[i],4)+round(fear[i],4)+round(happy[i],4)+round(sad[i],4)+round(surprise[i],4)+round(neutral[i],4))
		# if anger[i]+disgust[i]+fear[i]+happy[i]+sad[i]+surprise[i]+neutral[i] > 1:
		# 	count+=1
		positive =round(happy[i],4)+round(surprise[i],4)
		negative = round(anger[i],4)+round(sad[i],4)
		if positive>negative:
			countp+=1
			if positive>neutral[i]:
				max_emo = "Positive"
				conf = round(positive,4)
			else:
				max_emo = "Neutral"
				conf = round(neutral[i],4)
		else:
			countn+=1
			if negative>neutral[i]:
				max_emo = "Negative"
				conf = round(negative,4)
			else:
				max_emo = "Neutral"
				conf = round(neutral[i],4)
		# print("Positive: ",positive,"Negative: ",negative,"Neutral: ",neutral[i])
		print(frame[i],max_emo,conf)
	print(count,countp,countn)

def writeit(p):
	now = datetime.now() # current date and time
	data111= now.strftime("%m_%d_%Y_%H_%M_%S")
	f = data111+'.csv'
	col = ['frame','anger','disgust','fear', 'happy','sad','surprise','neutral']
	df = pd.DataFrame(columns=col)
	df.to_csv(f)
	frame, anger, disgust, fear, happy, sad, surprise, neutral = p
	for i in range(len(frame)):
		col = [{'frame':frame[i],'anger':anger[i],'disgust':disgust[i],'fear':fear[i], 'happy':happy[i],'sad':sad[i],'surprise':surprise[i],'neutral':neutral[i]}]
		# add row to csv with an index
		df = df.append(col,ignore_index=True)
		# write to csv
		df.to_csv(f)

if __name__ == '__main__':

	f = 'csv/1/female/f1_sg1_clip28_2.mp4.csv'
	p1,p2 = clean_csv(f)
	# vas_emote(p1)
	# vas_emote(p2)
	writeit(p2)


	

