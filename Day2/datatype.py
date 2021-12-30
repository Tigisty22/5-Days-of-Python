""" 
# Data types
# Numbers(int, float, complex)
# Integers --- -3, -2, -1, 0, 1, 2, 3, ----
# Floats: Numbers with decimal eg 3.14, 1.5, 96.7, 9.81
# Complex Number: 2 + 2j, 1 + 4j, 
# Strings: are texts
# Booleans(True or False)
# List, Set, Tuple, Dictionary

# Bultin Function we use to check a type: type()

# Numbers(Int, float, Complext)
print(type(10))
print(type('10'))
print(type(9.81))
print(type(1 + 2j))

# Strings
# As short as a single character or as long as many pages

letter = 'a'
word = 'love'

print(letter)
print(len(letter))
print(word)
print(len(word))
print(word[0])
print(word[1])
last_index = len(word) - 1
print(word[3])
print(word[last_index])


sentence = 'I love Python'

print(sentence)
print(sentence.upper())
print(sentence.lower())
# print(sentence.count())
""" 
dna = '''gtggcgctgcagagtagaactccgttgttagaccagtaatatctgggggcggaagatggc
ctcggagcgaggctgaaggaactcagtatctaaaagttaattgatgagcatttctaccgg
ggagcgccgtagatggcagtgagccgtttaaagctcatcatctcagcaccgcgaagagtc
ctctgtgggggtccgggcacaccccgagtagtatcctgcacccaacacaggcatcccgtc
gagtatagtataaagaaggtctgcggttatttggtcctgttttctctttacgatacaacg
tataaaccgcgggcttgcagaagccatctcaatttaccttaccttcttcggtatattctt
tataggctggtcaacaacaatcaacattgggggtcgcgaaattcgtgacgccttaggccc
ttgcgtacaggacgttgttcttaccataattacaggctgacttgtgcgaaaagtccgatt
tgccacatgacactcctaccgagcagcttgcgttaggacagttcgcaaattccctaacaa
aggtagcgtttcggaagatacccaaagcggcgcaggtcttcccgaagcaaagtgtggccg
tgtggtgtacatggccacatgggaacagtcgagacgacgtctctcataagtagacggata
tgctatacttgcggcaggcaccagggttctattccggtatctttccgtgggggtgcattc
cgtccataggcctcgtcgccggggattaacggcggcttcgcccaccgttccattaagtgc
gcctatcggcatagaaggtcgtttcctagaaccgggtgctccctagttttacggactcca
tggatttgtatgggccacttgctattcgcgtaagggatcacatatggtttagagacccac
cggtgcaccaaaactcggccttcaagagcctgacaatttacatggctcacccttgtgacg
gtctagccgtagggctgaataacctcttttgcctaaacac'''

print(dna)
print(len(dna))

total_count = len(dna)
a = dna.count('a')
c = dna.count('c')
t = dna.count('t')
g = dna.count('g')
print(a, c,t, g)
print('proporation', 'a nucotide:',  round(a / total_count * 100, 2), '%')
print('proporation','c nucotide:',round(c / total_count * 100, 2), '%')
print('proporation', 't nucotide:', round(t/total_count * 100, 2), '%')
print('proporation',  'g nucotide:', round(g/total_count * 100, 2), '%')