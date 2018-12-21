import re
import core

"""
SRT NUMBER

ensures that all dialogue in an .srt file is numbered n+1
"""



#---------------------------------------
# set file path here
#---------------------------------------
filename = "srt_files/combined.srt"
#---------------------------------------


def main():
	
	acc = 1


	# reads file
	print("\n........................................\nopening file: "+filename+'\n........................................')
	inputList = core.getText(filename)	

	for i in range(0,len(inputList)):
		m = re.findall(r"\d{2}:\d{2}:\d{2},\d{3}", inputList[i])
		if m:
			print("adjusting "+inputList[i-1]+"~>"+str(acc))
			inputList[i-1] = acc
			acc+=1

	core.writeFile(filename, inputList)


main()