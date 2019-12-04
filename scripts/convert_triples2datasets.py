import sys

def parse_args():
    if sys.argv[1] == "":
        return "output/tokenize_triples.txt"
    else:
        return sys.argv[1]

def count_file_lines(read_file):
    count = 0
    file = open(read_file, "r")
    for line in file:
        count += 1
    file.close()
    return count

def create_datasets(num_of_lines, source_file, datasets_files):
    line_to_split = num_of_lines // 3
    read_file = open(source_file, "r")
    for dataset in datasets_files:
        write_file = open(dataset, "w")
        for i in range(line_to_split):
            write_file.write(read_file.readline())
        write_file.close()
    read_file.close()


source_file = parse_args()
training_file = "output/training_dataset.txt"
validation_file = "output/validation_dataset.txt"
test_file = "output/test_dataset.txt"
datasets_files = [training_file, validation_file, test_file]

num_of_lines = count_file_lines(source_file)
create_datasets(num_of_lines, source_file, datasets_files)
