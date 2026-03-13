# Simple Rule Based Agent

def simple_agent(task):
    task=task.lower()

    if "hello" in task or "hi" in task:
        return "Hello! I am a simple python agent. How may I help you today?"
    
    elif "robot" in task:
        return "A robot is a machine capable of sensing, thinking, and acting"
    
    elif "ai" in task:
        return "Artificial Intelligence(AI) is a branch of computer science that enables machines to simulate human intelligence, such as learning, reasoning, problem-solving, and perception"
    
    elif "thank you" in task or "thanks" in task:
        return "You're welcome"
    
    else:
        return "I don't understand yet. I'm still learning"
    
# Run the agent
while True:
    user_input=input("Enter user response: ")
    if user_input.lower()=="exit":
        print("Agent shutting down")
        break

    response=simple_agent(user_input)
    print("Agent response:", response)