# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def readFile(fname):
    with open(fname) as file:
        lines = [line.rstrip() for line in file]
    # Use a breakpoint in the code line below to debug your script.
    sequence = dict()
    x = 0
    currSequence = ''
    for l in lines:
        print(l)  # Press
        if len(l)> 0:
            if l[0] == '>' :
                sequence[l] = ""
                currSequence = l
                continue
            sequence[currSequence] = sequence[currSequence] + l
    outfile = 'D:/Nemalogic_Git_Hub/nemalogic/R-Phylogenetic-analyses/Plectida/sequence.fasta'
    cnt=0
    with open(outfile, 'w') as f:
        for key in sequence:
            cnt = cnt +1
            f.write(key + '\n')
            f.write(sequence[key]+'\n')
            if cnt>10:
                break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fname = 'D:/Nemalogic_Git_Hub/nemalogic/R-Phylogenetic-analyses/Plectida/sequence.fasta.org'
    readFile(fname)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
