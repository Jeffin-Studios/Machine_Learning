import numpy as np
import os
import ntpath
import glob
import shutil
# from PIL import Image



#Make a function that creates the labels.txt file in data_scripts that build_image_data depends on
def make_label_file(labels):
	label_file = open("label_names.txt", "w")
	for label in labels:
		label_file.write(label+'\n')
	label_file.close()


def write_data(source):
	labels = []
	dirList = []
	scan_name = ""
	for dirName, subdirList, fileList in os.walk(source):
		print('Found directory: %s' % dirName)
		label = ntpath.basename(dirName)
		if dirName == source:
			dirList = subdirList
		else:
			if label in dirList:
				labels.append(label)

	make_label_file(labels)


if __name__ == "__main__":
	SOURCE_DIRECTORY = "../ImageData" 
	write_data(SOURCE_DIRECTORY)
