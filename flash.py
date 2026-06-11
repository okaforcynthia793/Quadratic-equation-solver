import tkinter as tk

root = tk.Tk()
root.title('Quadratic Equation solver')
root.geometry('400x350')
root.config(bg='#E2B3FF')

coffa = tk.StringVar(value='0.0')
coffb = tk.StringVar(value='0.0')
coffc = tk.StringVar(value='0.0')
result = tk.StringVar(value='No computation yet')

def solveEquation():
        a = coffa.get()
        b = coffb.get()
        c = coffc.get()
        try:
            a = float(a)
            b = float(b)
            c = float(c)
        except ValueError:
            result.set('Invalid numeric entry value')
            return
        if a == 0:
            result.set("Coefficient 'a' cannot be zero.")
            return
        
        discriminant = b**2 - 4*a*c

        if discriminant > 0:
            x1 = (-b + discriminant**0.5) / (2*a)
            x2 = (-b - discriminant**0.5) / (2*a)
            result.set(
                f'the roots are real and distinct\n'
                f'x1 = {x1:.2f}\n'
                f'x2 = {x2:.2f}'
            )
        elif discriminant == 0:
            x = -b / (2*a)
            result.set(
                f'the roots are real and repeated\n'
                f'x = {x:.2f}'
            )
        else:
            real = -b / (2*a)
            imag = ((-discriminant)**0.5) / (2*a)
            result.set(
                f'the roots are real and complex\n'
                f'x1 = {real:.2f} + {imag:.2f}j\n'
                f'x2 = {real:.2f} - {imag:.2f}j'
            )
def resetEquation():
        coffa.set('0.0')
        coffb.set('0.0')
        coffc.set('0.0')
        result.set('No computation yet')

headerLabel = tk.Label(root, text='Quadratic Equation Solver', font=('Avenir', 14, 'bold'), bg='#E2B3FF')
headerLabel.pack(pady=(10, 0))
subtitleLabel = tk.Label(root, text='ax\u00b2 + bx + c = 0' ,font=('Avenir', 11), bg='#E2B3FF', fg='grey')
subtitleLabel.pack(pady=(0, 5))

entriesFrame = tk.Frame(root, bg=root['bg'])
entriesFrame.pack()

aLabel = tk.Label(entriesFrame, text='Coeffficient a: ', font=('Avenir', 12), bg=root['bg'])
aLabel.grid(row=0, column=0, padx=5, pady=10)
aEntry = tk.Entry(entriesFrame, font=('Avenir', 12), textvariable=coffa)
aEntry.grid(row=0, column=1, padx=5, pady=10)

bLabel = tk.Label(entriesFrame, text='Coeffficient b: ', font=('Avenir', 12), bg=root['bg'])
bLabel.grid(row=1, column=0, padx=5, pady=10)
bEntry = tk.Entry(entriesFrame, font=('Avenir', 12), textvariable=coffb)
bEntry.grid(row=1, column=1, padx=5, pady=10)

cLabel = tk.Label(entriesFrame, text='Coeffficient c: ', font=('Avenir', 12), bg=root['bg'])
cLabel.grid(row=2, column=0, padx=5, pady=10)
cEntry = tk.Entry(entriesFrame, font=('Avenir', 12), textvariable=coffc)
cEntry.grid(row=2, column=1, padx=5, pady=10)

buttonsFrame = tk.Frame(root, bg=root['bg'])
buttonsFrame.pack()

solveBtn = tk.Button(buttonsFrame, text='Solve Equation', font=('Avenir', 12, 'bold'), width=12, command=solveEquation)
solveBtn.pack(side='left', padx=5, pady=10)

resetBtn = tk.Button(buttonsFrame, text='Reset', font=('Avenir', 12, 'bold'), width=12,command=resetEquation)
resetBtn.pack(side='left', padx=5, pady=10)

resultLabel = tk.Label(root, font=('Avenir', 12), bg=root['bg'], textvariable=result, justify='left')
resultLabel.pack(padx=5, pady=10)

root.mainloop()
