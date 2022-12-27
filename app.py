# Importações
from tkinter import *
import customtkinter
from PIL import Image, ImageTk


customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')


# Janela Principal
janela = customtkinter.CTk()
janela.title('Calculadora de IMC')
janela.geometry('500x600')
janela.iconbitmap(r'Imagens\icone_janela.ico')
janela.resizable(width=False, height=False)


def calculo_imc():
    '''Faz o calculo do IMC'''
    peso = float(entry_peso.get())
    altura = float(entry_altura.get())
    calculo = peso / (altura ** 2)
    resultado = calculo 
    if (resultado < 18.5):
        label_resultado.configure(text='{:.1f}'.format(resultado), text_color='#46ebff')
    elif (resultado > 18.5) and (resultado <= 24.9):
        label_resultado.configure(text='{:.1f}'.format(resultado), text_color='#16f55a')
    elif (resultado > 25.0) and (resultado <= 29.9):
        label_resultado.configure(text='{:.1f}'.format(resultado), text_color='#f5f216')
    elif (resultado > 30.0) and (resultado <= 39.9):
        label_resultado.configure(text='{:.1f}'.format(resultado),text_color='#f89534')
    else:
        label_resultado.configure(text='{:.1f}'.format(resultado), text_color='#fa3e3e')


# Regua IMC
regua_peso = ImageTk.PhotoImage(Image.open(r'D:\Projetos\Calculadora_IMC_TMB\Imagens\fundo2.png'))
label_regua = Label(janela, image=regua_peso, bd=0)
label_regua.place(x=0, y=0)


# Labels e Entries 
label_peso = customtkinter.CTkLabel(janela, text='Peso:', font=('Helvetica', 16), bg_color = '#04122b')
label_peso.place(x=230, y=145)
entry_peso = customtkinter.CTkEntry(master=janela,
width = 200,
height = 30,
border_width = 1,
corner_radius = 10,)
entry_peso.place(x=150, y=180)

label_altura = customtkinter.CTkLabel(janela, text='Altura:', font=('Helvetica', 16), bg_color = '#04122b')
label_altura.place(x=230, y=225)
entry_altura = customtkinter.CTkEntry(master=janela,
width = 200,
height = 30,
border_width = 1,
corner_radius = 10)
entry_altura.place(x=150, y=260)

label_resultado = customtkinter.CTkLabel(janela, text='', bg_color='#04122b', font=('Helvetica', 45))
label_resultado.place(x=208, y=460)


def limpar_entry():
    '''Limpa as entries e label do resultado'''
    entry_peso.delete(0, END)
    entry_altura.delete(0, END)
    label_resultado.configure(text='')


# Botões
botao_calcular = customtkinter.CTkButton(janela, width=200, height=33, text='Calcular IMC', fg_color='#00BFFF', hover_color='#4169E1', command=calculo_imc)
botao_calcular.place(x=150, y=330)

botao_limpar = customtkinter.CTkButton(janela, width=200, height=33, text='Limpar', fg_color='#B22222', hover_color='#8B0000',command = limpar_entry)
botao_limpar.place(x=150, y=380)


janela.mainloop()
