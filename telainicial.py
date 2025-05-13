import tkinter as tk


def mostrar_mensagem(titulo, mensagem):
    msg = tk.Tk()
    msg.title(titulo)
    msg.geometry("700x700")
    tk.Label(msg, text=mensagem).pack(padx=45, pady=30)
    tk.Button(msg, text="OK", command=msg.destroy).pack(pady=15)


def abrir_cadastro():
    nova_janela = tk.Tk()
    nova_janela.title("Cadastro")

    tk.Label(nova_janela, text="Nome:").pack()
    nome = tk.Entry(nova_janela)
    nome.pack()

    tk.Label(nova_janela, text="Email:").pack()
    email = tk.Entry(nova_janela)
    email.pack()

    def salvar():
        mostrar_mensagem("Cadastro", "Cadastro feito com sucesso!")

    tk.Button(nova_janela, text="Cadastrar", command=salvar).pack()


def abrir_agendamento():
    nova_janela = tk.Tk()
    nova_janela.title("Agendamento")

    tk.Label(nova_janela, text="Data:").pack()
    data = tk.Entry(nova_janela)
    data.pack()

    tk.Label(nova_janela, text="Hora:").pack()
    hora = tk.Entry(nova_janela)
    hora.pack()

    def agendar():
        mostrar_mensagem("Agendamento", "Agendamento feito com sucesso!")

    tk.Button(nova_janela, text="Agendar", command=agendar).pack()


def abrir_consultoria():
    nova_janela = tk.Tk()
    nova_janela.title("Consultoria")

    tk.Label(nova_janela, text="Descreva sua dúvida:").pack()
    texto = tk.Text(nova_janela, height=45, width=40)
    texto.pack()

    def enviar():
        mostrar_mensagem("Consultoria", "Pedido de consultoria enviado!")

    tk.Button(nova_janela, text="Enviar", command=enviar).pack()


janela_principal = tk.Tk()
janela_principal.title("Sistema de Serviços")

tk.Label(janela_principal, text="Escolha uma opção:", font=("Arial", 45)).pack(pady=20)

tk.Button(janela_principal, text="Cadastro de Usuário", width=70, command=abrir_cadastro).pack(pady=15)
tk.Button(janela_principal, text="Agendamento",width=70, command=abrir_agendamento).pack(pady=15)
tk.Button(janela_principal, text="Consultoria de Serviço", width=70, command=abrir_consultoria).pack(pady=15)

janela_principal.mainloop()