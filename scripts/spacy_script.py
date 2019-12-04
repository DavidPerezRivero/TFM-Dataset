import spacy
import sys

class TokenizeDataset:
    def __init__(self, read_file, write_file):
        self.read_file = read_file
        self.write_file = write_file

    def run(self):
        nlp = spacy.load("en_core_web_sm")
        rf = open(self.read_file, "r")
        wf = open(self.write_file, "w")

        for line in rf:
            doc = nlp(line)
            for ent in doc.ents:
                line = line.replace(ent.text, '<' + ent.label_ + '>')
            wf.write(line)

        rf.close()
        wf.close()
        print("Triples Tokenize File:  " + self.write_file)
