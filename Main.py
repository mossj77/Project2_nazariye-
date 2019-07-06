from Convert_CGF import *
from Test_string import *


#C:\git\Nazaryeh github\Project2_nazariye-\input_NPDA.txt


def main():
    file = input("Please enter the NPDA's File Address:\n")
    file = open(file, 'r')

    decision = input("Enter ( 1 :to converting NPDA to CFG) or ( 2 :to test input string): \n")
    if decision == '1':
        List = input_string(file)
        convertedCFG = convertToCFG(List)
        for i in range(4*int(List[0])):
            print(convertedCFG[0] +
                  " -> " + convertedCFG [1] +
                  convertedCFG[2] +
                  " | " +
                  convertedCFG[1] +
                  convertedCFG[3])
            for j in range(2*int(List[0])):
                del convertedCFG[0]

        for i in range(len(convertedCFG)):
            print(convertedCFG[i])
    elif decision == '2':
        List = input_CFG(file)
        main_process(List)

def input_CFG(File):
    input_list = []
    for line in File:
        line = line.split("\n")
        input_list.append(line)

    for i in range(len(input_list)):
        if input_list[i][-1] == '':
            del input_list[i][-1]
    return input_list


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


if __name__ == "__main__":
    main()