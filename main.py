from pawpal_system import Owner, Pet, Task, Scheduler


# Create tasks out of order
walk = Task(
    description="Morning Walk",
    time="09:00",
    frequency="Daily",
    priority=1
)

feeding = Task(
    description="Breakfast",
    time="07:00",
    frequency="Daily",
    priority=2
)

medicine = Task(
    description="Give Medicine",
    time="08:00",
    frequency="Daily",
    priority=1
)

grooming = Task(
    description="Grooming",
    time="08:00",
    frequency="Weekly",
    priority=3
)


# Create pet
dog = Pet(
    name="Biscuit",
    species="Dog",
    breed="Golden Retriever",
    age=3
)


# Add tasks to pet
dog.add_task(walk)
dog.add_task(feeding)
dog.add_task(medicine)
dog.add_task(grooming)


# Create owner
owner = Owner(
    name="Alex",
    available_time=120
)

owner.add_pet(dog)


# Create scheduler
scheduler = Scheduler(owner)


# -------------------------------
# Test Sorting
# -------------------------------

print("\n--- Sorted Tasks By Time ---")

sorted_tasks = scheduler.sort_by_time(
    owner.get_all_tasks()
)

for task in sorted_tasks:
    print(
        task.time,
        "-",
        task.description
    )


# -------------------------------
# Test Filtering
# -------------------------------

print("\n--- Filtering Completed Tasks ---")

feeding.completed = True

active_tasks = scheduler.filter_completed_tasks(
    owner.get_all_tasks()
)

for task in active_tasks:
    print(
        task.description
    )


# -------------------------------
# Test Recurring Tasks
# -------------------------------

print("\n--- Recurring Task Test ---")

new_task = walk.mark_complete()

if new_task:
    print(
        "New recurring task:",
        new_task.description,
        new_task.frequency
    )


# -------------------------------
# Test Conflict Detection
# -------------------------------

print("\n--- Conflict Detection ---")

conflicts = scheduler.detect_conflicts(
    owner.get_all_tasks()
)

for conflict in conflicts:
    print(conflict)


# -------------------------------
# Test Schedule Generation
# -------------------------------

print("\n--- Generated Schedule ---")

schedule = scheduler.generate_schedule()

for task in schedule:
    print(
        task.time,
        "-",
        task.description
    )