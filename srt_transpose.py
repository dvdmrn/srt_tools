import re
import core

"""
SRT TRANSPOSE

adds or removes time (in ms) to all dialogue in a .srt file

"""



#---------------------------------------
# change these to affect transposition
#---------------------------------------
transpose = -57625 # in ms
filename = "srt_files/p2.srt"
#---------------------------------------


def convertTimecodeToMs(tc):
	h =  int(tc[0:2])
	m =  int(tc[3:5])
	s =  int(tc[6:8])
	ms = int(tc[9:12])
	seconds = (h*3600)+(m*60)+s
	full = (seconds*1000)+ms
	return full


def convertMsToTimecode(ms):
	l_ms = ms%1000
	ms-=l_ms
	hrs = ms/3600000
	ms -= hrs*3600000
	m = ms/60000
	ms -= m*60000
	s = ms/1000
	tc = '%02d'%hrs+":"+'%02d'%m+":"+'%02d'%s+","+'%03d'%l_ms
	return tc


def addTime(tc,toAdd):
	ms = convertTimecodeToMs(tc)
	ms = ms + toAdd
	return convertMsToTimecode(ms)


def processTimecodes(tc,timeToAdd):
	print "\n-----\nconverting: "+str(tc)
	tc[0] = addTime(tc[0], timeToAdd)
	tc[1] = addTime(tc[1], timeToAdd)
	print "         >> "+str(tc)
	return tc

def writeFile(filename,toWrite):
    with open(filename[:-4]+'_transposed.srt','w') as outputFile:
	    print("\n........................................\noutputting file as: "+filename[:-4]+'_transposed.srt\n........................................')
	    for e in toWrite:
	        outputFile.write("%s\n" % e)

def formatTimecodes(toFormat):
	for i in xrange(0,len(toFormat)):
		if isinstance(toFormat[i],list):
			toFormat[i] = toFormat[i][0]+" --> "+toFormat[i][1]


def main():
	print("\n........................................\nopening file: "+filename+'\n........................................')
	inputList = core.getText(filename)	

	for i in range(0,len(inputList)):
		m = re.findall(r"\d{2}:\d{2}:\d{2},\d{3}", inputList[i])
		if m:
			newTC = processTimecodes(m,transpose)
			inputList[i] = newTC

	formatTimecodes(inputList)

	core.writeFile(filename, inputList)



		


main()