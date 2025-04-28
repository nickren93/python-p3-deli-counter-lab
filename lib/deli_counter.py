
katz_deli = []

def line(list):
    #pass
    if len(list) == 0:
        print("The line is currently empty.")
    else:
        print("The line is currently:", end=' ')
        for index, person in enumerate(list):
            if index == len(list) - 1:
                print(f"{index + 1}. {person}", end='\n')
            else:
                print(f"{index + 1}. {person}", end=' ')


def take_a_number(list, new_person):
    #pass
    list.append(new_person)
    print(f"Welcome, {new_person}. You are number {len(list)} in line.")

def now_serving(list):
    #pass
    if len(list) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {list[0]}.")
        list.pop(0)