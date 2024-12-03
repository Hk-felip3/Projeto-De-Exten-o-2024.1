import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

logo_image = None  # Definindo a variável global logo_image



def open_login_page():
    # Cria uma nova janela para a tela de login
    login_window = tk.Toplevel()
    login_window.title("Login")

    # Define as dimensões da janela
    width, height = 350, 600

    # Configuração do fundo da janela
    bg_color = '#FFFFFF'
    canvas = tk.Canvas(login_window, width=width, height=height, bg=bg_color)
    canvas.pack()

    # Adiciona o título "Login"
    title_label = tk.Label(login_window, text="Login", fg="black", bg=bg_color, font=("Arial", 14))
    title_label.place(relx=0.5, rely=0.05, anchor="n")

    # Campos de entrada para usuário e senha
    username_label = tk.Label(login_window, text="Usuário:", fg="black", bg=bg_color, font=("Arial", 12))
    username_label.place(relx=0.2, rely=0.3, anchor="e")
    username_entry = tk.Entry(login_window)
    username_entry.place(relx=0.3, rely=0.3, anchor="w")

    password_label = tk.Label(login_window, text="Senha:", fg="black", bg=bg_color, font=("Arial", 12))
    password_label.place(relx=0.2, rely=0.4, anchor="e")
    password_entry = tk.Entry(login_window, show="*")
    password_entry.place(relx=0.3, rely=0.4, anchor="w")

    # Botão de entrar
    login_button = tk.Button(login_window, text="Entrar", width=10, command=lambda: verify_login(username_entry.get(), password_entry.get()))
    login_button.place(relx=0.5, rely=0.6, anchor="center")

def verify_login(username, password):
    # Verificação de login
    if username == "admin" and password == "admin":
        messagebox.showinfo("Login", "Login bem-sucedido!")
        open_area_aluno()
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos")

def open_area_aluno():
    # Cria uma nova janela para a área do aluno
    area_aluno_window = tk.Toplevel()
    area_aluno_window.title("Área do Aluno")

    # Define as dimensões da janela
    width, height = 350, 600

    # Configuração do fundo da janela
    bg_color = '#FFFFFF'
    canvas = tk.Canvas(area_aluno_window, width=width, height=height, bg=bg_color)
    canvas.pack()

    # Adiciona o título "Central Aluno"
    title_label = tk.Label(area_aluno_window, text="Central Aluno", fg="black", bg=bg_color, font=("Arial", 14))
    title_label.place(relx=0.05, rely=0.05, anchor="nw")

    # Adiciona o nome do aluno
    aluno_nome_label = tk.Label(area_aluno_window, text="Nome do Aluno: João Silva", fg="black", bg=bg_color,
                                font=("Arial", 12))
    aluno_nome_label.place(relx=0.05, rely=0.1, anchor="nw")

    # Adiciona a seção "Sistema de Presença e Ficha de Treino"
    presenca_label = tk.Label(area_aluno_window, text="Sistema de Presença:", fg="black", bg=bg_color,
                              font=("Arial", 12))
    presenca_label.place(relx=0.05, rely=0.2, anchor="nw")

    # Adiciona o botão de sistema de presença
    presenca_button = tk.Button(area_aluno_window, text="Presença", width=10,
                                command=lambda: marcar_presenca(presenca_text))
    presenca_button.place(relx=0.2, rely=0.2, anchor="nw")

    # Adiciona a ficha de treino
    ficha_treino_label = tk.Label(area_aluno_window, text="Ficha de Treino:", fg="black", bg=bg_color,
                                  font=("Arial", 12))
    ficha_treino_label.place(relx=0.05, rely=0.3, anchor="nw")
    ficha_treino_text = tk.Text(area_aluno_window, width=25, height=5)
    ficha_treino_text.place(relx=0.05, rely=0.35, anchor="nw")
    ficha_treino_text.insert(tk.END, "Aqui está a ficha de treino")

    # Adiciona os botões de consultoria e feedback
    consultoria_button = tk.Button(area_aluno_window, text="Consultoria", width=15,
                                   command=lambda: messagebox.showinfo("Consultoria",
                                                                       "Funcionalidade em desenvolvimento"))
    consultoria_button.place(relx=0.3, rely=0.8, anchor="center")

    feedback_button = tk.Button(area_aluno_window, text="Feedback", width=15,
                                command=lambda: messagebox.showinfo("Feedback", "Funcionalidade em desenvolvimento"))
    feedback_button.place(relx=0.7, rely=0.8, anchor="center")


