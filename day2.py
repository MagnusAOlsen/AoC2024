
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
            correct = 0
            for i in range(len(element) - 1):
                if int(element[i + 1]) > int(element[i]) and int(element[i + 1]) < int(element[i]) + 4:
                    correct += 1
            
            if correct == len(element) - 1:
                safe += 1
            

        elif not increasing:
            correct = 0
            for i in range(len(element) - 1):
                if int(element[i + 1]) < int(element[i]) and int(element[i + 1]) > int(element[i]) - 4:
                    correct += 1
            
            if correct == len(element) - 1:
                safe += 1
    return safe
    

print(read_file())








    