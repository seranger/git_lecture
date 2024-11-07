#Pizza Party Planner
def pizzaria():
    people=int(input("How many guests are attending?:"))
    pizza=int(input("How many slices of pizza would each person like to eat?:"))
    total_slices= pizza * people
    return print(f"You need {total_slices} slices of pizza for the {people} people attending your party.")
pizzaria()