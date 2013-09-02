#Given: A DNA string s of length at most 1000 bp.

#Return: The reverse complement sc of s.

def rev_compl(string):
    upper_string = string.upper()
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
    return ''.join([complement[base] for base in upper_string[::-1]])

input_file = 'rosalind_revc.txt'
input = open(input_file, 'r')

sequence = ''.join([line[:-1] for line in input])
print rev_compl(sequence)