def marcar_presenca(presenca_text):
    # Lógica para marcar presença
    presenca_text.insert(tk.END, "\nSua resposta foi enviada!")
def open_professor_login():
    # Cria uma nova janela para o login do professor
    professor_login_window = tk.Toplevel()
    professor_login_window.title("Login do Professor")

    # Define as dimensões da janela de login do professor
    width, height = 350, 600

    # Configuração do fundo da janela (degradê do preto para o cinza)
    bg_color = '#000000'
    canvas = tk.Canvas(professor_login_window, width=width, height=height, bg=bg_color)
    canvas.pack()

    # Carrega e redimensiona a imagem do logo
    original_image = Image.open("logo.png")
    scaled_image = original_image.resize((int(width * 0.8), int(height * 0.3)))
    logo_image = ImageTk.PhotoImage(scaled_image)

    # Adiciona o logo à janela
    logo_label = tk.Label(professor_login_window, image=logo_image, bg=bg_color)
    logo_label.place(relx=0.5, rely=0.15, anchor="center")

    # Adiciona o rótulo "Login do Professor" mais acima
    login_label = tk.Label(professor_login_window, text="Login do Professor", fg="white", bg=bg_color, font=("Arial", 16))
    login_label.place(relx=0.5, rely=0.05, anchor="center")

    # Adiciona campos de entrada para nome, email e senha
    campos = ["Nome", "Email", "Senha"]
    default_values = ["Professor Teste", "professor@teste.com", "senha123"]
    entries = []
    for i, campo in enumerate(campos):
        label = tk.Label(professor_login_window, text=campo, fg="white", bg=bg_color, font=("Arial", 12))
        label.place(relx=0.1, rely=0.5 + i * 0.1, anchor="w")
        entry = tk.Entry(professor_login_window)
        entry.insert(0, default_values[i])
        entry.place(relx=0.3, rely=0.5 + i * 0.1, anchor="w")
        entries.append(entry)

    # Adiciona o botão "Entrar"
    entrar_btn = tk.Button(professor_login_window, text="Entrar", width=10, command=lambda: verify_login(entries, professor_login_window))
    entrar_btn.place(relx=0.5, rely=0.85, anchor="center")

def verify_login(entries, professor_login_window):
    # Verifica se a senha está correta
    if entries[2].get() == "senha123":
        # Fecha a janela de login do professor
        professor_login_window.destroy()
        # Abre a área administrativa
        open_admin_area()
    else:
        # Exibe uma mensagem de erro se a senha estiver incorreta
        error_label = tk.Label(professor_login_window, text="Senha incorreta", fg="red", bg='#000000', font=("Arial", 12))
        error_label.place(relx=0.5, rely=0.95, anchor="center")

