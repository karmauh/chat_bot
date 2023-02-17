from app import App, tk, ai

# Initialize the API key
with open('api_key.env', 'r') as f:
        api_key = f.read()
        ai.api_key = api_key
       
       
       
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()