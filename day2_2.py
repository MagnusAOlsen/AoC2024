         
def read_file() -> int:
    with open('input_files/day2.txt', 'r') as f:
        data = f.readlines()
        reports = []
        for element in data:
            element = element.strip()
            reports.append(element.split(' '))

    return check(reports)


        
            

def check(reports) -> int:
    safe = 0
    for element in reports:
        if int(element[0]) > int(element[1]):
            increasing = False
        else:
            increasing = True


        if increasing:
            new_safe = check_increasing(element)
            safe += new_safe
            new_safe2 = check_decreasing(element)
            safe += new_safe2
            

        elif not increasing:
            new_safe = check_decreasing(element)
            safe += new_safe
            new_safe2 = check_increasing(element)
            safe += new_safe2

    return safe
    

def check_increasing(element) -> int:
    correct = 0
    for i in range(len(element) - 1):
        if int(element[i + 1]) > int(element[i]) and int(element[i + 1]) < int(element[i]) + 4:
            correct += 1
    
    if correct == len(element) - 1:
        return 1

    else:  
        for i in range(len(element)):
            new_correct = 0
            new_element = element
            my_element = new_element[i]
            new_element.pop(i)
            for j in range(len(new_element) - 1):
                if int(new_element[j + 1]) > int(new_element[j]) and int(new_element[j + 1]) < int(new_element[j]) + 4:
                    new_correct += 1
            
            if new_correct == len(new_element) - 1:
                return 1
            new_element.insert(i, my_element)
        return 0

            

def check_decreasing(element) -> int:
    correct = 0
    for i in range(len(element) - 1):
        if int(element[i + 1]) < int(element[i]) and int(element[i + 1]) > int(element[i]) - 4:
            correct += 1
    
    if correct == len(element) - 1:
        return 1

    else:
        for i in range(len(element)):
            new_correct = 0
            new_element = element
            my_element = new_element[i]
            new_element.pop(i)
            for j in range(len(new_element) - 1):
                if int(new_element[j + 1]) < int(new_element[j]) and int(new_element[j + 1]) > int(new_element[j]) - 4:
                    new_correct += 1
            
            if new_correct == len(new_element) - 1:
                return 1
            new_element.insert(i, my_element)
        return 0


print(read_file())