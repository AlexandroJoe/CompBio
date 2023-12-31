aminoAcid = "NAN"
dnaSequence = "AAUGCUAAU"


def translate_codon(cod):
    tc = {
        "TTT": "Phe - (F)", "TTC": "Phe - (F)", "TTA": "Leu - (L)", "TTG": "Leu - (L)",
        "TCT": "Ser - (S)", "TCC": "Ser - (S)", "TCA": "Ser - (S)", "TCG": "Ser - (S)",
        "TAT": "Tyr - (Y)", "TAC": "Tyr - (Y)", "TAA": "_", "TAG": "_",
        "TGT": "Cys - (C)", "TGC": "Cys - (C)", "TGA": "_", "TGG": "Trp - (W)",

        "CTT": "Leu - (L)", "CTC": "Leu - (L)", "CTA": "Leu - (L)", "CTG": "Leu - (L)",
        "CCT": "Pro - (P)", "CCC": "Pro - (P)", "CCA": "Pro - (P)", "CCG": "Pro - (P)",
        "CAT": "His - (H)", "CAC": "His - (H)", "CAA": "Gln - (Q)", "CAG": "Gln - (Q)",
        "CGT": "Arg - (R)", "CGC": "Arg - (R)", "CGA": "Arg - (R)", "CGG": "Arg - (R)",

        "ATT": "Ile - (I)", "ATC": "Ile - (I)", "ATA": "Ile - (I)", "ATG": "Met - (M)",
        "ACT": "Thr - (T)", "ACC": "Thr - (T)", "ACA": "Thr - (T)", "ACG": "Thr - (T)",
        "AAT": "Asn - (N)", "AAC": "Asn - (N)", "AAA": "Lys - (K)", "AAG": "Lys - (K)",
        "AGT": "Ser - (S)", "AGC": "Ser - (S)", "AGA": "Arg - (R)", "AGG": "Arg - (R)",

        "GTT": "Val - (V)", "GTC": "Val - (V)", "GTA": "Val - (V)", "GTG": "Val - (V)",
        "GCT": "Ala - (A)", "GCC": "Ala - (A)", "GCA": "Ala - (A)", "GCG": "Ala - (A)",
        "GAT": "Asp - (D)", "GAC": "Asp - (D)", "GAA": "Glu - (E)", "GAG": "Glu - (E)",
        "GGT": "Gly - (G)", "GGC": "Gly - (G)", "GGA": "Gly - (G)", "GGG": "Gly - (G)",
    }

    if cod in tc:
        return tc[cod]
    else:
        return None

def find_codon_frequency(dnaSequence, aminoAcid):
    codon_count = {}
    dnaSequence = dnaSequence.upper()  

    for i in range(0, len(dnaSequence) - 2, 3):
        codon = dnaSequence[i:i+3]
        amino_acid_translation = translate_codon(codon)
        if amino_acid_translation == aminoAcid:
            if codon in codon_count:
                codon_count[codon] += 1
            else:
                codon_count[codon] = 1

    return codon_count

frequency = find_codon_frequency(dnaSequence, aminoAcid)

for codon, frequency in frequency.items():
    print(f"{codon}: {frequency}")
