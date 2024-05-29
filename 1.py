import tkinter

def convert():
    value = inputValue.get()
    returnValue = float(value) * 1.6
    outputValue.set(returnValue)

root = tkinter.Tk()
root.geometry("200x200")

label = tkinter.Label(master=root, text="Miles to kilometers converter")
label.pack()

inputValue = tkinter.StringVar()
inputField = tkinter.Entry(master=root, textvariable=inputValue)
inputField.pack(pady=20)

button = tkinter.Button(master=root, text="Convert", command=convert)
button.pack()

outputValue = tkinter.StringVar()
output = tkinter.Label(master=root, textvariable=outputValue)
output.pack()

root.mainloop()