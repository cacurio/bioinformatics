import os
import re

EXTENSION_FILE = '.fasta'


# Crea un directorio
def create_directory():
    path = os.path.dirname(os.path.realpath(__file__)) + "/sequences/"
    try:
        os.stat(path)
    except:
        os.mkdir(path)
    return path


# obtener el nombre del archivo
def regex_head(head):
    segment = re.search(r'>(\w*.\d*)', head)
    return segment.group(1)


# procesa el file .fasta
def process_file(file):
    input = open(file)
    directory = create_directory()
    for line in input:
        if line[0] == '>':
            name_file = regex_head(line)
            output = open(directory + name_file + EXTENSION_FILE, 'w')
            output.write(line)
        else:
            output.write(line)

    input.close()
    output.close()


# arranca el programa
if __name__ == '__main__':
    process_file('aves.fasta')
