import openai as ai

# Initialize the API key
with open('api_key.env', 'r') as f:
    api_key = f.read()
    ai.api_key = api_key
    
question = ''
while(question != 'exit.'):
    with open("conversation_log.txt", "a") as log_file:
        # Define the prompt
        question = str(input('User question: '))
        if question.endswith('exit.'):
            break
        log_file.write('User: ' + question + '\n')
        prompt = question

            # Generate a response
        try:
            response = ai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=2048,
                n=1,
                stop=None,
                temperature=0.5,
            )

            # Print the response
            response_text = response['choices'][0]['text']
            print(response_text)
            log_file.write("Bot: " + response_text + "\n")
            
        except Exception as e:
            print('Network Error', e)
            log_file.wirte('Bot: Network Error\n')