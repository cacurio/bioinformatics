#!/bin/python3

import os
import sys
import subprocess
import shutil

#subprocess.call('esearch -db protein -query "Aves[organism] AND G6PC NOT PARTIAL" | efetch -db protein -format acc > aves.txt', shell=True)

subprocess.call('esearch -db protein -query "Aves[organism] AND G6PC NOT PARTIAL" | efetch -db protein -format fasta > aves.fasta', shell=True)


#subprocess.call('clustal -i aves.fasta -o aves_out.fasta -v', shell=True)

#subprocess.call('plotcon aves.fasta -graph svg', shell=True)


