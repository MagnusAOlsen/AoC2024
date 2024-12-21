def calculate_distance() -> int:
    with open("input_files/input.txt") as f:
        left_list = []
        right_list = []
        data = f.readlines()

        for element in data:
            element = element.strip()
            new_el = element.split("   ")
            left_list.append(int(new_el[0]))
            right_list.append(int(new_el[1]))
            
    
    total = 0
    left_list.sort()
    right_list.sort()
    
    print(left_list)
    print(right_list)

    for i in range(0, len(left_list)):
        total += abs(left_list[i] - right_list[i])
        
        
    print(right_list, left_list)
    return right_list, left_list


def similarity(right_list, left_list):

    similarity_score = 0

    for i in range(len(left_list)):
        total = 0
        for j in range(len(right_list)):
            if left_list[i] == right_list[j]:
                total += 1
            
        similarity_score += left_list[i] * total

    return similarity_score




right_list, left_list = calculate_distance()

print(similarity(right_list, left_list))





        