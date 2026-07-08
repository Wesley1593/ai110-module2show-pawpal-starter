import streamlit as st 
from pawpal_system import Owner, Pet, Task, Scheduler


st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")


# Create Owner object only once and store it in Streamlit memory
if "owner" not in st.session_state:
    st.session_state.owner = Owner(
        name="Jordan",
        available_time=120,
        preferences={}
    )

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Add Pet"):
    new_pet = Pet(
        name=pet_name,
        species=species,
        breed="Unknown",
        age=0
    )

    st.session_state.owner.add_pet(new_pet)

    st.success(f"{pet_name} added!")

if st.session_state.owner.pets:
    st.subheader("Your Pets")

    for pet in st.session_state.owner.pets:
        st.write(
            f"🐾 {pet.name} - {pet.species}"
        )

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")


col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add Task"):
    if st.session_state.owner.pets:

        priority_value = {
            "high": 1,
            "medium": 2,
            "low": 3
        }

        task = Task(
            description=task_title,
            time="Morning",
            frequency="Daily",
            priority=priority_value[priority]
        )

        st.session_state.owner.pets[0].add_task(task)

        st.success("Task added!")

    else:
        st.warning("Add a pet first.")

if st.session_state.owner.pets:
    st.subheader("Current Tasks")

    for pet in st.session_state.owner.pets:
        st.write(f"🐾 {pet.name}'s Tasks:")

        for task in pet.tasks:
            st.write(
                f"- {task.description} | {task.time} | Priority: {task.priority}"
            )

st.divider()

st.subheader("Build Schedule")
st.caption("Generate a daily plan based on your pet tasks.")

if st.button("Generate schedule"):

    scheduler = Scheduler(st.session_state.owner)

    schedule = scheduler.generate_schedule()

    if schedule:
        st.success("Today's Schedule")

        for task in schedule:
            st.write(
                f"- {task.description} | {task.time} | Priority: {task.priority}"
            )

    else:
        st.info("No tasks available for today's schedule.")

