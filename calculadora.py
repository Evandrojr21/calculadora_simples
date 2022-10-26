from tkinter import *
from tkinter import ttk

#cores pegas no colour picker
cor_fundo = "#343b32" # preto
cor_2 = "#ffffff" # branco
cor_3 = "#384cc9" # azul
cor_4 = "#49524c" #cinza
cor_5 = "#ff7300" #laranja

# criar janela
display = Tk()
display.title("projeto calculadora")
display.geometry("235x310")
display.config(bg=cor_fundo)

#divisão da tela/ frames
frame_tela = Frame(display, width=235, height=50, bg=cor_3)
frame_tela.grid(row=0, column= 0)

frame_inferior = Frame(display, width=235, height=268)
frame_inferior.grid(row=1, column= 0)

#criando label
valor_text = StringVar()

app_label = Label(frame_tela, textvariable= valor_text, width=16, height=2, padx= 7, relief=FLAT, anchor= "e", justify= RIGHT, font= ('Ivy 18 '), bg= cor_3, fg= cor_2 )
app_label.place(x=0, y=0)

# variavel todos valores
valores_totais = ''

#criando função
def entrada_valores(event):

    global valores_totais

    valores_totais = valores_totais + str(event)

    #passando valor para tela
    valor_text.set(valores_totais)

#funçao calcular
def calcular():
    global valores_totais
    result = eval(valores_totais)
    print(result)

    valor_text.set(str(result))

# funçao limpár tela
def limpar_tela():
    global valores_totais
    valores_totais = ""
    valor_text.set("")


#criando botões
b_1 = Button(frame_inferior, command= limpar_tela,text= "C", width=11, height=2, bg= cor_4, font= ('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_1.place(x=0,y=0)
b_2 = Button(frame_inferior, command= lambda: entrada_valores('%'),text= "%", width=5, height=2, bg= cor_4, font= ('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_2.place(x=118,y=0)
b_3 = Button(frame_inferior,command= lambda: entrada_valores('/'), text= "/", width=5, height=2, bg= cor_5, fg= cor_2 , font= ('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_3.place(x=177,y=0)

b_4 = Button(frame_inferior,command= lambda: entrada_valores('7'), text= "7", width=5, height=2, bg= cor_4, font= ('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_4.place(x=0,y=52)
b_5 = Button(frame_inferior,command= lambda: entrada_valores('8'), text= "8", width=5, height=2, bg= cor_4, font= ('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_5.place(x=59,y=52)
b_6 = Button(frame_inferior, command= lambda: entrada_valores('9'),text= "9", width=5, height=2, bg= cor_4, font= ('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_6.place(x=118,y=52)
b_7 = Button(frame_inferior, command= lambda: entrada_valores('*'),text= "*", width=5, height=2, bg= cor_5, font= ('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_7.place(x=177,y=52)

b_8 = Button(frame_inferior,command= lambda: entrada_valores('4'), text= "4", width=5, height=2, bg= cor_4, font= ('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_8.place(x=0,y=104)
b_9 = Button(frame_inferior, command= lambda: entrada_valores('5'),text= "5", width=5, height=2, bg= cor_4, font= ('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_9.place(x=59,y=104)
b_10 = Button(frame_inferior, command= lambda: entrada_valores('6'),text= "6", width=5, height=2, bg= cor_4, font= ('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_10.place(x=118,y=104)
b_11 = Button(frame_inferior, command= lambda: entrada_valores('-'),text= "-", width=5, height=2, bg= cor_5, font= ('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_11.place(x=177,y=104)

b_12 = Button(frame_inferior, command= lambda: entrada_valores('1'),text= "1", width=5, height=2, bg= cor_4, font= ('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_12.place(x=0,y=156)
b_13 = Button(frame_inferior,command= lambda: entrada_valores('2'), text= "2", width=5, height=2, bg= cor_4, font= ('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_13.place(x=59,y=156)
b_14 = Button(frame_inferior,command= lambda: entrada_valores('3'), text= "3", width=5, height=2, bg= cor_4, font= ('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_14.place(x=118,y=156)
b_15 = Button(frame_inferior, command= lambda: entrada_valores('+'),text= "+", width=5, height=2, bg= cor_5, font= ('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_15.place(x=177,y=156)

b_16 = Button(frame_inferior,command= lambda: entrada_valores('0'), text= "0", width=11, height=2, bg= cor_4, font= ('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_16.place(x=0,y=208)
b_17 = Button(frame_inferior,command= lambda: entrada_valores('.'), text= ".", width=5, height=2, bg= cor_4, font= ('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_17.place(x=118,y=208)
b_18 = Button(frame_inferior,command= calcular, text= "=", width=5, height=2, bg= cor_5, fg= cor_2 , font= ('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_18.place(x=177,y=208)


display.mainloop()



