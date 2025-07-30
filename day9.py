class day9():

    def __init__(self, name, file) -> None:
        self.name = name
        self.file = file

    def main(self):
        data_list = self.readfile()
        first_string = self.add_dot(data_list)
        modified_string = self.modify(first_string)
        summen = self.compute(modified_string)
        return summen

    
    def readfile(self) -> list:
        with open(self.file, 'r') as f:
            data = f.read()
            data_list = data.split()
            return data_list
        
    def add_dot(self, content_list) -> str:
        first_string = ''
        for i in range(len(content_list)):
            if i % 2 != 0:
                first_string += content_list[i]
            else:
                first_string += ('.' * int(content_list[i]))
        return first_string
    
    def modify(self, first_string) -> str:
        index = len(first_string)
        for character in first_string:
            if character == '.':
                for element in first_string[:index:-1]:
                    if element != '.':
                        character = element
                        index = first_string.reverse().index(element)
                        element = '.'
        return first_string
    
    def compute(self, done_string) -> int:
        summen = 0
        for i in range(len(done_string)):
            summen += int(done_string[i]) * i
        return summen


test = day9('test1', 'input_files/day9.txt')
print(test.main())

    





            

