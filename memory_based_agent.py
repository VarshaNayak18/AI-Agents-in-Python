# Memory-based agent in pure Python

memory = []

def memory_based_agent(task):
    task = task.lower()
    memory.append(task)

    if "who am i" in task:
        return "You told me: " + ", ".join(memory)

    elif "imu" in task:
        return "IMU is used to measure acceleration and angular velocity."

    elif "robot" in task:
        return "Robots sense the environment and act accordingly."

    elif "bye" in task:
        return "Goodbye! I will remember our conversation."

    else:
        return "I have stored this information."


# Run the agent
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Session ended")
        break
    
    response = memory_based_agent(user_input)
    print("Agent:", response)
