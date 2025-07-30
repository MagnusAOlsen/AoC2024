# with open('input_files/day3.txt', 'r') as f:
#     data = f.readlines()
#     total = 0
#     for line in data:
#         check = 0
#         while True:
#             check = line.find('mul', check)
#             if check == -1:
#                 break
#             done = line.find(')', check)
#             if done == -1: 
#                 break
#             numbers = line[check + 4:done].split(',')
#             if ''.join(numbers).isnumeric():
#                 total += int(numbers[0]) * int(numbers[1])
#             check += 1
#     print(total)

def find_instances():

    with open('input_files/day3.txt', 'r') as f:
        data = f.readlines()
        total = 0
        round = 0
        for line in data:
    
            index = 0
            while True:
                if round != 0:
                    index = line.find('do()', index)
                    if index == -1:
                        break

                substring = line[index:]

                dont_index = line.find("don't()", index)

                if dont_index != -1:
                    substring = substring[:dont_index]

                check = 0
                while True:
                    check = substring.find('mul', check)
                    if check == -1:
                        break
                    done = substring.find(')', check)
                    if done == -1: 
                        break
                    numbers = substring[check + 4:done].split(',')
                    if ''.join(numbers).isnumeric():
                        total += int(numbers[0]) * int(numbers[1])
                    check += 1
                

                index = dont_index
                print(index)
                round += 1
                
    return total


print(find_instances())


        
