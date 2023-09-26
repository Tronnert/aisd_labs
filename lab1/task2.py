def parse_file(filename: str):
    file = [line.strip().split(',')
            for line
            in open(filename, encoding="UTF-8").readlines()]
    questions = file[0][1:]
    students = [(line[0], [ans == 'да' for ans in line[1:]])
                for line
                in file[1:]]
    return questions, students

def create_btree(students: list):
    if len(students) == 0:
        return None
    if len(students) == 1:
        return students[0][0]
    else:
        left = []
        right = []
        for student in students:
            if student[1].pop(0):
                left.append(student)
            else:
                right.append(student)
        return (create_btree(left), create_btree(right))


def ask(question):
    user_answer = input(question + ": ")
    if user_answer in ('да', 'Да', 'д', 'Д'):
        return True
    if user_answer in ('нет', 'Нет', 'н', 'Н'):
        return False
    return ask(question) # wrong answer, ask again


def print_btree(btree, layer=0):
    if btree is None:
        print('--' * layer + 'None')
        return
    if type(btree) == str:
        print('--' * layer + btree)
        return
    print('--' * layer + 'True: ')
    print_btree(btree[0], layer=layer+1)
    print('--' * layer + 'False: ')
    print_btree(btree[1], layer=layer+1)


if __name__ == "__main__":
    questions, students = parse_file("lab1/students.csv")
    btree = create_btree(students)
    for question in questions:
        # print_btree(btree)
        btree = btree[0 if ask(question) else 1]

        if btree is None:
            print('Нет такого человека')
            break

        if type(btree) == str:
            print(btree)
            break
