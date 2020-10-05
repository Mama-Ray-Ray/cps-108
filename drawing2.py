from tkinter import Tk, Canvas, mainloop

root = Tk()
c = Canvas(root, width=500, height=500)
c.pack()

# Checkered Square
c.create_rectangle(25, 25, 50, 50, fill='black')
c.create_rectangle(50, 50, 75, 75, fill='black')
def checker1(x, y, height, width, fill='black'):
    c.create_rectangle(x,y, x+width, y+height, fill='black')
def checker1_row(y):
    for x in range(50, 450+1, 50):
        checker1(x,y, 25, 25, 'black')
for y in range(50, 450+1, 50):
    checker1_row(y)
def checker2(x, y, height, width, fill='black'):

# Lines
for y in range(50, 500, 50):
    c.create_line(0, y, 500, y)
    c.create_text(18, y + 10, text=str(y))

for x in range(50, 500, 50):
    c.create_line(x, 0, x, 500)
    c.create_text(x + 18, 10, text=str(x))

def react_to_click(event):
    root.quit()

c.bind('<Button-1>', react_to_click)
mainloop()
