import sys

if len(sys.argv) < 2:
    print("Usage: python dna_sequencing.py <dna_sequence>")
    sys.exit(1)

dna_sequence = sys.argv[1]
print(f"DNA Sequence: {dna_sequence}")
dna_List = dna_sequence.split("X")
print(dna_List)
valid_dna = [p for p in dna_List if p and set(p).issubset(set('ACGT'))]
print(f"Valid DNA: {valid_dna}")
valid_dna.sort(key=len, reverse=True)
print(f"Sorted Valid DNA: {valid_dna}")
if len(valid_dna) == 0:
    print("No valid DNA sequences found.")