def open_admin_area():
    # Cria uma nova janela para a área administrativa
    admin_area_window = tk.Toplevel()
    admin_area_window.title("Área Administrativa")

    # Define as dimensões da janela
    width, height = 350, 600

    # Configuração do fundo da janela
    bg_color = '#FFFFFF'
    canvas = tk.Canvas(admin_area_window, width=width, height=height, bg=bg_color)
    canvas.pack()

    # Carrega e redimensiona a imagem do logo
    original_image = Image.open("logo.png")
    scaled_image = original_image.resize((int(width * 0.1), int(height * 0.1)))
    logo_image = ImageTk.PhotoImage(scaled_image)

    # Adiciona a logo no canto inferior esquerdo
    logo_label = tk.Label(admin_area_window, image=logo_image, bg=bg_color)
    logo_label.place(relx=0.0, rely=1.0, anchor="sw")

    # Adiciona o título "Área Administrativa"
    title_label = tk.Label(admin_area_window, text="Área Administrativa", fg="black", bg=bg_color, font=("Arial", 14))
    title_label.place(relx=0.5, rely=0.05, anchor="n")

    # Adiciona o nome da professora Rebeca
    teacher_label = tk.Label(admin_area_window, text="Professor(a)- Rebeca Moreira", fg="black", bg=bg_color, font=("Arial", 12))
    teacher_label.place(relx=0.5, rely=0.1, anchor="n")

    # Adiciona os botões
    button_width = 20
    button_height = 2
    student_button = tk.Button(admin_area_window, text="Alunos", width=button_width, height=button_height, command=open_student_window)
    student_button.place(relx=0.5, rely=0.3, anchor="center")

    feedback_button = tk.Button(admin_area_window, text="Feedback", width=button_width, height=button_height, command=open_feedback_window)
    feedback_button.place(relx=0.5, rely=0.4, anchor="center")

    cadastrar_button = tk.Button(admin_area_window, text="Cadastrar Alunos", width=button_width, height=button_height, command=open_registration_window)
    cadastrar_button.place(relx=0.5, rely=0.6, anchor="center")

    consulting_button = tk.Button(admin_area_window, text="consultoria ", width=button_width, height=button_height, command=open_registration_window)
    consulting_button.place(relx=0.5, rely=0.8, anchor="center")
def open_student_window():
    # Lista de alunos cadastrados (exemplo)
    alunos_cadastrados = [
        {"Nome": "Guilherme Souza Pereira", "Email": "guilherme@example.com", "Telefone": "123456789", "Idade": "25", "Senha": "senha123", "Presenca": 100},
        {"Nome": "Maria Silva", "Email": "maria@example.com", "Telefone": "987654321", "Idade": "30", "Senha": "maria456", "Presenca": 95},
        {"Nome": "João Oliveira", "Email": "joao@example.com", "Telefone": "999888777", "Idade": "28", "Senha": "joao789", "Presenca": 85},
        # Adicione mais alunos conforme necessário
    ]

    # Cria uma nova janela para exibir os alunos cadastrados
    student_window = tk.Toplevel()
    student_window.title("Alunos Cadastrados")

    # Define as dimensões da janela
    width, height = 450, 600

    # Configuração do fundo da janela
    bg_color = '#FFFFFF'
    canvas = tk.Canvas(student_window, width=width, height=height, bg=bg_color)
    canvas.pack()

    # Adiciona o título "Alunos Cadastrados"
    title_label = tk.Label(student_window, text="Alunos Cadastrados", fg="black", bg=bg_color, font=("Arial", 14))
    title_label.place(relx=0.5, rely=0.05, anchor="n")

    # Posição inicial para exibir os alunos
    initial_y = 0.1

    # Itera sobre os alunos cadastrados e exibe suas informações
    for aluno in alunos_cadastrados:
        # Exibe as informações do aluno
        aluno_info = f"Nome: {aluno['Nome']}\nEmail: {aluno['Email']}\nTelefone: {aluno['Telefone']}\nIdade: {aluno['Idade']}\nSenha: {aluno['Senha']}\nPresença: {aluno['Presenca']}%"
        aluno_label = tk.Label(student_window, text=aluno_info, fg="black", bg=bg_color, font=("Arial", 12), justify="left")
        aluno_label.place(relx=0.5, rely=initial_y, anchor="n")
        initial_y += 0.2  # Ajusta a posição para o próximo aluno

        # Exibe o campo para presença (simulado)
        presenca_label = tk.Label(student_window, text="Presença:", fg="black", bg=bg_color, font=("Arial", 12))
        presenca_label.place(relx=0.25, rely=initial_y, anchor="e")
        presenca_entry = tk.Entry(student_window, width=5)
        presenca_entry.insert(0, aluno['Presenca'])  # Define a presença inicial do aluno
        presenca_entry.place(relx=0.3, rely=initial_y, anchor="w")

        # Exibe a prescrição do treino (simulado)
        prescricao_label = tk.Label(student_window, text="Prescrição do Treino:", fg="black", bg=bg_color, font=("Arial", 12))
        prescricao_label.place(relx=0.7, rely=initial_y, anchor="e")
        prescricao_entry = tk.Entry(student_window, width=20)
        prescricao_entry.place(relx=0.75, rely=initial_y, anchor="w")

        initial_y += 0.2  # Ajusta a posição para o próximo aluno


