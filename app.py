import os

# Crea un directorio
def create_directory():
    directory = "/Users/cristhian/Proyectos/basch/Project2/sequences/"
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)
    return directory


# procesa el file .fasta
def process_file(file):
    input = open(file)
    for line in input:
        if line[0] == '>':
            output = open(create_directory() + line + '_seq.fasta', 'w')
            output.write(line)
        else:
            output.write(line)

    input.close()
    output.close()

# arranca el programa
if __name__ == '__main__':
    process_file('aves.fasta')
