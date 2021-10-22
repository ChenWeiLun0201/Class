# Tham khao tu bai The Anh

def input_text(text):
    return input(text)

def input_number(text, min, max):
    while True:
        try:
            grade = int(input(text))
            if min <= grade <= max:
                return grade
                break
            else:
                print("\nInvalid Value. Try again!!!\n")
        except ValueError:
            print("\nInvalid Value. Try again!!!\n")

def choose_gender():
    gender = input_number("""
+) Gender:
    Choose one of the followings:
    1. Male
    2. Female
    3. Fluid
    Your choice: """, 1, 3)

    if gender == 1:
        return "Male"
    elif gender == 2:
        return "Female"
    else:
        return "Fluid"

def add_information():
    individual = []
    questions = [
        "+) Full name: ",
        "+) Gender: ",
        "+) Address: ",
        "+) Theory: ",
        "+) Practice: "
    ]

    for i in range(len(questions)):
        if i == 1:
            individual.append(choose_gender())
        elif i <= 2:
            individual.append(input_text(questions[i]))
        else:
            individual.append(input_number(questions[i], 0, 100))

    return individual

if __name__ == '__main__':
    sis = []
    for i in range(2):
        sis.append(add_information())
    print(sis)

def remove_item(index, *array):
    temp_list = list(array).copy()
    temp_list.pop(index - 1)
    return temp_list

def choose_item(*array):
    while True:
        try:
            index = int(input("Enter S/N to delete: "))
            if 1 <= index <= len(array):
                return index
                break
            else:
                print("\nInvalid Value. Try Again!!!\n")
        except ValueError:
            print("\nInvalid Value. Try Again!!!\n")

if __name__ == '__main__':
    array = [
        ["Tran Duy Luan", "Male", "Vung Tau", 75, 75],
        ["Nguyen Duy Luan", "Male", "Vung Tau", 70, 80]
    ]
    item = choose_item(*array)
    array = remove_item(item, *array)
    print(array)


def choose_option():
    while True:
        try:
            option = int(input("""
            Choose one of the following options to execute program
            1. Display all list
            2. Add
            3. Delete
            4. Exit

            Your choice: """))
            if 1 <= option <= 4:
                return option
                break
            else:
                print("\nInvalid Input. Try again!!!\n")
        except ValueError:
            print("\nInvalid Input. Try again!!!\n")


def display_information(*list):
    info = "{:^5}|{:^20}|{:^10}|{:^20}|{:^10}|{:^10}"
    print(info.format("S/N", "FULL NAME", "GENDER", "CITY", "THEORY", "PRACTICE"))

    for i in range(len(list)):
        print(info.format(i + 1, list[i][0], list[i][1], list[i][2], list[i][3], list[i][4]))


def try_again(text):
    answer = input(text).upper().strip()
    if answer == "Y" or answer == "YES":
        return True
    else:
        return False


if __name__ == '__main__':
    sis = []
    while True:
        option = choose_option()
        if option == 1:
            if sis == []:
                print("\nYou have to add student information first!!!\n".upper())
            else:
                display_information(*sis)
        elif option == 2:
            choice = True
            while choice:
                sis.append(add_information())
                choice = try_again("\nYou you want to add more students? (Y/N): ")
        elif option == 3:
            if sis == []:
                print("\nNothing to delete. You have to add information first\n".upper())
            else:
                choice = True
                while choice:
                    item = choose_item(*sis)
                    sis = remove_item(item, *sis)
                    choice = try_again("\nYou you want to delete more? (Y/N): ")
        else:
            exit()