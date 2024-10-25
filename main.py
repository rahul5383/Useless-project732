import openai

openai.api_key = "your_openai_api_key_here"

def generate_motivational_response(conversation_history, user_goal=None):
    prompt = f"""
    You are a witty, motivational insult bot. Your job is to help the user achieve their goals by lightly insulting them in a funny but encouraging way. The insults should be motivational and should push the user to do better.
    
    User's Goal: {user_goal if user_goal else "Not provided yet"}
    
    Here's the conversation so far:
    
    {conversation_history}
    
    Now respond with a motivational insult to push the user to improve.
    """
    
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # or "gpt-4"
        prompt=prompt,
        max_tokens=100,
        temperature=0.8,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    return response.choices[0].text.strip()

def start_conversation():
    conversation_history = ""
    user_goal = None  
    
    print("Motivational Insulter Bot: What's your goal today? (Type 'quit' to exit)")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'quit':
            print("Motivational Insulter Bot: Alright, quitter! See you next time.")
            break
        
        if not user_goal:
            user_goal = user_input
            conversation_history += f"User's goal: {user_goal}\n"
            print(f"Motivational Insulter Bot: Got it! I'll make sure you stick to {user_goal}.")
            continue
        
        conversation_history += f"User: {user_input}\n"
        
        bot_response = generate_motivational_response(conversation_history, user_goal)
        conversation_history += f"Bot: {bot_response}\n"
        
        print(f"Motivational Insulter Bot: {bot_response}")


if __name__ == "__main__":
    start_conversation()
