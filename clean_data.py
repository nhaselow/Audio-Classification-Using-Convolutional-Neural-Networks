import os
import csv
import sys
import json

def trim_csv() :
	train = open("train_unbalanced_5000.csv", "w")
	train.write("Filename,Class Label\n")

	ontology = open("./ontology/ontology.json", "r")
	ontol_json = json.load(ontology)

	counter = 0

	# For each spectrogram
	for imgname in os.listdir("./spectrograms/") :
		seg = open("unbalanced_subset.csv", "r")
		seg_reader = csv.reader(seg, delimiter=',')
		validImg = False

		# For each row in the eval_subset.csv file
		for row in seg_reader :

			# If the filename matches the current spectrogram's name
			if(row[0] in imgname) :

				# Match the class label with the name in the ontology JSON file
				classname = row[3]
				#for dict in ontol_json :
				#	if row[1].replace(' ', '').replace('"','') in dict["id"] :
				#		classname = dict["name"]

				# Write to train.csv and rename the file to match
				train.write(row[0] + ".png," + classname.split(',', 1)[0].replace('"','') + "\n")
				os.rename("./spectrograms/" + imgname, "./spectrograms/" + row[0] + ".png")
				validImg = True

		# Remove any images that aren't in the eval_segments.csv
		if not validImg :
			os.remove("./spectrograms/" + imgname)

		counter = counter + 1
		if counter%100 == 0 :
			print(str(counter) + " are complete")
		seg.close()
		
	print("Done.")


trim_csv()
