from tkinter import *

raiz = Tk()
raiz.title("Numeros y sus bases")
raiz.geometry("600x180")
raiz.configure(bg="#76b5a0")

numbLabel = Label(raiz, text="COLOQUE UN NUMERO ENTERO: ",
                  font=("Courier", 12, "bold"), bg="#76b5a0")
numbLabel.grid(row=1, column=0)

numbEntry = Entry(raiz, bg="#fbc599", fg="#9b726f",
                  font=("Courier", 12, "bold"), width=20)
numbEntry.focus()
numbEntry.grid(row=1, column=1)


def calcular_todos():
    global binLabelRta
    global hexLabelRta
    global octLabelRta
    a = int(numbEntry.get())
    binario = bin(a)[2:]
    binLabelRta.config(text=binario)

    hexadecimal = hex(a)[2:]
    hexLabelRta.config(text=hexadecimal)

    octal = oct(a)[2:]
    octLabelRta.config(text=octal)


btn1 = Button(raiz, text="CALCULAR", command=calcular_todos,
              width=11, height=1, bg="yellow", font=("Courier", 12, "bold"))
btn1.grid(row=2, column=0, sticky=S+E)

binLabel = Label(raiz, text="Base Binaria: ", font=(
    "Courier", 12, "bold"), bg="#76b5a0").grid(row=3, column=0)
binLabelRta = Label(raiz, font=("Courier", 12, "bold"), bg="#76b5a0", text="")
binLabelRta.grid(row=3, column=1)

hexLabel = Label(raiz, text="Base Hexadecimal: ", font=(
    "Courier", 12, "bold"), bg="#76b5a0").grid(row=4, column=0)
hexLabelRta = Label(raiz, font=("Courier", 12, "bold"), bg="#76b5a0", text="")
hexLabelRta.grid(row=4, column=1)

octLabel = Label(raiz, text="Base Octal: ", font=(
    "Courier", 12, "bold"), bg="#76b5a0").grid(row=5, column=0)
octLabelRta = Label(raiz, font=("Courier", 12, "bold"), bg="#76b5a0", text="")
octLabelRta.grid(row=5, column=1)

raiz.mainloop()