def open_feedback_window():
    # Função para gerar o relatório PDF
    def gerar_relatorio():
        # Lógica para gerar o relatório PDF
        # Aqui você pode criar um relatório em PDF com os dados necessários, como o total de alunos e o total de feedbacks enviados

        # Exemplo simples: exibindo uma mensagem
        messagebox.showinfo("Relatório Gerado", "Relatório PDF gerado com sucesso!")

    # Cria uma nova janela para o feedback
    feedback_window = tk.Toplevel()
    feedback_window.title("Feedback")

    # Define as dimensões da janela
    width, height = 350, 600

    # Configuração do fundo da janela
    bg_color = '#FFFFFF'
    canvas = tk.Canvas(feedback_window, width=width, height=height, bg=bg_color)
    canvas.pack()

    # Adiciona o título "Feedback"
    title_label = tk.Label(feedback_window, text="Feedback", fg="black", bg=bg_color, font=("Arial", 14))
    title_label.place(relx=0.5, rely=0.05, anchor="n")

    # Aqui você pode adicionar widgets para exibir e coletar feedback dos usuários

    # Exibir total de alunos
    total_alunos_label = tk.Label(feedback_window, text="Total de Alunos: 100", fg="black", bg=bg_color, font=("Arial", 12))
    total_alunos_label.place(relx=0.5, rely=0.2, anchor="n")

    # Exibir total de feedbacks enviados
    total_feedbacks_label = tk.Label(feedback_window, text="Total de Feedbacks: 50", fg="black", bg=bg_color, font=("Arial", 12))
    total_feedbacks_label.place(relx=0.5, rely=0.3, anchor="n")

    # Botão para gerar relatório PDF
    relatorio_button = tk.Button(feedback_window, text="Gerar Relatório PDF", width=20, command=gerar_relatorio)
    relatorio_button.place(relx=0.5, rely=0.4, anchor="n")

