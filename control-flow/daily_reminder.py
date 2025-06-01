# daily_reminder.py

# Prompt for a single task (exact text)
task = input("Enter your task: ")
# Prompt for the task’s priority (exact text)
priority = input("Priority (high/medium/low): ").lower().strip()
# Prompt for time sensitivity (exact text)
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

# Match‐case on priority to set a descriptive prefix
match priority:
    case "high":
        prefix = "high priority task"
    case "medium":
        prefix = "medium priority task"
    case "low":
        prefix = "low priority task"
    case _:
        print("Invalid priority level.")
        exit()

# Based on time_bound, choose between a “Reminder:” or a “Note:”
if time_bound == "yes":
    print(f"Reminder: '{task}' is a {prefix} that requires immediate attention today!")
else:
    print(f"Note: '{task}' is a {prefix}. Consider completing it when you have free time.")
