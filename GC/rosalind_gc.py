#Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
#
#Return: The ID of the string having the highest GC-content, followed by the
#GC-content of that string. Rosalind allows for a default error of 0.001 in all
#decimal answers unless otherwise stated; please see the note on absolute error
#below.

def calc_gc(string):
    upper_string = string.upper()
    return (upper_string.count('G') + upper_string.count('C')) / float(len(upper_string))

input_file = 'rosalind_gc.txt'
input = open(input_file, 'r')

sequences = {}
name = ''
for line in input:
    if line[0] == '>':
        name = line[1:-1]
        sequences[name] = ''
    else:
        sequences[name] += line[:-1]

gc = [calc_gc(sequences[sequence]) for sequence in sorted(sequences.keys())]
print sorted(sequences.keys())[gc.index(max(gc))]
print max(gc)*100
