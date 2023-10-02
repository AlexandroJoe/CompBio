userInputDNA = str(input("Input DNA = "))
DNAinput = userInputDNA.upper()
# print(DNAinput)
# for i in DNAinput:
#     print(i)

complement = ""
mRNA = ""
acid = ""

def TransalationComplement(DNAinput):
    complement = ""
    for i in DNAinput:
        if i == "T":
            complement += "A"
        elif i == "A":
            complement += "T"
        elif i == "C":
            complement += "G"
        elif i == "G":
            complement += "C"
        
        # print("test complement" + complement)
    return complement

# print("test complement" + complement)

def TransalationmRNA(DNAinput):
    mRNA = ""
    for i in DNAinput:
        if i == "T":
            mRNA += "A"
        elif i == "A":
            mRNA += "U"
        elif i == "C":
            mRNA += "G"
        elif i == "G":
            mRNA += "C"
        
    return mRNA

def translate_codon(cod):
    tc = {"GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
           "TGT":"C", "TGC":"C", "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
            "TTT":"F", "TTC":"F", "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G",
            "CAT":"H", "CAC":"H", "ATA":"I", "ATT":"I", "ATC":"I", "AAA":"K",
            "AAG":"K", "TTA":"L", "TTG":"L", "CTT":"L", "CTC":"L", "CTA":"L", 
            "CTG":"L", "ATG":"M", "AAT":"N", "AAC":"N", "CCT":"P", "CCC":"P", 
            "CCA":"P", "CCG":"P", "CAA":"Q", "CAG":"Q", "CGT":"R", "CGC":"R", 
            "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R", "TCT":"S", "TCC":"S",
            "TCA":"S", "TCG":"S", "AGT":"S", "AGC":"S ","ACT":"T", "ACC":"T", 
            "ACA":"T", "ACG":"T", "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V", 
            "TGG":"W", "TAT":"Y", "TAC":"Y", "TAA":"_","TAG":"_","TGA":"_"
    }
    if cod in tc:
        return tc[cod]
    else:
        return None
    
def AminoAcid (complement):
    acid = ""

    if len(complement) % 3 == 0:
        for i in range(0, len(complement),3):
            codon = complement[i:i + 3]
            acid += translate_codon(codon) + " - "
    
    return acid

# complement = TransalationComplement(DNAinput,complement)
# mRNA = TransalationmRNA(DNAinput,mRNA)
# acid = AminoAcid(complement)

def main(complement,mRNA,acid):
    complement = TransalationComplement(DNAinput)
    mRNA = TransalationmRNA(DNAinput)
    acid = AminoAcid(complement)
    
    print("Complement = " + complement)
    print("mRNA =  " + mRNA)
    print("Aminoacid = " + acid[:-2])

main(complement,mRNA,acid)