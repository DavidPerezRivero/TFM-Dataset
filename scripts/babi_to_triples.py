import sys

class Babi2Triples:
    def __init__(self, read_file, write_file):
        self.read_file = read_file
        self.write_file = write_file

    def split_line_function(self, line):
        split_line = line.split("\t")
        utterance_1 = split_line[0][2:]
        utterance_2 = split_line[1]
        return utterance_1, utterance_2

    def run(self):
        rf = open(self.read_file, "r")
        wf = open(self.write_file, "w")
        line_to_write = ""
        count = 0
        stop = False
        lines = rf.read().split("\n")

        for i, line in enumerate(lines):
            if line == "":
                count = count
            elif lines[i+1].find("api_call") > 0:
                u1, u2 = self.split_line_function(line)
                if u1.find("<SILENCE>") >= 0:
                    pre_u1, pre_u2 = self.split_line_function(lines[i-1])
                    pre2_u1, pre2_u2 = self.split_line_function(lines[i-2])
                    line_to_write = pre2_u2 + "\t" + pre_u1 + "\t" + pre_u2 + ", " + u2
                elif count == 1:
                    line_to_write += "\t" + u1 + "\t" + u2
                else:
                    pre_u1, pre_u2 = self.split_line_function(lines[i-1])
                    if count == 2:
                        line_to_write += "\t" + u1
                        wf.write(line_to_write + "\n")
                    line_to_write = pre_u2 + "\t" + u1 + "\t" + u2
                wf.write(line_to_write + "\n")
                line_to_write = ""
                count = 0
            else:
                u1, u2 = self.split_line_function(line)
                if u1.find("<SILENCE>") >= 0:
                    line_to_write += ", " + u2
                else:
                    if count == 2:
                        line_to_write += "\t" + u1
                        wf.write(line_to_write + "\n")
                        line_to_write = u2
                        count = 1
                    elif count == 1:
                        line_to_write += "\t" + u1 + "\t" + u2
                        wf.write(line_to_write + "\n")
                        line_to_write = ""
                        count = 0
                    else:
                        line_to_write = u1 + "\t" + u2
                        count = 2
        rf.close()
        wf.close()
        print("Babi to Triples File:  " + self.write_file)
