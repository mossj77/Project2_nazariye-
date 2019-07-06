def convertToCFG(List):
    number = int(List[0])
    transition = []
    other_transitions = []
    for i in range(4,len(List)):
        local_var = List[i].split(",")
        if local_var[3] != "" :
            transition.append(List[i])
        else:
            other_transitions.append(List[i])

    List_of_CFG = []
    for l in range(number):
        if l == 0:
            for i in range(len(transition)):
                local_var = transition[i].split(",")
                local_str = ""
                local_str = local_str + str(local_var[0])
                local_str = local_str + str(local_var[2])
                local_str = local_str + str(local_var[4])
                List_of_CFG.append(local_str)
                for j in range(number-1):
                    local_str = ""
                    local_str = local_str.join(local_var[1])
                    List_of_CFG.append(local_str)
                    for m in range(0,number):

                        local_str = ""
                        if len(local_var[3])>1:
                            local_str = local_str.join(str("("+
                                                           local_var[0]+
                                                           str(local_var[3][0])+
                                                           "q"+str(m)+")"+
                                                           "("+"q"+str(m)+
                                                           str(local_var[3][1])+
                                                           local_var[4]+")"))
                        else:
                            local_str = local_str.join(str("(" +
                                                           local_var[0] +
                                                           str(local_var[3][0]) +
                                                           "q" + str(m) + ")"))
                        List_of_CFG.append(local_str)
        else:
            for i in range(len(transition)):
                local_var = transition[i].split(",")
                local_str = ""
                local_str = local_str + str(local_var[0])
                local_str = local_str + str(local_var[2])
                local_str = local_str + "qf"
                List_of_CFG.append(local_str)
                for j in range(number - 1):
                    local_str = ""
                    local_str = local_str.join(local_var[1])
                    List_of_CFG.append(local_str)
                    for m in range(0, number):
                        local_str = ""
                        if (len(local_var[3]) > 1):
                            local_str = local_str.join(str(
                                "(" + local_var[0] + str(local_var[3][0]) + "q" + str(m) + ")" + "(" + "q" + str(m) + str(
                                    local_var[3][1]) + "qf" + ")"))
                        else:
                            local_str = local_str.join(str(
                                "(" + local_var[0] + str(local_var[3][0]) + "q" + str(m) + ")"))

                        List_of_CFG.append(local_str)


    others = other_transition(other_transitions)
    for i in range(len(others)):

        List_of_CFG.append(others[i])
    return List_of_CFG

def other_transition(lst):
    CFG = []
    for i in range(len(lst)):
        string = ""
        Var = lst[i].split(",")
        string = string + str(Var[0])
        string = string + str(Var[2])
        string = string + str(Var[4])
        string = string + " -> "
        if Var[1] != "":
            string = string + str(Var[1])
        else:
            string = string + "_"
        CFG.append(string)
    return CFG
