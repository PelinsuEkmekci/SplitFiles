splitlength = 20 #20 lines per fasta files
output = 'output'

input = "/Users/pelinsuekmekci/PycharmProjects/csv2fasta/"

def F2():

    inputdata = open("input", 'r').read().split('\n')  # read and split files
    at = 1
    for lines in range(0, len(inputdata), splitlength):  # create loop start from 0 to splitlength

        outputdata = inputdata[lines:lines+splitlength]
        outputfunction = open(output + str(at) + '.fasta', 'w')  # create new file with desired features
        outputfunction.write('\n'.join(outputdata))
        outputfunction.close()

        at += 1

if __name__ == "__main__":
        F2()