import tkinter as tk
from tkinter import messagebox


def calcular_imc():
    try:
        nome = entrada_nome.get().strip()
        endereco = entrada_endereco.get().strip()
        altura = float(entrada_altura.get().replace(",", "."))
        peso = float(entrada_peso.get().replace(",", "."))

        if not nome:
            messagebox.showwarning("Atenção", "Informe o nome do paciente.")
            return

        if altura <= 0 or peso <= 0:
            messagebox.showerror("Erro", "Altura e peso devem ser maiores que zero.")
            return

        # Converter altura de centímetros para metros
        altura_metros = altura / 100

        # Calcular IMC
        imc = peso / (altura_metros ** 2)

        # Classificação do IMC para adultos
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        elif imc < 35:
            classificacao = "Obesidade grau I"
        elif imc < 40:
            classificacao = "Obesidade grau II"
        else:
            classificacao = "Obesidade grau III"

        resultado.config(
            text=f"Paciente: {nome}\n"
                 f"IMC: {imc:.2f}\n"
                 f"Classificação: {classificacao}"
        )

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Informe valores numéricos válidos para altura e peso."
        )


def reiniciar():
    entrada_nome.delete(0, tk.END)
    entrada_endereco.delete(0, tk.END)
    entrada_altura.delete(0, tk.END)
    entrada_peso.delete(0, tk.END)

    resultado.config(text="Resultado")


def sair():
    janela.destroy()


# Janela principal
janela = tk.Tk()
janela.title("Cálculo do IMC - Índice de Massa Corporal")
janela.geometry("550x330")
janela.resizable(False, False)
janela.configure(bg="#f0f0f0")


# Nome
tk.Label(
    janela,
    text="Nome do Paciente:",
    bg="#f0f0f0"
).place(x=20, y=30)

entrada_nome = tk.Entry(janela, width=48)
entrada_nome.place(x=160, y=30)


# Endereço
tk.Label(
    janela,
    text="Endereço Completo:",
    bg="#f0f0f0"
).place(x=20, y=70)

entrada_endereco = tk.Entry(janela, width=48)
entrada_endereco.place(x=160, y=70)


# Altura
tk.Label(
    janela,
    text="Altura (cm):",
    bg="#f0f0f0"
).place(x=20, y=110)

entrada_altura = tk.Entry(janela, width=20)
entrada_altura.place(x=160, y=110)


# Peso
tk.Label(
    janela,
    text="Peso (Kg):",
    bg="#f0f0f0"
).place(x=20, y=150)

entrada_peso = tk.Entry(janela, width=20)
entrada_peso.place(x=160, y=150)


# Área do resultado
frame_resultado = tk.Frame(
    janela,
    bg="white",
    relief="solid",
    borderwidth=1
)

frame_resultado.place(
    x=320,
    y=110,
    width=210,
    height=110
)

resultado = tk.Label(
    frame_resultado,
    text="Resultado",
    bg="white",
    justify="center",
    wraplength=190
)

resultado.pack(expand=True)


# Botões
botao_calcular = tk.Button(
    janela,
    text="Calcular",
    width=12,
    command=calcular_imc
)

botao_calcular.place(x=120, y=260)


botao_reiniciar = tk.Button(
    janela,
    text="Reiniciar",
    width=12,
    command=reiniciar
)

botao_reiniciar.place(x=230, y=260)


botao_sair = tk.Button(
    janela,
    text="Sair",
    width=12,
    command=sair
)

botao_sair.place(x=410, y=260)


# Executar aplicação
janela.mainloop()