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

    def mark_complete(self):
        """Mark task as completed and create recurring task if needed."""

        self.completed = True

        if self.frequency in ["Daily", "Weekly"]:
            return self.create_next_occurrence()

        return None

    def create_next_occurrence(self):
        """Create the next version of a recurring task."""

        if self.frequency in ["Daily", "Weekly"]:
            return Task(
                description=self.description,
                time=self.time,
                frequency=self.frequency,
                priority=self.priority
            )

        return None

    def update_task(
        self,
        description=None,
        time=None,
        frequency=None,
        priority=None
    ):
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
        """Initialize scheduler with owner."""

        self.owner = owner
        self.daily_schedule = []

    def get_available_tasks(self) -> list[Task]:
        """Retrieve tasks from owner's pets."""

        return self.owner.get_all_tasks()

    def sort_tasks_by_priority(self, tasks: list[Task]) -> list[Task]:
        """Sort tasks by priority."""

        return sorted(
            tasks,
            key=lambda task: task.priority
        )

    def sort_by_time(self, tasks: list[Task]) -> list[Task]:
        """Sort tasks by scheduled time."""

        return sorted(
            tasks,
            key=lambda task: task.time
        )

    def filter_completed_tasks(self, tasks: list[Task]) -> list[Task]:
        """Remove completed tasks."""

        return [
            task
            for task in tasks
            if not task.completed
        ]

    def detect_conflicts(self, tasks: list[Task]) -> list[str]:
        """Detect tasks scheduled at the same time."""

        conflicts = []

        for i in range(len(tasks)):
            for j in range(i + 1, len(tasks)):

                if tasks[i].time == tasks[j].time:

                    conflicts.append(
                        f"Conflict: {tasks[i].description} and "
                        f"{tasks[j].description} are both scheduled at "
                        f"{tasks[i].time}"
                    )

        return conflicts

    def generate_schedule(self) -> list[Task]:
        """Generate daily schedule based on priority and time."""

        tasks = self.get_available_tasks()

        # Remove completed tasks
        tasks = self.filter_completed_tasks(tasks)

        # Sort by priority
        tasks = self.sort_tasks_by_priority(tasks)

        schedule = []

        total_time = 0

        for task in tasks:

            # Each task counts as 30 minutes for now
            if total_time + 30 <= self.owner.available_time:

                schedule.append(task)

                total_time += 30

        # Sort final schedule by time
        schedule = self.sort_by_time(schedule)

        self.daily_schedule = schedule

        return schedule


# Demo test
if __name__ == "__main__":

    walk = Task(
        description="Morning walk",
        time="09:00",
        frequency="Daily",
        priority=1
    )

    feeding = Task(
        description="Feed dog",
        time="08:00",
        frequency="Daily",
        priority=2
    )

    grooming = Task(
        description="Brush dog",
        time="08:00",
        frequency="Weekly",
        priority=3
    )


    dog = Pet(
        name="Biscuit",
        species="Dog",
        breed="Golden Retriever",
        age=3
    )


    dog.add_task(walk)
    dog.add_task(feeding)
    dog.add_task(grooming)


    owner = Owner(
        name="Alex",
        available_time=120
    )

    owner.add_pet(dog)


    scheduler = Scheduler(owner)


    print("Sorted Schedule:")

    plan = scheduler.generate_schedule()

    for task in plan:
        print(
            task.time,
            "-",
            task.description
        )


    print("\nConflicts:")

    conflicts = scheduler.detect_conflicts(plan)

    for conflict in conflicts:
        print(conflict)