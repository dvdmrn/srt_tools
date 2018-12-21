
from math import floor


def getText(filename):
	lst = []
	with open(filename) as inputfile:
	    for line in inputfile:
	        lst.append(line.strip())
	return lst


def writeFile(filename,toWrite):
    with open(filename[:-4]+'_numbered.srt','w') as outputFile:
	    print("\n........................................\noutputting file as: "+filename[:-4]+'_numbered.srt\n........................................')
	    for e in toWrite:
	        outputFile.write("%s\n" % e)




def frames_to_ms(frames,fps):
	proportion = frames/float(fps)
	return int(math.floor(proportion*1000))
