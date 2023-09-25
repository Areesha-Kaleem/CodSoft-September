'''Name: Areesha Kaleem
codsoft internship Sep Batch A3'''



from art import *
def create():
    global tdl, to_do_dic
    no_of_works = int(input("Enter the no of tasks you have per day: "))
    for i in range(no_of_works):
        time = input("Enter the time(like hh:mm): ")
        work = input("Enter the work: ")
        tw = time +": "+ work
        tdl.append(tw)
    to_do_dic[day] = tdl
def update():
    nwork = input("Enter the update: ")
    ntw = time2 + ": " + nwork
    to_do_dic[day2][j] = ntw
    print("Updated")

tprint("TO DO LIST", font="fancymedium")
to_do_dic = {"Monday": None, "Tuesday": None, "Wednesday": None, "Thursday": None, "Friday": None, "Saturday": None, "Sunday": None}
tdl = []
day = input("Enter the day (initial capital and full spellings please): ")
if day in to_do_dic:
    create()
else:
    print("Enter full spelling #invalid_input")
    create()
while True:
    options = input("What you wanna do\n 1. Update it\n 2. Track your tasks\n 3. Exist\nEnter the option number here: ")
    if options == "1":
        day2 = input("Enter the day (initial capital and full spellings please): ")
        time2 = input("Enter the time (like hh:mm): ")
        if day2 in to_do_dic:
            for j in range(len(to_do_dic[day2])):
                if time2 in to_do_dic[day2][j]:
                   update()
    elif options == "2":
        day2 = input("Enter the day (initial capital and full spellings please): ")
        time2 = input("Enter the time (like hh:mm): ")
        if day2 in to_do_dic:
            for j in range(len(to_do_dic[day2])):
                if time2 in to_do_dic[day2][j]:
                    print(f"On {day2} at {to_do_dic[day2][j]}")
    elif options == "3":
        quit()
    else:
        print("#invalid input")

