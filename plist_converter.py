#!/usr/bin/python
__author__ = 'Morgan Hough'
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:52:36 2013

@author: mhough
"""
import argparse, csv, os, plistlib
parser = argparse.ArgumentParser(description='Converts Mac OS X Property List Data to a CSV file and metadata to a text file')
parser.add_argument('-i','--input', dest='filename', required=True, help="path to plist file")
parser.add_argument('-v','--verbosity', dest='verbose', help='increase output verbosity', action="store_true")
args = parser.parse_args()

# Reading file
print 'Processing plist file'
input = open(args.filename)
data = plistlib.readPlist(input)
input.close()

if 'name' not in data:
    subject=data['subjectID']
else:
    subject=data['name']

# Report metadata and write out textfile of metadata
print 'Processing subject '+ subject + ' in study ' + data['studyID']
print 'Outputing metadata in text file'
textfile = open(data['studyID']+ subject + '.txt','wb')
for item in data.keys():
	if item == 'logData':
		pass
	else: 
		if args.verbose:
			print item + ' ' + str(data[item])
		textfile.write(item + ' ' + str(data[item]) + os.linesep)

textfile.close()

# Write out new CSV file
print 'Outputing CSV file'
writer = csv.writer(open(data['studyID']+subject + '.csv', 'wb'))
writer.writerow(data['logData'][0].keys())
for trials in data['logData']:
	writer.writerow(trials.values())
