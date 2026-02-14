from tkinter import *
import tkinter as tk
import math
import tkinter.messagebox


class Calc:
    def getandreplace(self):  # replace x, + and % to symbols that can be used in calculations
        # we wont re write this to the text box until we are done with calculations

        self.txt = self.e.get()  # Get value from text box and assign it to the global txt var
        self.txt = self.txt.replace('÷', '/')
        self.txt = self.txt.replace('x', '*')
        self.txt = self.txt.replace('%', '/100')
        self.txt = self.txt.replace('^', '**')

    def evaluation(self, specfunc):  # Evaluate the items in the text box for calculation specfunc = eq, sqroot or power
        self.getandreplace()
        try:
            self.txt = eval(str(self.txt))  # evaluate the expression using the eval function
        except Exception as e:
            self.displayinvalid()

        else:
            if any([specfunc == 'sqroot', specfunc == 'power', specfunc == 'fact', specfunc == '1/x', specfunc == 'log',
                    specfunc == 'ln',
                    specfunc == 'sin', specfunc == 'cos', specfunc == 'tan', specfunc == 'asin', specfunc == 'acos',
                    specfunc == 'atan',
                    specfunc == 'sinh', specfunc == 'cosh', specfunc == 'tanh', specfunc == 'asinh',
                    specfunc == 'acosh', specfunc == 'atanh',
                    specfunc == 'e', specfunc == 'pi', specfunc == '10^x', specfunc == 'pm', specfunc == 'rad',
                    specfunc == 'qubicroot', specfunc == 'exp',
                    specfunc == 'bin', specfunc == 'hex', specfunc == 'oct', specfunc == 'in-cm', specfunc == 'cm-in',
                    specfunc == 'ft-m', specfunc == 'm-ft',
                    specfunc == 'mile-km', specfunc == 'km-mile', specfunc == '°C-°F', specfunc == '°F-°C',
                    specfunc == 'radian-degree', specfunc == 'j-cal',
                    specfunc == 'cal-j', specfunc == 'kg-lb', specfunc == 'lb-kg']):
                self.txt = self.evalspecialfunctions(specfunc)

            self.refreshtext()

    def displayinvalid(self):

        self.e.delete(0, END)
        self.e.insert(0, 'Invalid !')

    def refreshtext(self):  # Delete current contents of textbox and replace with our completed evaluatioin
        self.e.delete(0, END)
        self.e.insert(0, self.txt)

    def evalspecialfunctions(self, specfunc):  # Calculate square root and power if specfunc is sqroot or power
        if specfunc == 'sqroot':
            return math.sqrt(float(self.txt))
        elif specfunc == 'power':
            return math.pow(float(self.txt), 2)
        elif specfunc == 'qubicroot':
            return math.pow(float(self.txt), 1 / 3)

        elif specfunc == 'fact':
            return math.factorial(int(self.txt))
        elif specfunc == 'exp':
            return math.exp(float(self.txt))
        elif specfunc == '10^x':
            return (10 ** (float(self.txt)))
        elif specfunc == 'pm':
            return -float((self.txt))

        elif specfunc == 'log':
            return math.log10(float(self.txt))
        elif specfunc == 'ln':
            return math.log(float(self.txt))
        elif specfunc == 'rad':
            return .017453 * (float(self.txt))
        elif specfunc == '1/x':
            return (1 / (float(self.txt)))


        elif specfunc == 'sin':
            return math.sin(math.radians(float(self.txt)))
        elif specfunc == 'cos':
            return math.cos(math.radians(float(self.txt)))
        elif specfunc == 'tan':
            if self.txt == 90:
                self.displayinvalid()
            elif self.txt == -90:
                self.displayinvalid()
            else:
                return math.tan(math.radians(float(self.txt)))

        elif specfunc == 'asin':
            if self.txt > 1:
                self.displayinvalid()
            elif self.txt < -1:
                self.displayinvalid()
            else:
                return math.degrees(math.asin(float(self.txt)))

        elif specfunc == 'acos':
            if self.txt > 1:
                self.displayinvalid()
            elif self.txt < -1:
                self.displayinvalid()
            else:
                return math.degrees(math.acos(float(self.txt)))

        elif specfunc == 'atan':
            return math.degrees(math.atan(float(self.txt)))
        elif specfunc == 'sinh':
            return math.sinh(float(self.txt))
        elif specfunc == 'cosh':
            return math.cosh(float(self.txt))
        elif specfunc == 'tanh':
            return math.tanh(float(self.txt))
        elif specfunc == 'asinh':
            return math.asinh(float(self.txt))
        elif specfunc == 'acosh':
            return math.acosh(float(self.txt))
        elif specfunc == 'atanh':
            return math.atanh(float(self.txt))

        elif specfunc == 'bin':
            return bin(int(self.txt))
        elif specfunc == 'hex':
            return hex(int(self.txt))
        elif specfunc == 'oct':
            return oct(int(self.txt))
        elif specfunc == 'in-cm':
            return 2.54 * (float(self.txt))
        elif specfunc == 'cm-in':
            return (50 / 127) * (float(self.txt))
        elif specfunc == 'm-ft':
            return (1250 / 381) * (float(self.txt))
        elif specfunc == 'ft-m':
            return (381 / 1250) * (float(self.txt))
        elif specfunc == 'mile-km':
            return 1.609344 * (float(self.txt))
        elif specfunc == 'km-mile':
            return .62137 * (float(self.txt))
        elif specfunc == '°F-°C':
            return (5 / 9) * ((-32 + float(self.txt)))
        elif specfunc == '°C-°F':
            return 32 + (9 / 5 * (float(self.txt)))
        elif specfunc == 'radian-degree':
            return 57.2957 * (float(self.txt))
        elif specfunc == 'j-cal':
            return (5000 / 20929) * (float(self.txt))
        elif specfunc == 'cal-j':
            return (20929 / 5000) * (float(self.txt))
        elif specfunc == 'kg-lb':
            return (2.204622476) * (float(self.txt))
        elif specfunc == 'lb-kg':
            return (0.4535924) * (float(self.txt))

    def clearall(self):  # AC button pressed on form or 'esc" pressed on keyboard
        self.e.delete(0, END)
        self.e.insert(0, '0')

    def clear(self):
        # C button press on form or backspace press on keyboard event defined on keyboard press

        self.txt = self.e.get()[:-1]

        self.e.delete(0, END)
        self.e.insert(0, self.txt)

    def action(self, argi: object):  # Number or operator button pressed on form and passed in as argi
        self.txt = self.getvalue()

        self.stripfirstchar()

        self.e.insert(END, argi)

    def keyaction(self, event=None):  # Key pressed on keyboard which defines event
        self.txt = self.getvalue()

        if event.char.isdigit():
            self.stripfirstchar()
        elif event.char in '/*-+%().':
            self.stripfirstchar()
        elif event.char == '\x08':
            self.clear1(event)
        elif event.char == '\x1b':
            self.clearall()
        elif event.char == '\r':
            self.evaluation('eq')
        else:
            self.displayinvalid()
            return 'break'

    def stripfirstchar(self):  # Strips leading 0 from text box with first key or button is pressed
        if self.txt[0] == '0':
            self.e.delete(0, 1)

    def getvalue(self):  # Returns value of the text box
        return self.e.get()

    def __init__(self, master):  # Constructor method

        self.txt = 'o'  # Global var to work with text box contents
        master.title('Scientific Calulator')
        master.geometry()
        self.e = Entry(master, font=('arial', 20), bg="white", bd=12, width=30)

        self.e.grid(row=0, column=0, columnspan=6, pady=3)
        self.e.insert(0, '0')
        self.e.focus_set()
        # Generating Buttons
        Button(master, text="=", width=13, height=2, pady=1, font=('arial', 15, 'bold'), bg="Misty rose3",
               command=lambda: self.evaluation('eq')).grid(row=4, column=4, columnspan=2)
        Button(master, text='AC', width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="Misty rose1",
               command=lambda: self.clearall()).grid(row=1, column=4)
        Button(master, text='C', width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="Misty rose2",
               command=lambda: self.clear()).grid(row=1, column=5)
        Button(master, text="+", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="light slate blue",
               command=lambda: self.action('+')).grid(row=4, column=3)
        Button(master, text="x", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="light slate blue",
               command=lambda: self.action('x')).grid(row=2, column=3)
        Button(master, text="-", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="light slate blue",
               command=lambda: self.action('-')).grid(row=3, column=3)
        Button(master, text="÷", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="light slate blue",
               command=lambda: self.action('÷')).grid(row=1, column=3)
        Button(master, text="%", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.action('%')).grid(row=5, column=5)
        Button(master, text="7", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="light slate blue",
               command=lambda: self.action('7')).grid(row=1, column=0)
        Button(master, text="8", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="light slate blue",
               command=lambda: self.action('8')).grid(row=1, column=1)
        Button(master, text="9", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="light slate blue",
               command=lambda: self.action('9')).grid(row=1, column=2)
        Button(master, text="4", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="light slate blue",
               command=lambda: self.action('4')).grid(row=2, column=0)
        Button(master, text="5", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="light slate blue",
               command=lambda: self.action('5')).grid(row=2, column=1)
        Button(master, text="6", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="light slate blue",
               command=lambda: self.action('6')).grid(row=2, column=2)
        Button(master, text="1", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="light slate blue",
               command=lambda: self.action('1')).grid(row=3, column=0)
        Button(master, text="2", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="light slate blue",
               command=lambda: self.action('2')).grid(row=3, column=1)
        Button(master, text="3", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="light slate blue",
               command=lambda: self.action('3')).grid(row=3, column=2)
        Button(master, text="0", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="light slate blue",
               command=lambda: self.action('0')).grid(row=4, column=1)
        Button(master, text=".", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="light slate blue",
               command=lambda: self.action('.')).grid(row=4, column=2)
        Button(master, text="(", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="light slate blue",
               command=lambda: self.action('(')).grid(row=2, column=4)
        Button(master, text=")", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="light slate blue",
               command=lambda: self.action(')')).grid(row=2, column=5)
        Button(master, text="√", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="light slate blue",
               command=lambda: self.evaluation('sqroot')).grid(row=3, column=4)
        Button(master, text="x²", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="light slate blue",
               command=lambda: self.evaluation('power')).grid(row=3, column=5)
        Button(master, text="xʸ", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.action('^')).grid(row=5, column=1)
        # ***************** scientific button***************************
        Button(master, text="x!", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.evaluation('fact')).grid(row=5, column=0)
        Button(master, text="¹⁄ₓ", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.evaluation('1/x')).grid(row=5, column=2)
        Button(master, text="10ˣ", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.evaluation('10^x')).grid(row=5, column=3)
        Button(master, text=chr(8731), width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.evaluation('qubicroot')).grid(row=5, column=4)
        Button(master, text="±", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="light slate blue",
               command=lambda: self.evaluation('pm')).grid(row=4, column=0)
        Button(master, text="log", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.evaluation('log')).grid(row=6, column=0)
        Button(master, text="ln", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.evaluation('ln')).grid(row=6, column=1)
        Button(master, text="e", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.action(math.e)).grid(row=6, column=2)
        Button(master, text="π", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.action(math.pi)).grid(row=6, column=3)
        Button(master, text="Rad", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.evaluation('rad')).grid(row=6, column=4)
        Button(master, text="Exp", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.evaluation('exp')).grid(row=6, column=5)

        Button(master, text="sin", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.evaluation('sin')).grid(row=7, column=0)
        Button(master, text="cos", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.evaluation('cos')).grid(row=7, column=1)
        Button(master, text="tan", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.evaluation('tan')).grid(row=7, column=2)
        Button(master, text="sin⁻¹", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.evaluation('asin')).grid(row=7, column=3)
        Button(master, text="cos⁻¹", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.evaluation('acos')).grid(row=7, column=4)
        Button(master, text="tan⁻¹", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.evaluation('atan')).grid(row=7, column=5)

        Button(master, text="sinh", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.evaluation('sinh')).grid(row=8, column=0)
        Button(master, text="cosh", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.evaluation('cosh')).grid(row=8, column=1)
        Button(master, text="tanh", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.evaluation('tanh')).grid(row=8, column=2)
        Button(master, text="sinh⁻¹", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.evaluation('asinh')).grid(row=8, column=3)
        Button(master, text="cosh⁻¹", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.evaluation('acosh')).grid(row=8, column=4)
        Button(master, text="tanh⁻¹", width=6, height=2, pady=1, font=('arial', 15, 'bold'), bg="slate blue",
               command=lambda: self.evaluation('atanh')).grid(row=8, column=5)
        # *************** coverter button*************************
        Button(master, text=('Decimal' + chr(8594) + 'Binary'), width=13, height=2, pady=1, font=('arial', 15, 'bold'),
               bg='SlateGray3', command=lambda: self.evaluation('bin')).grid(row=1, column=6)
        Button(master, text=('Decimal' + chr(8594) + 'Hex'), width=13, height=2, pady=1, font=('arial', 15, 'bold'),
               bg='SlateGray3', command=lambda: self.evaluation('hex')).grid(row=1, column=7)
        Button(master, text=('Decimal' + chr(8594) + 'Octal'), width=13, height=2, pady=1, font=('arial', 15, 'bold'),
               bg='SlateGray3', command=lambda: self.evaluation('oct')).grid(row=2, column=6)
        Button(master, text=('radian' + chr(8594) + 'degree'), width=13, height=2, pady=1, font=('arial', 15, 'bold'),
               bg='SlateGray3', command=lambda: self.evaluation('radian-degree')).grid(row=2, column=7)
        Button(master, text=('mile' + chr(8594) + 'km'), width=13, height=2, pady=1, font=('arial', 15, 'bold'),
               bg='SlateGray3', command=lambda: self.evaluation('mile-km')).grid(row=3, column=6)
        Button(master, text=('km' + chr(8594) + 'mile'), width=13, height=2, pady=1, font=('arial', 15, 'bold'),
               bg='SlateGray3', command=lambda: self.evaluation('km-mile')).grid(row=3, column=7)
        Button(master, text=('°C' + chr(8594) + '°F'), width=13, height=2, pady=1, font=('arial', 15, 'bold'),
               bg='SlateGray3', command=lambda: self.evaluation('°C-°F')).grid(row=4, column=6)
        Button(master, text=('°F' + chr(8594) + '°C'), width=13, height=2, pady=1, font=('arial', 15, 'bold'),
               bg='SlateGray3', command=lambda: self.evaluation('°F-°C')).grid(row=4, column=7)
        Button(master, text=('J' + chr(8594) + 'cal'), width=13, height=2, pady=1, font=('arial', 15, 'bold'),
               bg='SlateGray3', command=lambda: self.evaluation('j-cal')).grid(row=5, column=6)
        Button(master, text=('cal' + chr(8594) + 'J'), width=13, height=2, pady=1, font=('arial', 15, 'bold'),
               bg='SlateGray3', command=lambda: self.evaluation('cal-j')).grid(row=5, column=7)
        Button(master, text=('in' + chr(8594) + 'cm'), width=13, height=2, pady=1, font=('arial', 15, 'bold'),
               bg='SlateGray3', command=lambda: self.evaluation('in-cm')).grid(row=6, column=6)
        Button(master, text=('cm' + chr(8594) + 'in'), width=13, height=2, pady=1, font=('arial', 15, 'bold'),
               bg='SlateGray3', command=lambda: self.evaluation('cm-in')).grid(row=6, column=7)
        Button(master, text=('ft' + chr(8594) + 'm'), width=13, height=2, pady=1, font=('arial', 15, 'bold'),
               bg='SlateGray3', command=lambda: self.evaluation('ft-m')).grid(row=7, column=6)
        Button(master, text=('m' + chr(8594) + 'ft'), width=13, height=2, pady=1, font=('arial', 15, 'bold'),
               bg='SlateGray3', command=lambda: self.evaluation('m-ft')).grid(row=7, column=7)
        Button(master, text=('lb' + chr(8594) + 'kg'), width=13, height=2, pady=1, font=('arial', 15, 'bold'),
               bg='SlateGray3', command=lambda: self.evaluation('lb-kg')).grid(row=8, column=6)
        Button(master, text=('kg' + chr(8594) + 'lb'), width=13, height=2, pady=1, font=('arial', 15, 'bold'),
               bg='SlateGray3', command=lambda: self.evaluation('kg-lb')).grid(row=8, column=7)

        # bind key strokes
        self.e.bind('<Key>', lambda evt: self.keyaction(evt))


