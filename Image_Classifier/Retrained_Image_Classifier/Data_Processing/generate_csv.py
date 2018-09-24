import os
import ntpath
import csv
import random 

DATA_DIRECTORY = "../ImageData"
LABELS = None

labels_file = open(“testfile.txt”, “r”) 
for label in labels_file: 
	LABELS.append(label)



def filter(dirName, ratio):
	index = LABELS.index(ntpath.basename(dirName))
	if index >= 0:
		if random.random() < ratio[index]:
			return True
	return False


def generate(rootDir, output_file, ratio = [1, 1, 1, 1]):
	data = open(output_file, 'w')
	writer = csv.writer(data)
	for dirName, subdirList, fileList in os.walk(rootDir):
		print('Found directory: %s' % dirName)
		if ntpath.basename(dirName) in LABELS:
			for fname in fileList:
				if fname != ".DS_Store":
					if (filter(dirName, ratio)):
						writer.writerow([os.path.join(dirName, fname), ntpath.basename(dirName)])

if __name__ == "__main__":
	# generate(DATA_DIRECTORY, "nuclei.csv")
	generate(DATA_DIRECTORY, "data.csv")