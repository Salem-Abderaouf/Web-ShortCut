import os
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title('SHORTCUT')
root.geometry('200x60+0+200')
root.configure(background='#000000')
root.iconbitmap(default='add.ico')

# Define the widgets
val = tk.StringVar()
name = tk.Entry(root, width=60, textvariable=val)
button = tk.Button(root)
button.config(background="#000000", image=tk.PhotoImage(file="add.gif"))

# Set functions
def create_files():
    # Create a new folder with the name entered in the text entry
    folder_name = val.get()
    os.mkdir(f'./{folder_name}')
    
    # Copy files to the new folder
    with open('msg.txt', 'r') as file:
        data = file.read()
        with open(f'{folder_name}/index.html', 'w') as index_file:
            index_file.write(data)
        
        os.mkdir(os.path.join(str(folder_name), 'js'))
        with open(f'{folder_name}/js/app.js', 'w') as js_file:
            pass
        
        os.mkdir(os.path.join(str(folder_name), 'css'))
        with open(f'{folder_name}/css/style.css', 'w') as css_file:
            pass

def clear_text(event):
    # Clear the text entry when the user clicks on it
    name.delete(0, tk.END)

# Widget configuration
name.config(background="#000000", foreground="#9acd32")
name.insert(0, "Name Your Folder")
name.bind("<Button>", clear_text)

button.config(command=create_files)
button.pack(side=tk.LEFT)
name.pack(ipady=20)

# Start the main event loop
root.mainloop()
