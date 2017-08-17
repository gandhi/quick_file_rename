import sys
import os
import re

def get_matching_files(remove_string, all_files):
	for index, file in enumerate(all_files):
		if file.find(remove_string) is -1:
			all_files.pop(index)
	return all_files

def rename_files(folder, files, match_string, replace_string):
	folder = folder + '/'
	for file in files:
		os.rename(folder + file, folder + file.replace(match_string, replace_string))

def delete_string_in(folder):
	all_files = os.listdir(folder) 
	if len(all_files) is 0:
		print 'No files in directory!'
		sys.exit(1)
	remove_string = raw_input("> What is the string you would like to delete?: ")
	replace_string = raw_input("> What is the string you would like to replace it with?: ")
	good_files = get_matching_files(remove_string, all_files)
	if len(good_files) is 0:
		print 'No matching files!'
		sys.exit(1)
	rename_files(folder, good_files, remove_string, replace_string)		

if __name__ == '__main__':
	folder = sys.argv[1]
	if not os.path.isdir(folder):
		print 'Not a folder!'
		sys.exit(1)
	delete_string_in(folder)	
