import tkinter as tk
import tkinter.font as tkFont
import openai as ai


# GUI init 
class GUI:
    def __init__(self, root):
        # Setting title
        root.title("Chat Bot")
        
        # Setting main window values
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # User message label 'User:'
        label=tk.Label(root)
        ft = tkFont.Font(family='Comfortaa', size=11)
        label["font"] = ft
        label["text"] = 'User:'
        label.place(x=10, y=10, width=40, height=30)

        # User message entry
        entry=tk.Entry(root)
        entry["borderwidth"] = '1px'
        entry["font"] = ft
        entry["justify"] = 'left'
        entry.place(x=50, y=10, width=406, height=30)
        self.entry = entry
        
        # Bind the <Return> key to the send_message_to_bot function
        entry.bind('<Return>', lambda event: self.send_message_to_bot())
        
        # Send user message button
        send_button=tk.Button(root)
        send_button["font"] = ft
        send_button["text"] = 'SEND'
        send_button.place(x=460, y=10, width=60, height=30)
        send_button["command"] = self.send_message_to_bot
        
        # Exit button
        exit_button=tk.Button(root)
        exit_button["font"] = ft
        exit_button["text"] = 'EXIT'
        exit_button.place(x=530, y=10, width=60, height=30)
        exit_button["command"] = root.quit
        
        # Bot message
        bot_label=tk.Label(root, wraplength=400)
        bot_label["font"] = ft
        bot_label["justify"] = 'left'
        bot_label.place(x=10, y=40, width=406, height=406)
        self.bot_label = bot_label


class App(GUI):
    # Send message to bot
    def send_message_to_bot(self):
        with open("conversation_log.txt", "a") as log_file:
            # Get the user message
            user_message = self.entry.get()
            
            # print('User: ' + user_message)
            prompt = user_message
            
            # User message write to file
            log_file.write('User: ' + user_message + '\n')
            
            # Create the response object
            try:
                response = ai.Completion.create(
                    engine='text-davinci-002',
                    prompt=prompt,
                    max_tokens=2048,
                    n=1,
                    stop=None,
                    temperature=0.5,
                )
                
                # Get the bot response
                bot_message = response['choices'][0]['text']
                print('Bot: ' + bot_message)
                
                # Bot message wirte to file
                log_file.write('Bot: ' + bot_message)
                self.bot_label['text'] = bot_message.strip()
                
            except (KeyError) as e:
                print('Error occurred while making request to OpenAI API: ', e)
                log_file.write('Bot: Error occurred while making request to OpenAI API\n')
                
                exit(1)