def window():
    window = Toplevel(root)
    window.resizable(width=False, height=False)
    window.geometry("330x300")

    window.title("Equation")

    lbl = Label(window, text=('Equation : ax' + chr(178) + '+bx+c=0'), font=('arial', 20, 'bold'), bg="Gray63")
    lbl.grid(row=0, column=0, columnspan=2)
    window.configure(background='Gray63')


    txta = StringVar()
    z = 0
    la = Label(window, text="a = ", font=('arial', 20, 'bold'))
    la.grid(row=1, column=0)
    lb = Label(window, text="b = ", font=('arial', 20, 'bold'))
    lb.grid(row=2, column=0)
    lc = Label(window, text="c = ", font=('arial', 20, 'bold'))
    lc.grid(row=3, column=0)
    e1 = Entry(window, bd=7, font=('arial', 15, 'bold'))
    e1.grid(row=1, column=1)
    e2 = Entry(window, bd=7, font=('arial', 15, 'bold'))
    e2.grid(row=2, column=1)
    e3 = Entry(window, bd=7, font=('arial', 15, 'bold'))
    e3.grid(row=3, column=1)
    lx = Label(window, text="x = ", font=('arial', 20, 'bold'))
    lx.grid(row=6, column=0)
    e4 = Entry(window, textvariable=txta, bd=8, font=('arial', 15, 'bold'))
    e4.grid(row=6, column=1)
    Button(window, text="Solve", font=('arial', 20, 'bold'),bg="Gray48",command=lambda: eqn()).grid(row=4, column=1)

    

    def eqn():
        x1 = 0

        a = float(e1.get())
        b = float(e2.get())
        c = float(e3.get())
        z = abs(b ** 2 - 4 * a * c)
        x1 = (b + z) / (2 * a)
        x2 = (-b + z) / (2 * a)
        x5 = "%.2f" % x1
        x6 = "%.2f" % x2
        
        txta.set(str(x5) + " or " + str(x6))


