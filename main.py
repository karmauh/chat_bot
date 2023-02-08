import tkinter as tk
import tkinter.font as tkFont
import openai as ai

# Initialize the API key
with open('api_key.env', 'r') as f:
        api_key = f.read()
        ai.api_key = api_key
        

# GUI init
class App:
    def __init__(self, root):
        # Setting title
        root.title("Chat Bot")
        
        # Setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # User message label 'User:'
        label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        label["font"] = ft
        label["fg"] = "#333333"
        label["justify"] = "center"
        label["text"] = "User:"
        label.place(x=10,y=10,width=40,height=30)

        entry=tk.Entry(root)
        entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entry["font"] = ft
        entry["fg"] = "#333333"
        entry["justify"] = "left"
        entry.place(x=50,y=10,width=406,height=30)
        self.entry = entry

        # Send user message button
        send_button=tk.Button(root)
        send_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        send_button["font"] = ft
        send_button["fg"] = "#000000"
        send_button["justify"] = "center"
        send_button["text"] = "SEND"
        send_button.place(x=460,y=10,width=60,height=30)
        send_button["command"] = self.send_message_to_bot
        
        # Exit button
        exit_button=tk.Button(root)
        exit_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        exit_button["font"] = ft
        exit_button["fg"] = "#000000"
        exit_button["justify"] = "center"
        exit_button["text"] = "EXIT"
        exit_button.place(x=530,y=10,width=60,height=30)
        exit_button["command"] = root.quit
        
        # Bot message
        bot_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        bot_label["font"] = ft
        bot_label["fg"] = "#333333"
        bot_label["justify"] = "left"
        bot_label["text"] = ""
        bot_label.place(x=10,y=50,width=406,height=50)
        self.bot_label = bot_label
        
        
    # Send message to bot
    def send_message_to_bot(self):
        with open("conversation_log.txt", "a") as log_file:
            # Get the user message
            user_message = self.entry.get()
            
            # Print the user message
            print('User: ' + user_message)
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
                
                # Print the bot response
                print("Bot: "+bot_message)
                
                # Bot message wirte to file
                log_file.write('Bot: ' + bot_message + '\n')
                
                self.bot_label["text"] = bot_message
            except Exception as e:
                print('Network Error', e)
                log_file.write('Bot: Network Error\n')


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()