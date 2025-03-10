from tkinter import Tk, Frame, Label, Button
from tkinter.font import Font

# Create the main window
root = Tk()
root.geometry('1200x800')
root.configure(bg='#232427')

poppins = Font(family="Poppins", size=12)

# Container setup
container = Frame(root, bg='#232427', padx=40, pady=40)
container.pack(expand=True)

# Function to create a card
def create_card(bg_color, label_text):
    card = Frame(container, width=320, height=440, bg='#2a2b2f', bd=0, relief='ridge')
    card.pack_propagate(False)
    card.pack(side='left', padx=30, pady=30)

    box = Frame(card, bg=bg_color, padx=20, pady=20)
    box.pack(expand=True, fill='both')

    content = Frame(box, bg='#2a2b2f')
    content.pack(expand=True, fill='both')

    h2 = Label(content, text='02', font=poppins, fg='rgba(255, 255, 255, 0.1)', bg='#2a2b2f', anchor='ne')
    h2.place(relx=0.5, rely=0, anchor='n')

    h3 = Label(content, text=label_text, font=Font(family="Poppins", size=15), fg='#fff', bg='#2a2b2f')
    h3.pack()

    p = Label(content, text='Sample description.', font=Font(family="Poppins", size=10), fg='rgba(255, 255, 255, 0.9)', bg='#2a2b2f')
    p.pack()

    btn = Button(content, text='Click Me', bg='black', fg='white', bd=0,
                 padx=10, pady=5, relief='flat', highlightthickness=0,
                 activebackground="white", activeforeground="black")
    btn.pack(pady=20)

# Creating multiple cards
create_card('#2196f3', 'Card 1')
create_card('#e91e63', 'Card 2')
create_card('#23c186', 'Card 3')

root.mainloop()
