#Given: A DNA string s of length at most 1000 nt.
#
#Return: Four integers (separated by spaces) counting the respective number of
#times that the symbols 'A', 'C', 'G', and 'T' occur in s.

def count_nucleotides(string):
    upper_string = string.upper()
    return([upper_string.count("A"),
            upper_string.count("C"),
            upper_string.count("G"),
            upper_string.count("T")])

input_file = 'rosalind_dna.txt'
input = open(input_file, 'r')

sequence = "".join([line[:-1] for line in input])
nucleotides = count_nucleotides(sequence)
print " ".join([str(int) for int in nucleotides])
