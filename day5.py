with open('input_files/day5.txt', 'r') as f:
    data = f.readlines()
    instructions = [x.strip() for x in data if '|' not in x and x != '']
    rule_list = [x.strip() for x in data if '|' in x]
    correct = []
    not_correct = []

    for instruction in instructions:
        counter = 0
        for rule in rule_list:
            if instruction.find(rule[:2]) <= instruction.find(rule[3:]) or (instruction.find(rule[3:]) == -1):
                counter += 1

        if counter == len(rule_list): 
            correct.append(instruction.split(','))

    result_list = []
    for i in range(1,len(correct)):
        print(len(correct[i]))
        result_list.append(int(correct[i][(len(correct[i]) - 1) // 2]))

    print(sum(result_list))



