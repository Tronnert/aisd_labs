def parse_file(filename: str):
    file = list(map(lambda x: x.strip().split(","), 
                    open(filename, encoding="UTF-8").readlines()))
    questions = file[0][1:]
    students = [(line[0], [1 if ans == "да" else 0 for ans in line[1:]]) for line in file[1:]]
    return questions, students


def simple_binary_tree(students: list):
    if len(students) == 0:
        return ("Таких людей нет",)
    if len(students) == 1:
        return (students[0][0],)
    else:
        return (simple_binary_tree([(student[0], student[1][1:]) for student in students if student[1][0]]), 
                simple_binary_tree([(student[0], student[1][1:]) for student in students if not student[1][0]]))


if __name__ == "__main__":
    questions, students = parse_file("lab1\students.csv")
    binary_tree = simple_binary_tree(students)
    for e in range(len(questions)):
        if input(questions[e] + " ") == "да":
            binary_tree = binary_tree[0]
        else:
            binary_tree = binary_tree[1]
        if len(binary_tree) == 1:
            print(binary_tree[0])
            break