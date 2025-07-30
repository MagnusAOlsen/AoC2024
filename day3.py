with open('input_files/day3.txt', 'r') as f:
    data = f.readlines()
    total = 0
    for line in data:
        check = 0
        while True:
            check = line.find('mul', check)
            if check == -1:
                break
            done = line.find(')', check)
            if done == -1: 
                break
            numbers = line[check + 4:done].split(',')
            if ''.join(numbers).isnumeric():
                total += int(numbers[0]) * int(numbers[1])
            check += 1
    print(total)







