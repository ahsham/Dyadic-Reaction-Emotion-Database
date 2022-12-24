# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# # ffmpeg_extract_subclip("full.mp4", start_seconds, end_seconds, targetname="cut.mp4")
# ffmpeg_extract_subclip("f1_pilot_s1_g1_v5_pilot_s2_g2_v2_01.mp4", 250, 261, targetname="f1.mp4")

# Import everything needed to edit video clips
from moviepy.editor import *
from os import listdir, makedirs
from os.path import isfile, join, exists

def cutit(filename,scenario,v1,v2,name1):
	count1 = 0
	count = 6
	ii = [["1","1","2","2","3","3"],
		  ["2","2","3","3","1","1"],
		  ["3","3","1","1","2","2"],
		  ["1","1","3","3","2","2"],
		  ["2","2","1","1","3","3"],
		  ["3","3","2","2","1","1"]]
	sg1 = [[ 15,16, 16,16, 16,15], 
		   [ 16,16, 16,15, 15,16], 
		   [ 16,15, 15,16, 16,16],
		   [ 15,16, 16,15, 16,16],
		   [ 16,16, 15,16, 16,15],
		   [ 16,15, 16,16, 15,16]]
	sg2 = [[ 16,16, 15,16, 16,15],
		   [ 15,16, 16,15, 16,16],
		   [ 16,15, 16,16, 15,16],
		   [ 16,16, 16,15, 15,16],
		   [ 15,16, 16,16, 16,15],
		   [ 16,15, 15,16, 16,16]]

	lv1 = sg1[int(v1)-1]
	lv2 = sg2[int(v2)-1]
	print(lv1,lv2)

	fl = 'out3/'+scenario+'/'
	if not exists(fl):
		makedirs(fl, mode=0o777)
	else:
		print("Name already exists!")

	if not exists(fl+'male/'):
		makedirs(fl+'male/', mode=0o777)
	else:
		print("Name already exists!")

	if not exists(fl+'female/'):
		makedirs(fl+'female/', mode=0o777)
	else:
		print("Name already exists!")

	# 1.need to separate male and female. 2. separate sg1 and sg2. 3. split time accuracy
	it = lv1
	flname_f = fl+"male/"+fm+"_sg1_clip"
	flname_m = fl+"female/"+fm+"_sg1_clip"
	iii = int(v1)-1
	while count< 261:
		if count1 ==6:
			count1= 0
			it = lv2
			flname_m = fl+"male/"+fm+"_sg2_clip"
			flname_f = fl+"female/"+fm+"_sg2_clip"
			iii = int(v2)-1

		for idx,seq_time in enumerate(it):
			
			print("coun1: ", count1)
			# loading video gfg
			clip = VideoFileClip(filename)
			# getting only first 5 seconds
			clip = clip.subclip(count, count+seq_time)
			# showing clip
			# clip.ipython_display(width = 360)
			count = count + seq_time + 6
			if idx % 2:
				clip.write_videofile(flname_f+str(count)+"_"+ii[iii][idx]+".mp4")
			else :
				clip.write_videofile(flname_m+str(count)+"_"+ii[iii][idx]+".mp4")

			count1+=1


if __name__=="__main__":
	a = ['M',"F"]
	for i in a:
		for j in range(30):
			num = str(j+1)
			filename = i+'/'+i.lower()+num+'/'
			print(filename)
			onlyfiles = [fl for fl in listdir(filename) if isfile(join(filename, fl))]
			print(onlyfiles)
			for x in onlyfiles:
				print(filename+x+'/')
				z = x.split('.')
				y = z[0].split('_')
				# print(z[0])
				# print(y)
				fm = y[0]
				v1 = y[4][1]
				v2 = y[8][1]
				scenario = y[9][1]
				# print("scenario: ",scenario," s1g1: ",v1," s2g2: ",v2 )
				# y[4] for s1 g1
				# y[8] for s2 g2
				# y[9] for variant/iteration
				cutit(filename+x,scenario,v1,v2,fm)