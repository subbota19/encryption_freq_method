from tkinter import *
from  tkinter import messagebox
from collections import Counter
import copy

class Main():
    def __init__(self,root):
        Design_window(root)

class Design_window():

    def __init__(self,root):

        self.frequency = {
            'E':12.31, 'T':9.59, 'A':8.05, 'O':7.94, 'N':7.19, 'I':7.18, 'S':6.59, 'R':6.03, 'H':5.14, 'L':4.03,
            'D':3.65, 'C':3.20, 'U':3.10,'P':2.29, 'F':2.28, 'M':2.25, 'W':2.03, 'Y':1.88, 'B':1.62, 'G':1.61,
            'V':0.93, 'K':0.52, 'Q':0.20, 'X':0.20, 'J':0.10,'Z':0.09}
        self.frequency_letters=[x for x in self.frequency]

        self.alphabet =sorted([x for x in self.frequency.keys()],key=str.lower)

        self.number = [i + 1 for i in range(26)]
        self.dict_alphabet = dict(zip(self.alphabet, self.number))


        self.name=Label(root, text="Input text", font="Arial 20").place(x=170,y=5)
        self.input_text = Text(width=55,height=10)
        self.input_text.place(x=30,y=50)

        self.key = Label(root, text="Input key:", font="Arial 20").place(x=10,y=220)
        self.input_key = Entry(root)
        self.input_key.place(x=150,y=235)


        self.output_1 = Label(root, text="Text use frequency method", font="Arial 20").place(x=600, y=10)

        self.input_req = Text(root, width=55, height=10)
        self.input_req.place(x=500, y=50)

        self.letter = Label(root, text="Change letter:", font="Arial 16").place(x=500, y=220)
        self.input_change = Entry(root, width=10)
        self.input_change.place(x=645, y=225)

        self.letter = Label(root, text="on:", font="Arial 16").place(x=720, y=220)
        self.input_on = Entry(root, width=10)
        self.input_on.place(x=770, y=225)

        self.button_ex = Button(root, text='Execute', font="Arial 14",
                               command=self.change_letter, width=40, height=3).place(x=500, y=280)

        self.list_analysis = []

        self.button_1 = Button(root, text='Execute',font="Arial 22" , command=self.execute_buttom_1, width=12,
                               height=2).place(x=10,y=280)

        self.button_2 = Button(root, text='Exit',font="Arial 22" , command=root.destroy, width=12,
                               height=2).place(x=250,y=280)

    def change_letter(self):

        ch_letter = self.input_change.get()
        on_letter = self.input_on.get()

        text=[x for x in self.input_req.get(1.,END)]

        list_ch_letter = []
        list_on_letter = []
        for i, item in enumerate(text):
            if ch_letter == item:
                list_ch_letter.append(i)
            if on_letter == item:
                list_on_letter.append(i)

        for i in list_ch_letter:
            text[i] = on_letter

        for i in list_on_letter:
            text[i] = ch_letter

        self.input_req.delete(1.0, END)
        self.input_req.insert(1.0, ''.join(text))


    def execute_buttom_1(self):

        Create_add_window(' '.join(self.func_execute_crypt()), 'Text after cryption')
        self.input_req.insert(1.0,self.func_execute_frequency_method())

    def func_execute_crypt(self):
            mod = 26
            text = (self.input_text.get(1., END)).upper()
            key = self.input_key.get()

            text_after_crypt=[]

            list_with_text=(text.replace('\n',' ')).split(' ')
            for i in range(len(list_with_text)):
               word = []
               for j in list_with_text[i]:
                     math = (self.alphabet.index(j)+1) * int(key) % int(mod)
                     word.append(self.alphabet[math - 1])
               text_after_crypt.append(''.join(word))
            text_after_crypt.pop()
            return text_after_crypt

    def func_execute_frequency_method(self):

            text_after_crypt=' '.join(self.func_execute_crypt())
            total=len(text_after_crypt.replace(' ',''))
            ordered_vac=Counter(text_after_crypt.replace(' ',''))
            for i,item in enumerate(ordered_vac):
                ordered_vac[item]/=total*0.01

            for i,item in enumerate(self.frequency):
                if ordered_vac[item]:
                    pass
                else:
                    ordered_vac[item]=0

            ordered_vac={x: round(y, 2) for x, y in ordered_vac.items()}
            self.list_analysis = [list(x) for x in ordered_vac.items()]
            self.list_analysis.sort(key=lambda number: number[1], reverse=True)

            Create_add_window(self.list_analysis,'Analysis my alphabet')

            list_with_letters = [x for y in self.list_analysis for x in y[0]]

            # analysis date

            frequency_text = []
            print(text_after_crypt)
            for i, item in enumerate(text_after_crypt):
                    if item == ' ':
                        frequency_text.append(' ')
                    else:
                        frequency_text.append(self.frequency_letters[list_with_letters.index(item)])

            return ''.join(frequency_text)



class Create_add_window(Design_window):
    def __init__(self,text,design):

        self.new_window=Tk()
        self.new_window.geometry("500x300")
        self.new_window.title("Add_window")

        self.text=text

        outpt_1=Label(self.new_window, text=design, font="Arial 20").place(x=125,y=20)

        self.input_text=Text(self.new_window,width=55,height=10)
        self.input_text.insert(1.,self.text)
        self.input_text.place(x=35,y=60)

    def __call__(self):

        self.letter = Label(self.new_window, text="Change letter:", font="Arial 16").place(x=10, y=230)
        self.input_1 = Entry(self.new_window,width=10)
        self.input_1.place(x=160, y=235)

        self.letter = Label(self.new_window, text="on:", font="Arial 16").place(x=230, y=230)
        self.input_2 = Entry(self.new_window,width=10)
        self.input_2.place(x=280, y=235)

if __name__=="__main__":
    root_1=Tk()
    win_1=Main(root_1)
    root_1.title("First_window")
    root_1.geometry("1000x450")
    root_1.mainloop()