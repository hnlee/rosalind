#Given: A DNA string t having length at most 1000 nt.

#Return: The transcribed RNA string of t.

from string import replace

def transcribe(string):
    upper_string = string.upper()
    return(replace(upper_string, "T", "U"))

input_file = 'rosalind_rna.txt'
input = open(input_file,'r')

sequence = "".join([line[:-1] for line in input])
transcript = transcribe(sequence)

print transcript
