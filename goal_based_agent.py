# Goal-based agent

def goal_based_agent(task,goal):
    task = task.lower()

    if goal == "education":
        if "imu" in task:
            return "IMU measures acceleration and rotation to help robots maintain balance"
        elif "pid" in task:
            return "PID controller maintains stability using feedback control"
        else:
            return "I can explain robotics concepts for learning."

    elif goal == "exam":
        if "imu" in task:
            return "IMU is an inertial sensor used to measure linear acceleration and angular velocity."
        else:
            return "Ask exam-related questions."

    elif goal == "conversation":
        if "hello" in task:
            return "Hello! How can I help you?"
        else:
            return "Let's talk."

    else:
        return "Goal not recognized."
    
# Run the agent
goal=input("Set agent goal(education/exam/conversation): ")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goal session ended")
        break

    response = goal_based_agent(user_input, goal)
    print("Agent:", response)