from pawpal_system import Task, Pet, Owner, Scheduler


# Create tasks
dog_walk = Task(
    description="Morning walk",
    time="8:00 AM",
    frequency="Daily",
    priority=1
)

dog_food = Task(
    description="Feed Max",
    time="9:00 AM",
    frequency="Daily",
    priority=2
)

cat_grooming = Task(
    description="Brush Luna",
    time="5:00 PM",
    frequency="Weekly",
    priority=3
)


# Create pets
dog = Pet(
    name="Max",
    species="Dog",
    breed="Golden Retriever",
    age=4
)

cat = Pet(
    name="Luna",
    species="Cat",
    breed="Siamese",
    age=2
)


# Add tasks to pets
dog.add_task(dog_walk)
dog.add_task(dog_food)

cat.add_task(cat_grooming)


# Create owner
owner = Owner(
    name="Wesley",
    available_time=120
)

owner.add_pet(dog)
owner.add_pet(cat)


# Create scheduler
scheduler = Scheduler(owner)

schedule = scheduler.generate_schedule()


# Print schedule
print("Today's Schedule")
print("----------------")

for task in schedule:
    print(
        f"{task.time} - {task.description} "
        f"(Priority: {task.priority})"
    )