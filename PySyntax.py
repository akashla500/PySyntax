from tkinter import *


def main():
    def clearEditor():
        codeEditor.delete(1.0, END)
        fileName.delete(0, END)

    def saveFile():
        code = codeEditor.get(0.1, END)
        file = fileName.get()
        if len(file) == 0:
            file = "Code_PySyntax"
        with open(file+".py", "w") as sourceCodeFile:
            sourceCodeFile.write(code)
        clearEditor()

    def tabChange(arg):
        codeEditor.insert(INSERT, " "*4)
        return 'break'

    def spaceCalculation():
        space = ""
        indexLocation = str(codeEditor.index(INSERT))
        indexLocation = indexLocation.split(".")
        code = codeEditor.get(0.1, END)
        code = code.split("\n")
        code = code[int(indexLocation[0]) - 1]
        striped = code.strip()
        striped = striped[::-1]
        if len(striped) != 0:
            if striped[0] != ":":
                for i in code:
                    if i == " ":
                        space = space + " "
                    else:
                        break
        else:
            space = int(indexLocation[1])*" "
        return space

    def enterChange(arg):
        space = spaceCalculation()
        codeEditor.insert(INSERT, "\n")
        codeEditor.insert(INSERT, space)
        return 'break'

    def write(command):
        indexLocation = str(codeEditor.index(INSERT))
        indexLocation = indexLocation.split(".")
        if command == "input":
            space = spaceCalculation()
            codeEditor.insert(indexLocation[0]+"."+indexLocation[1], "input(\"\")\n"+space)
        elif command == "print":
            space = spaceCalculation()
            codeEditor.insert(indexLocation[0]+"."+indexLocation[1], "print()\n"+space)
        elif command == "if":
            space = spaceCalculation() + "    "
            codeEditor.insert(indexLocation[0]+"."+indexLocation[1], "if :\n"+space)
        elif command == "elif":
            space = spaceCalculation() + "    "
            codeEditor.insert(indexLocation[0]+"."+indexLocation[1], "elif :\n"+space)
        elif command == "else":
            space = spaceCalculation() + "    "
            codeEditor.insert(indexLocation[0]+"."+indexLocation[1], "else:\n"+space)
        elif command == "while":
            space = spaceCalculation() + "    "
            codeEditor.insert(indexLocation[0] + "." + indexLocation[1], "while :\n" + space)
        elif command == "for":
            space = spaceCalculation() + "    "
            codeEditor.insert(indexLocation[0]+"."+indexLocation[1], "for i in :\n"+space)
        elif command == "function":
            space = spaceCalculation() + "    "
            codeEditor.insert(indexLocation[0] + "." + indexLocation[1], "def fn_name():\n" + space)
        elif command == "lambda":
            space = spaceCalculation()
            codeEditor.insert(indexLocation[0]+"."+indexLocation[1], "fn_name = lambda args : expression\n"+space)
        elif command == "class":
            space = spaceCalculation() + "    "
            codeEditor.insert(indexLocation[0]+"."+indexLocation[1], "class cls_name():\n"+space)
        elif command == "init":
            space = spaceCalculation() + "    "
            codeEditor.insert(indexLocation[0]+"."+indexLocation[1], "def __init__(self):\n"+space)
        elif command == "method":
            space = spaceCalculation() + "    "
            codeEditor.insert(indexLocation[0]+"."+indexLocation[1], "def fn_name(self):\n"+space)
        elif command == "try":
            space = spaceCalculation() + "    "
            codeEditor.insert(indexLocation[0]+"."+indexLocation[1], "try():\n"+space)
        elif command == "except":
            space = spaceCalculation() + "    "
            codeEditor.insert(indexLocation[0]+"."+indexLocation[1], "except():\n"+space)
        elif command == "finally":
            space = spaceCalculation() + "    "
            codeEditor.insert(indexLocation[0]+"."+indexLocation[1], "finally():\n"+space)
        elif command == "r":
            space = spaceCalculation() + "    "
            codeEditor.insert(indexLocation[0]+"."+indexLocation[1], "with open(file_name, \"r\") as file:\n"+space)
        elif command == "w":
            space = spaceCalculation() + "    "
            codeEditor.insert(indexLocation[0]+"."+indexLocation[1], "with open(file_name, \"w\") as file:\n"+space)
        elif command == "a":
            space = spaceCalculation() + "    "
            codeEditor.insert(indexLocation[0]+"."+indexLocation[1], "with open(file_name, \"w\") as file:\n"+space)
        elif command == "r+":
            space = spaceCalculation() + "    "
            codeEditor.insert(indexLocation[0]+"."+indexLocation[1], "with open(file_name, \"r+\") as file:\n"+space)
        elif command == "a+":
            space = spaceCalculation() + "    "
            codeEditor.insert(indexLocation[0]+"."+indexLocation[1], "with open(file_name, \"a+\") as file:\n"+space)
        elif command == "range":
            space = spaceCalculation()
            codeEditor.insert(indexLocation[0]+"."+indexLocation[1], "range(end)\n"+space)

    # PySyntax box configurations
    PySyntaxWindow = Tk()
    PySyntaxWindow.title("PySyntax")
    PySyntaxWindow.geometry("1200x600+130+100")
    PySyntaxWindow.resizable(False, False)

    # Code editor
    codeEditor = Text(PySyntaxWindow, width=77, height=33, font=12)
    codeEditor.bind("<Tab>", tabChange)
    codeEditor.bind("<Return>", enterChange)
    codeEditor.place(x=15, y=10)

    # File name
    fileName = Entry(PySyntaxWindow)
    fileName.place(x=30, y=550)
    pyLabel = Label(PySyntaxWindow, text=".py")
    pyLabel.place(x=220, y=550)
    # Save button
    saveButton = Button(PySyntaxWindow, text="Save", command=saveFile)
    saveButton.place(x=260, y=548)
    # Clear button
    clearButton = Button(PySyntaxWindow, text="Clear", command=clearEditor)
    clearButton.place(x=360, y=548)

    # User Interaction
    userInteraction = Label(PySyntaxWindow, text="User Interaction")
    userInteraction.place(x=720, y=10)
    inputButton = Button(PySyntaxWindow, text="input", command=lambda: write("input"))
    inputButton.place(x=730, y=30)
    printButton = Button(PySyntaxWindow, text="print", command=lambda: write("print"))
    printButton.place(x=800, y=30)

    # Control statements
    controlStatements = Label(PySyntaxWindow, text="Control Statements")
    controlStatements.place(x=720, y=70)
    ifButton = Button(PySyntaxWindow, text="if", command=lambda: write("if"))
    ifButton.place(x=730, y=90)
    elifButton = Button(PySyntaxWindow, text="elif", command=lambda: write("elif"))
    elifButton.place(x=780, y=90)
    elseButton = Button(PySyntaxWindow, text="else", command=lambda: write("else"))
    elseButton.place(x=840, y=90)
    whileButton = Button(PySyntaxWindow, text="while", command=lambda: write("while"))
    whileButton.place(x=905, y=90)
    forButton = Button(PySyntaxWindow, text="for", command=lambda: write("for"))
    forButton.place(x=975, y=90)

    # Functions
    functions = Label(PySyntaxWindow, text="Functions")
    functions.place(x=720, y=130)
    functionButton = Button(PySyntaxWindow, text="function", command=lambda: write("function"))
    functionButton.place(x=730, y=150)
    lambdaButton = Button(PySyntaxWindow, text="lambda", command=lambda: write("lambda"))
    lambdaButton.place(x=820, y=150)

    # Class
    classLabel = Label(PySyntaxWindow, text="Class")
    classLabel.place(x=720, y=190)
    classButton = Button(PySyntaxWindow, text="class", command=lambda: write("class"))
    classButton.place(x=730, y=210)
    initButton = Button(PySyntaxWindow, text="init", command=lambda: write("init"))
    initButton.place(x=800, y=210)
    methodButton = Button(PySyntaxWindow, text="method", command=lambda: write("method"))
    methodButton.place(x=860, y=210)

    # Exception handling
    exceptionHandling = Label(PySyntaxWindow, text="Exception Handling")
    exceptionHandling.place(x=720, y=250)
    tryButton = Button(PySyntaxWindow, text="try", command=lambda: write("try"))
    tryButton.place(x=730, y=270)
    exceptButton = Button(PySyntaxWindow, text="except", command=lambda: write("except"))
    exceptButton.place(x=785, y=270)
    finallyButton = Button(PySyntaxWindow, text="finally", command=lambda: write("finally"))
    finallyButton.place(x=865, y=270)

    # File operations
    fileOperations = Label(PySyntaxWindow, text="File operations")
    fileOperations.place(x=720, y=310)
    openR = Button(PySyntaxWindow, text="Open Read", command=lambda: write("r"))
    openR.place(x=730, y=330)
    openW = Button(PySyntaxWindow, text="Open Write", command=lambda: write("w"))
    openW.place(x=840, y=330)
    openA = Button(PySyntaxWindow, text="Open Append", command=lambda: write("a"))
    openA.place(x=950, y=330)
    openWPlus = Button(PySyntaxWindow, text="Read & Write", command=lambda: write("r+"))
    openWPlus.place(x=1075, y=330)
    openAPlus = Button(PySyntaxWindow, text="Read & Append", command=lambda: write("a+"))
    openAPlus.place(x=730, y=360)

    # Misc.
    misc = Label(PySyntaxWindow, text="Misc.")
    misc.place(x=720, y=400)
    rangeButton = Button(PySyntaxWindow, text="range", command=lambda: write("range"))
    rangeButton.place(x=730, y=420)

    PySyntaxWindow.mainloop()


if __name__ == "__main__":
    main()
