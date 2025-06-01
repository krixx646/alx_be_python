#Priotize task

Task = input("Enter the task: ")
Priority_level = input("Enter the priority level (high/medium/low): ").lower().strip()
time_bound = input("Enter the time bound (yes/no): ").lower().strip()

match Priority_level:
    case "high":
        level = f"Don't forget this {Task} is important"
    case "medium":
        level = f"{Task} is important, but not urgent"
    case "low":
        level = f"{Task} is not so important"
    case _:
        level = f"seems you made a mistake here"

if time_bound == "yes":
    urgency = f"execute this task immediately"
elif time_bound == "no":
    urgency = f"take your time with the task"
else:
    urgency = f"Do what ever you want"

print(f"{Task} is a {Priority_level} that you need to {urgency}")