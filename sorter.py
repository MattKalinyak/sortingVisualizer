from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubbleSort
from mergeSort import mergeSort
import threading


class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.algorithms = ('Bubble Sort', 'Merge Sort')
        self.speeds = ('Fast', 'Medium', 'Slow')
        self.setup()
        self.data = self.generateArray()
        self.draw(self.data, ['red' for x in range(len(self.data))])

    def setup(self):
        # UI
        ui = Frame(self, width = 900, height = 300)
        ui.grid(row = 0, column = 0)
        # Extra Space
        Label(ui, text = " ", pady = 10, padx = 100).grid(row = 0, column = 0)
        # Algorithm Label
        sortingLabel = Label(ui, text = "Choose Algorithm: ", font = 12)
        sortingLabel.grid(row = 1, column = 1, padx = 5, pady = 10, sticky = W)
        # Dropdown for Algorithm
        self.sortingChoice = ttk.Combobox(ui)
        self.sortingChoice['values'] = self.algorithms
        self.sortingChoice['state'] = 'readonly'
        self.sortingChoice.grid(row = 1, column = 2)
        self.sortingChoice.current(0)
        # Speed Label
        speedLabel = Label(ui, text = "Choose Speed: ", font = 12)
        speedLabel.grid(row = 2, column = 1)
        # Dropdown for Speed
        self.speedChoice = ttk.Combobox(ui)
        self.speedChoice['values'] = self.speeds
        self.speedChoice['state'] = 'readonly'
        self.speedChoice.grid(row = 2, column = 2)
        self.speedChoice.current(0)
        # Generate Button
        self.genButton = Button(ui, text = "Generate", font = 12, command = self.generate)
        self.genButton.grid(row = 3, column = 1)
        # Run Button
        self.startButton = Button(ui, text = "Run", font = 12, command = self.start)
        self.startButton.grid(row = 3, column = 2)
        # Canvas to draw the Array
        self.canvas = Canvas(self, width=700, height=400, bg='WHITE')
        self.canvas.grid(row=1, column=0, columnspan = 6, padx=10, pady=5)

    def generate(self):
        self.data = self.generateArray()
        self.draw(self.data, ['red' for x in range(len(self.data))])

    # Creates new data
    def generateArray(self):
        data = []
        for i in range(0, 75):
            data.append(random.randint(1+(i-i), 150))
        return data

    # Visualizes the data
    def draw(self, data, colorArray):
        self.canvas.delete("all") # deletes previous data
        width = 700 # Canvas Width
        height = 400 #Canvas Height
        offset = 6 #Space on the edges
        spacing = 3 # Space between
        x_width = width/(len(data) + 1) # width of each rectangle
        normalizedData = [i/max(data) for i in data]

        # Loops through creating each rectangle
        for i, h in enumerate(normalizedData):
            x0 = i * x_width + offset + spacing
            y0 = height - h*390
            x1 = (i + 1) * x_width + offset
            y1 = height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

        # Updates the canvas with the new rectangles
        root.update_idletasks()

    def startThread(self):
        try:
            self.t1 = threading.Thread(target = self.start)
            self.t1.start()
        except Exception:
            print("Exception in t1")

    def start(self):
        speed = self.setSpeed()
        choice = self.sortingChoice.get()
        if (choice == 'Bubble Sort'): bubbleSort(self.data, speed, self.draw)
        if (choice == 'Merge Sort'): mergeSort(self.data, 0, len(self.data)-1, self.draw, speed)
        

    def setSpeed(self):
        val = self.speedChoice.get()
        if (val == 'Fast'): return .01
        elif (val == 'Medium'): return .05
        else: return .1

        
    
root = Tk()
root.title("WAN Tool")
root.geometry("725x600")
app = App(master=root)
app.mainloop()