def matrix():
    matrix= Toplevel(root)
    matrix.resizable(width=False, height=False)
    matrix.geometry("600x460")

    matrix.title("Matrix")

    lbl = Label(matrix, text=('Matrix  2x2 [A] = [ a, b | c, d ]'), font=('arial', 15, 'bold'),bg="Gray63")
    lbl.grid(row=0, column=0, columnspan=2)
    matrix.configure(background="Gray63")


    txta = StringVar()
    ad2 = StringVar()
    inv1= StringVar()
    Z=0
    la1 = Label(matrix, text="Enter a ", font=('arial', 15, 'bold')).grid(row=1, column=0)
    lb1 = Label(matrix, text="Enter b ", font=('arial', 15, 'bold')).grid(row=2, column=0)
    lc1 = Label(matrix, text="Enter c ", font=('arial', 15, 'bold')).grid(row=3, column=0)
    ld1 = Label(matrix, text="Enter d ", font=('arial', 15, 'bold')).grid(row=4, column=0)
    det = Button(matrix, text="|A| = ", font=('arial', 15, 'bold'), bg="Gray38",width=7,command=lambda:det ()).grid(row=6, column=0)
    Button(matrix, text="Aᵀ = ", font=('arial', 15, 'bold'), bg="Gray40",width=7, command=lambda: ad()).grid(
        row=7, column=0)
    Button(matrix, text="A⁻¹ = ", font=('arial', 15, 'bold'), bg="Gray42",width=7, command=lambda: inv()).grid(
        row=8, column=0)
    Label(matrix, text="Solution",font=('arial', 15, 'bold'),bg="Gray63").grid(row=5, column=0, columnspan=2)

    a1 = Entry(matrix, font=('arial', 15, 'bold'))
    a1.grid(row=1, column=1)
    a2 = Entry(matrix, font=('arial', 15, 'bold'))
    a2.grid(row=2, column=1)
    b1 = Entry(matrix, font=('arial', 15, 'bold'))
    b1.grid(row=3, column=1)
    b2 = Entry(matrix, font=('arial', 15, 'bold'))
    b2.grid(row=4, column=1)
    det1= Entry(matrix, bd=6,font=('arial', 20, 'bold'), textvariable=txta, width=30)
    det1.grid(row=6, column=1)
    ad1=Entry(matrix, bd=6,font=('arial', 20, 'bold'), textvariable=ad2, width=30).grid(row=7, column=1)
    inv2=Entry(matrix, bd=6,font=('arial', 20, 'bold'), textvariable=inv1, width=30).grid(row=8, column=1)



    def det():
        X1 = 0

        A = float(a1.get())
        B = float(a2.get())
        C = float(b1.get())
        D=  float(b2.get())
        z = (A*D)-(B*C)
        X1= z
        txta.set(str(X1))

    def ad():
        X1 = 0


        A = float(a1.get())
        B = float(a2.get())
        C = float(b1.get())
        D= float(b2.get())
        ad2.set("["+str(A) +" , " +str(C)+" | "+str(B) +" , " +str(D)+"]" )

    def inv():
            A = float(a1.get())
            B = float(a2.get())
            C = float(b1.get())
            D = float(b2.get())
            z = ((A * D) - (B * C))
            X1 = A / z
            X2 = -B / z
            X3 = -C / z
            X4 = D / z
            X5=  "%.2f" % X1
            X6= "%.2f" % X2
            X7 = "%.2f" % X3
            X8 = "%.2f" % X4

            inv1.set("[" + str(X8) + " , " + str(X6) + " | " + str(X7) + " , " + str(X5) + "]")


# Main
root = tk.Tk()

root.title("Scientific Calculator")
root.configure(background='')
root.resizable(width=False, height=False)
root.geometry("494x593")


def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return


def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("494x593")


def Converter():
    root.resizable(width=False, height=False)
    root.geometry("827x593")
    root.configure(background='white')
#def simple():
  #  root.resizable(width=False, height=False)
   # root.geometry("494x330")

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Mode", menu=filemenu)
menubar.add_cascade(label="Equation", command=window)
menubar.add_cascade(label="Matrix", command=matrix)

#filemenu.add_command(label="Normal", command=simple)
filemenu.add_command(label="Standard", command=Scientific)
filemenu.add_command(label="Converter", command=Converter)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)

root.config(menu=menubar)

obj = Calc(root)  # object instantiated
root.mainloop()
