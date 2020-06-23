def to_rna(dna_strand):
    transcription = dna_strand.maketrans('GCTA', 'CGAU')
    return dna_strand.translate(transcription)