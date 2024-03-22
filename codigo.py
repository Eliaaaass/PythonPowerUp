# Passo a Passo
# Passo 1: Entar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 0.4

# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar uma tecla do teclado

# pyautogui.hotkey("ctrl", "v")

# abrir o navegador (chrome)
pyautogui.press("win")  
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" 
pyautogui.write(link)
pyautogui.press("enter")

# dar uma pausa um pouco maior (3 segundos)
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=425, y=413)
pyautogui.write("pythonimpressionador@gmail.com")
 
# escrever a senha
pyautogui.press("tab")
pyautogui.write("sua senha")

# clicar no botão de logar
pyautogui.click(x=669, y=567)
time.sleep(3)

# Passo 3: Importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar 1 produto
# para cada linha da minha tabela
for linha in tabela.index:
    # clicar no 1 campo
    pyautogui.click(x=418, y=286)
    #codigo do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # categoria
    # str() string -> texto
    # str(1) -> 1 -> "1"
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): 
        pyautogui.write(obs)
    pyautogui.press("tab")
    # enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até acabar
