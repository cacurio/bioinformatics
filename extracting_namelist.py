#!/bin/python

import os
import sys
import subprocess

input_file1=open('aves.fasta')
input_file1

sign=">"

species_list_names=[]

for each_line in input_file1:
	if each_line[0] == sign:
		print(each_line)
		species_list=each_line.replace("]",'').rstrip().split("[")
		species_list_names.append(species_list[1])

len(species_list_names)
len(set(species_list_names))





	
			
		
		
		
			
