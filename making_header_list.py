#!/bin/python3

import os
import sys
import subprocess

input_file1=open('aves.fasta')
output_file1=open("headers_1.txt", 'w')

sign=">"

for each_line in input_file1:
	if each_line[0] == sign:
                print(each_line)
		lines=each_line.replace(">","")
		lines		 
		output_file1.write(lines) 

output_file1.close()
                


