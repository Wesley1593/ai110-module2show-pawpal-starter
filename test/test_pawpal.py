from pawpal_system import Task, Pet


def test_task_completion():
    """Verify that marking a task complete changes its status."""

    task = Task(
        description="Morning walk",
        time="8:00 AM",
        frequency="Daily",
        priority=1
    )

    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_task_addition():
    """Verify adding a task increases a pet's task count."""

    pet = Pet(
        name="Max",
        species="Dog",
        breed="Golden Retriever",
        age=4
    )

    task = Task(
        description="Feed Max",
        time="9:00 AM",
        frequency="Daily",
        priority=2
    )

    assert len(pet.tasks) == 0

    pet.add_task(task)

    assert len(pet.tasks) == 1