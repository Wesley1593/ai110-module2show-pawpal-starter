"""PawPal+ pet care app - logic layer.

Contains the core classes:
Task, Pet, Owner, and Scheduler.
"""

from dataclasses import dataclass, field


@dataclass
class Task:
    """Represents a single pet care activity."""

    description: str
    time: str
    frequency: str
    completed: bool = False
    priority: int = 1

    def mark_complete(self) -> None:
        """Mark task as completed."""
        self.completed = True

    def update_task(self, description=None, time=None, frequency=None, priority=None):
        """Update task information."""
        if description:
            self.description = description
        if time:
            self.time = time
        if frequency:
            self.frequency = frequency
        if priority:
            self.priority = priority


@dataclass
class Pet:
    """Stores pet information and their tasks."""

    name: str
    species: str
    breed: str
    age: int
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        self.tasks.append(task)

    def get_tasks(self) -> list[Task]:
        """Return all tasks for this pet."""
        return self.tasks


@dataclass
class Owner:
    """Stores owner information and manages pets."""

    name: str
    available_time: int
    preferences: dict = field(default_factory=dict)
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's list."""
        self.pets.append(pet)

    def get_all_tasks(self) -> list[Task]:
        """Collect tasks from all owned pets."""
        all_tasks = []

        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())

        return all_tasks


class Scheduler:
    """Creates and manages daily pet care schedules."""

    def __init__(self, owner: Owner):
        self.owner = owner
        self.daily_schedule = []

    def get_available_tasks(self) -> list[Task]:
        """Retrieve tasks from owner's pets."""
        return self.owner.get_all_tasks()

    def sort_tasks_by_priority(self, tasks: list[Task]) -> list[Task]:
        """Sort tasks by priority."""
        return sorted(tasks, key=lambda task: task.priority)

    def generate_schedule(self) -> list[Task]:
        """Create a schedule based on available time."""

        tasks = self.get_available_tasks()

        # Remove completed tasks
        tasks = [
            task for task in tasks
            if not task.completed
        ]

        # Sort tasks
        tasks = self.sort_tasks_by_priority(tasks)

        total_time = 0
        schedule = []

        for task in tasks:
            if total_time + 30 <= self.owner.available_time:
                schedule.append(task)
                total_time += 30

        self.daily_schedule = schedule

        return schedule
    
if __name__ == "__main__":

    walk = Task(
        description="Morning walk",
        time="8:00 AM",
        frequency="Daily",
        priority=1
    )

    feeding = Task(
        description="Feed dog",
        time="9:00 AM",
        frequency="Daily",
        priority=2
    )

    dog = Pet(
        name="Biscuit",
        species="Dog",
        breed="Golden Retriever",
        age=3
    )

    dog.add_task(walk)
    dog.add_task(feeding)

    owner = Owner(
        name="Alex",
        available_time=60
    )

    owner.add_pet(dog)

    scheduler = Scheduler(owner)

    plan = scheduler.generate_schedule()

    for task in plan:
        print(task.description)