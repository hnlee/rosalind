# Given: A string Text as well as integers k and d.`

# Return: All most frequent k-mers with up to d mismatches in Text.

from itertools import combinations

nucleotides = set(['A','C','T','G'])

def find_kmers(string, k):
    upper_string = string.upper()
    unique_kmers = {}
    kmers = (upper_string[i:(i+k)]
             for i in xrange(len(upper_string)+1-k))
    for kmer in kmers:
        if kmer in unique_kmers:
            unique_kmers[kmer] += 1
        else:
            unique_kmers[kmer] = 1
    return unique_kmers

def all_dmers(d):
    dmers = nucleotides
    for i in xrange(d-1):
        dmers = [x + y for x in dmers for y in nucleotides]
    return dmers

def generate_mismatches(kmer, indices, mismatches):
    new_kmer = list(kmer)
    for i, j in enumerate(indices):
        new_kmer[j] = mismatches[i]
    return ''.join(new_kmer)

input_file = 'rosalind_ba1i.txt'
input = open(input_file, 'r')

for line in input:
    if line[0].upper() in nucleotides:
        text = line[:-1]
    else:
        [k, d] = [int(num) for num in line[:-1].split()]

input.close()

mismatch_indices = [indices for indices in combinations(xrange(k),d)]
mismatch_set = all_dmers(d)

kmer_set = find_kmers(text, k)
kmer_freq = {}
for kmer in kmer_set:
    all_mismatches = (generate_mismatches(kmer, i, j)
                          for i in mismatch_indices
                          for j in mismatch_set)
    unique_mismatches = []
    for mismatch in all_mismatches:
        if mismatch in unique_mismatches:
            continue
        elif mismatch in kmer_freq:
            kmer_freq[mismatch] += kmer_set[kmer]
        else:
            kmer_freq[mismatch] = kmer_set[kmer]
        unique_mismatches += [mismatch]

max_freq = max(kmer_freq.values())
print ' '.join([kmer for kmer in kmer_freq 
                if kmer_freq[kmer] == max_freq])
