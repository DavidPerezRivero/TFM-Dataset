import sys
from spacy_script import *
from babi_to_triples import *


read_file = sys.argv[1]
babi2triples_file = "output/triples_from_babi.txt"
tokenize_file = "output/tokenize_triples.txt"

babi_to_triples = Babi2Triples(read_file, babi2triples_file)
babi_to_triples.run()

tokenize = TokenizeDataset(babi2triples_file, tokenize_file)
tokenize.run()
