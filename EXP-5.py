print("UIN : 251A028")

tasks = []

# Adding tasks
tasks.append("Study Python")
tasks.append("Complete Assignment")
tasks.append("Practice Programs")

print("Tasks:", tasks)

# Removing a task
tasks.remove("Practice Programs")
print("After Removal:", tasks)

# Updating a task
tasks[1] = "Complete Python Lab"
print("After Update:", tasks)

# Sorting tasks
tasks.sort()
print("Sorted Tasks:", tasks)

# Converting list to tuple
task_tuple = tuple(tasks)
print("Tasks in Tuple:", task_tuple)