# PawPal+ Project Reflection

## 1. System Design

### Core User Actions

The three core actions a user should be able to perform in PawPal+ are:

1. **Enter owner and pet information**  
   The user should be able to provide basic information about themselves and their pet so the system can create a personalized care plan.

2. **Add and manage pet care tasks**  
   The user should be able to create tasks such as walks, feeding, medication, grooming, and enrichment. Each task should include information such as duration and priority.

3. **Generate and view a daily schedule**  
   The user should be able to generate a daily plan that organizes tasks based on available time, priorities, and owner preferences. The system should also explain why tasks were selected.

### a. Initial design

My initial UML design was based on four main classes: Owner, Pet, Task, and Scheduler.

- **Owner**: Stores information about the pet owner, including their name, available time, and scheduling preferences. This information helps the scheduler consider the owner's constraints.

- **Pet**: Stores information about the pet, including name, species, breed, and age. This represents the pet that requires care.

- **Task**: Represents individual pet care activities such as walks, feeding, medication, grooming, or enrichment. It stores information such as task name, category, duration, priority, and completion status.

- **Scheduler**: Handles the scheduling logic by managing tasks, sorting tasks by priority, considering available time, and generating a daily care plan.

The design separates responsibilities between data storage and scheduling logic. Owner, Pet, and Task store information, while Scheduler is responsible for creating and organizing the daily schedule.

### b. Design changes

After reviewing my class skeleton with AI, I identified several improvements that would make the design better match the PawPal+ scenario.

The main changes I would make are:

- Add a relationship between **Owner and Pet** by allowing an owner to store a list of pets. This better represents the real-world scenario where one owner can have multiple pets.

- Add a relationship between **Pet and Task** so each task is connected to the specific pet it belongs to. This prevents confusion when an owner has multiple pets with different care needs.

- Update the **Scheduler** design so it references the owner's information instead of storing a separate copy of available time. This avoids having duplicate data that could become inconsistent.

- Improve task management by considering unique task identifiers and clearer scheduling rules, such as how priorities are ranked and what happens when there is not enough available time.

These changes would make the system easier to expand and would allow the scheduler to create more accurate daily plans.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
