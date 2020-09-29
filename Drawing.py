from tkinter import Tk, Canvas, mainloop

root = Tk()
c = Canvas(root, width=500, height=500)
c.pack()

# Put drawing here!
c.create_rectangle(0, 0, 500, 300, fill='blue')
c.create_rectangle(0, 300, 500, 500, fill='green')
c.create_rectangle(150, 300, 300, 400, fill='yellow')
c.create_rectangle(200, 350, 250, 400, fill='red')
c.create_polygon(100, 300, 225, 200, 350, 300, fill='red')
c.create_oval(350, 100, 400, 150, fill='white')
c.create_oval(375, 50, 425, 100, fill='white' )
c.create_oval(400, 75, 500, 150, fill='white')
c.create_oval(375, 125, 425, 175, fill='white')
c.create_oval(50, 50, 100, 100, fill='white')
c.create_oval(75, 75, 150, 150, fill='white')
c.create_oval(125, 100, 175, 150, fill='white')

# Lines
# for y in range(50, 500, 50):
#     c.create_line(0, y, 500, y)
#     c.create_text(18, y + 10, text=str(y))

# for x in range(50, 500, 50):
#     c.create_line(x, 0, x, 500)
#     c.create_text(x + 18, 10, text=str(x))

def react_to_click(event):
    root.quit()

c.bind('<Button-1>', react_to_click)
mainloop()