def open_registration_window():
    def cadastrar_aluno():
        # Lógica para cadastrar o aluno
        # Aqui você pode pegar os valores inseridos nos campos de entrada e realizar o cadastro
        aluno_nome = nome_entry.get()
        aluno_email = email_entry.get()
        aluno_telefone = telefone_entry.get()
        aluno_idade = idade_entry.get()
        aluno_senha = senha_entry.get()
        # Aqui você pode adicionar a lógica de cadastro, por exemplo, salvar em um banco de dados

        # Após o cadastro, fechar a janela de cadastro e abrir a área de alunos
        registration_window.destroy()
        open_area_aluno()

    # Cria uma nova janela para o cadastro de alunos
    registration_window = tk.Toplevel()
    registration_window.title("Cadastro de Alunos")

    # Define as dimensões da janela
    width, height = 350, 600

    # Configuração do fundo da janela
    bg_color = '#FFFFFF'
    canvas = tk.Canvas(registration_window, width=width, height=height, bg=bg_color)
    canvas.pack()

    # Adiciona o título "Cadastro de Alunos"
    title_label = tk.Label(registration_window, text="Cadastro de Alunos", fg="black", bg=bg_color, font=("Arial", 14))
    title_label.place(relx=0.5, rely=0.05, anchor="n")

    # Adiciona campos de entrada para nome, email, telefone, idade e senha
    campos = ["Nome", "Email", "Telefone", "Idade", "Senha"]
    entries = []
    for i, campo in enumerate(campos):
        label = tk.Label(registration_window, text=campo+":", fg="black", bg=bg_color, font=("Arial", 12))
        label.place(relx=0.25, rely=0.2 + i * 0.1, anchor="e")
        entry = tk.Entry(registration_window)
        entry.place(relx=0.3, rely=0.2 + i * 0.1, anchor="w")
        entries.append(entry)

    # Adiciona o botão "Cadastrar"
    cadastrar_btn = tk.Button(registration_window, text="Cadastrar", width=10, command=cadastrar_aluno)
    cadastrar_btn.place(relx=0.5, rely=0.7, anchor="center")


    # Cria uma nova janela para o cadastro de alunos
    registration_window = tk.Toplevel()
    registration_window.title("Cadastro de Alunos")

    # Define as dimensões da janela
    width, height = 350, 600

    # Configuração do fundo da janela
    bg_color = '#FFFFFF'
    canvas = tk.Canvas(registration_window, width=width, height=height, bg=bg_color)
    canvas.pack()

    # Adiciona o título "Cadastro de Alunos"
    title_label = tk.Label(registration_window, text="Cadastro de Alunos", fg="black", bg=bg_color, font=("Arial", 14))
    title_label.place(relx=0.5, rely=0.05, anchor="n")

    # Adiciona campos de entrada
    nome_label = tk.Label(registration_window, text="Nome:", fg="black", bg=bg_color, font=("Arial", 12))
    nome_label.place(relx=0.1, rely=0.15, anchor="w")
    nome_entry = tk.Entry(registration_window)
    nome_entry.place(relx=0.3, rely=0.15, anchor="w")

    email_label = tk.Label(registration_window, text="Email:", fg="black", bg=bg_color, font=("Arial", 12))
    email_label.place(relx=0.1, rely=0.25, anchor="w")
    email_entry = tk.Entry(registration_window)
    email_entry.place(relx=0.3, rely=0.25, anchor="w")

    telefone_label = tk.Label(registration_window, text="Telefone:", fg="black", bg=bg_color, font=("Arial", 12))
    telefone_label.place(relx=0.1, rely=0.35, anchor="w")
    telefone_entry = tk.Entry(registration_window)
    telefone_entry.place(relx=0.3, rely=0.35, anchor="w")

    idade_label = tk.Label(registration_window, text="Idade:", fg="black", bg=bg_color, font=("Arial", 12))
    idade_label.place(relx=0.1, rely=0.45, anchor="w")
    idade_entry = tk.Entry(registration_window)
    idade_entry.place(relx=0.3, rely=0.45, anchor="w")

    senha_label = tk.Label(registration_window, text="Senha:", fg="black", bg=bg_color, font=("Arial", 12))
    senha_label.place(relx=0.1, rely=0.55, anchor="w")
    senha_entry = tk.Entry(registration_window, show="*")
    senha_entry.place(relx=0.3, rely=0.55, anchor="w")

    # Adiciona o botão de cadastrar
    cadastrar_button = tk.Button(registration_window, text="Cadastrar", width=15, command=cadastrar_aluno)
    cadastrar_button.place(relx=0.5, rely=0.8, anchor="center")

# Configurações da janela principal
width, height = 350, 600
root = tk.Tk()
root.title("FlexGym")
root.geometry(f"{width}x{height}")

# Configuração do fundo da janela principal
canvas = tk.Canvas(root, width=width, height=height, bg='#000000')
canvas.pack()

original_image = Image.open("logo.png")
scaled_image = original_image.resize((int(root.winfo_screenwidth() * 0.8), int(root.winfo_screenheight() * 0.3)))
logo_png = ImageTk.PhotoImage(scaled_image)

# Criando o Canvas
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg='#000000')
canvas.pack()

# Botões na janela principal
botao_width = 30
professor_login_btn = tk.Button(root, text="Login do Professor", width=botao_width, command=open_professor_login)
professor_login_btn.place(relx=0.5, rely=0.7, anchor="center")

area_aluno_btn = tk.Button(root, text="Área do Aluno", width=botao_width, command=open_login_page)
area_aluno_btn.place(relx=0.5, rely=0.8, anchor="center")

# Loop principal da aplicação
root.mainloop()
