import os
import csv
import sys
import json

classes = {
	"/m/09x0r" : "Speech",
	"/m/07y_7" : "Violin",
	"/m/0bt9lr" : "Dog",
	"/m/07yv9" : "Vehicle",
	"/m/014zdl" : "Explosion",
	"/m/04szw" : "MusicalInstrument",
	"/m/03m9d0z" : "Wind",
	"/m/03kmc9" : "Siren",
	"/m/015p6" : "Bird",
	"/m/07rdhzs" : "Whack"
}

class_counts = {
	"Speech" : 0,
	"Violin" : 0,
	"Dog" : 0,
	"Vehicle" : 0,
	"Explosion" : 0,
	"MusicalInstrument" : 0,
	"Wind" : 0,
	"Siren" : 0,
	"Bird" : 0,
	"Whack" : 0
}

subset = open("unbalanced_subset.csv", "w")
seg = open("unbalanced_train_segments.csv", "r")
seg_reader = csv.reader(seg, delimiter=',')

for row in range(3) :
	for col in next(seg_reader) :
		subset.write(col + ",")
	subset.write('\n')

def quote(phrase) :
	return '"' + phrase + '"'

# For each row in unbalanced_train_segments
for row in seg_reader :

	# Iterate through the columns
	for col in row :

		# Check if the row belongs to one of the classes we selected, and 
		# if it does, add it to eval_subset and add it to class_counts
		s_col = col.replace('"','').replace(' ','')
		if s_col in classes :
			class_counts[classes[s_col]] += 1
			subset.write(row[0] + ", " + row[1] + ", " + row[2] + ", " + quote(classes[s_col]) + "\n")
			break

	# Stop adding to eval_subset after 500 examples
	for classname in class_counts :
		if class_counts[classname] >= 500 :
			for key, value in dict(classes).items() :
				if value == classname :
					del classes[key]
			del class_counts[classname]
			break

for el in class_counts :
	print el + ":" + str(class_counts[el])