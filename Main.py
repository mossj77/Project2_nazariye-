from Convert_CGF import *

def input_string(File):
    input_list = []
    for line in File:
        line = line.split("\n")
        input_list.append(line)

    for i in range(len(input_list)):
        if input_list[i][-1] == '':
            del input_list[i][-1]

    List = []
    for i in range(len(input_list)):
        List.append(input_list[i][0])

    List = [s.replace('->', '') for s in List]
    List = [s.replace('*', '') for s in List]
    List = [s.replace('_', '') for s in List]

    return List

#C:\git\Nazaryeh github\Project2_nazariye-\input_NPDA.txt


def main():
    file = input("Please enter the NPDA's File Address:\n")
    file = open(file, 'r')
    List = input_string(file)
    convertedCFG = convertToCFG(List)
    for i in range(4*int(List[0])):
        print(convertedCFG[0] + " -> " + convertedCFG [1] + convertedCFG[2] + " | " + convertedCFG[1] + convertedCFG[3])
        for j in range(2*int(List[0])):
            del convertedCFG[0]

    for i in range(len(convertedCFG)):
        print(convertedCFG[i])



if __name__ == "__main__":
    main()