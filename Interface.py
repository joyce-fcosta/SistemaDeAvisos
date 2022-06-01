from tkinter import *
from Login import login,senha

class InterfaceSistemaDeAvisos(object):
  pass


def MostraTelaLogin():
  EsqueceElementosInicio()
  window.title("Login")
  LabelLogin.pack()
  form_Login.pack()
  LabelSenha.pack()
  form_Senha.pack()
  BotaoEntrar.pack(pady=10)
  resultado.pack()
  
def EsqueceFrameIniciar():
  frame1.pack_forget()
  frame2.pack_forget()
  frame3.pack_forget()

def MostraTelaCadastro():
  EsqueceFrameIniciar()
  EsqueceElementosInicio()
  window.geometry("800x600")
  window.title("Cadastro")
  FrameCadastro1.pack()
  FrameCadastro2.pack()
  TituloCadastro.pack(pady=40)
  SubFrameName.pack()
  SubFrameFuncao.pack(pady=15)
  NomeCadastroLabel.pack(side=LEFT,padx=4)
  NomeCadastroForms.pack(side=LEFT)
  FuncaoCadastroLabel.pack(side=LEFT)
  FuncaoCadastroforms.pack(side=LEFT)

  

def MostraTelaRelatorio():
  EsqueceElementosInicio()
  pass
"""
Função ao ser chamada esquece os elementos deixando a tela limpa 
"""
def EsqueceElementosInicio():
  lb.pack_forget()
  Botao1.pack_forget()
  Botao2.pack_forget()
  Botao3.pack_forget()


"""
Função para verificar se login e senha estão certos
"""
def Autenticacao():
    LabeLogin = form_Login.get()
    LabeSenha = form_Senha.get()

    if (LabeLogin != login) and (LabeSenha != senha):
        resultado['text'] = 'Login e Senha inválidos!'
        resultado['fg'] = 'red'

    elif LabeSenha != senha:
        resultado['text'] = 'Senha inválida!'
        resultado['fg'] = 'red'

    elif LabeLogin != login:
        resultado['text'] = 'Login inválida!'
        resultado['fg'] = 'red'

    else:
        resultado['text'] = 'Bem vindo ' + LabeLogin
        resultado['fg'] = 'green'


"""
Inicio
"""

window = Tk()
window.title("Início")
window.geometry("400x600")

"""
Grid da tela Iniciar
"""
frame1 = Frame(window,width=400,height=200)
frame1.pack()
frame2 = Frame(window,width=400,height=200)
frame2.pack()
frame3 = Frame(window,width=400,height=200)
frame3.pack()

"""
Título Iniciar
"""
lb = Label(frame1,text='Sistema de Aviso',font=('Arial',20, 'bold'))
lb.pack(pady=50)

"""
Botões da tela Iniciar
"""
Botao1 = Button(frame2,text='Login',font=('Arial',11),command=MostraTelaLogin,width=15, height=2)
Botao1.pack()

Botao2 = Button(frame2,text='Cadastro',font=('Arial',11), command=MostraTelaCadastro, width=15, height=2)
Botao2.pack(pady=10)

Botao3 = Button(frame2,text='Relátorio',font=('Arial',11), command=MostraTelaRelatorio, width=15, height=2)
Botao3.pack()


"""
Login
LabelLogin - Legenda
form_Login - Espaço para inserir informação, o login
"""
LabelLogin = Label(frame2, text='Login')
form_Login = Entry(frame2)

"""
Senha
LabelSenha - Legenda
form_Senha - Espaço para inserir informação, a senha
"""
LabelSenha = Label(frame2, text='Senha')
form_Senha = Entry(frame2, show='*')  #Escondendo a senha ao ser digitada

"""
Botão
"""
BotaoEntrar = Button(frame2, text='Entrar', command=Autenticacao)

"""
Mensagem instrutiva/saudação
"""
resultado = Label(frame2, text='', fg='blue')


"""
Tela Cadastro
"""
FrameCadastro1 = Frame(window,width=800,height=100)
FrameCadastro2 = Frame(window,width=800,height=500)
TituloCadastro = Label(FrameCadastro1,text="Cadastro", font=('Arial', 20, 'bold'))

SubFrameName = Frame(FrameCadastro2)
SubFrameFuncao = Frame(FrameCadastro2)

NomeCadastroLabel = Label(SubFrameName,text="Nome") 
NomeCadastroForms = Entry(SubFrameName,width=40) 

FuncaoCadastroLabel = Label(SubFrameFuncao,text="Função") 
FuncaoCadastroforms = Entry(SubFrameFuncao, width=25)



window.mainloop()

