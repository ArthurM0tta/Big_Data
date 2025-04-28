import pyautogui
import time
import subprocess

# Abrir Octoparse (ajuste o caminho se necessário)
subprocess.Popen(r"C:\Program Files\Octoparse\Octoparse.exe")
time.sleep(5)  # Espera 10 segundos para o Octoparse carregar completamente

# Tentativa de localizar o campo de e-mail
try:
    campo_email = pyautogui.locateCenterOnScreen(r'C:\Users\User\OneDrive\Documentos\botoes\caixa_email.png', confidence=0.8)
    if campo_email:
        pyautogui.click(campo_email)
        pyautogui.write("arthurmottat@gmail.com")  # Substitua com o seu e-mail
        print('Preencheu o e-mail')
    else:
        print("Campo de e-mail não encontrado. Pulando para o campo de senha.")
        raise ValueError("Campo de e-mail não encontrado")
except:
    campo_senha = pyautogui.locateCenterOnScreen(r'C:\Users\User\OneDrive\Documentos\botoes\caixa_senha.png', confidence=0.8)
    if campo_senha:
        pyautogui.click(campo_senha)
        pyautogui.write("0405tuco")  # Substitua com a sua senha
        print('Preencheu a senha')
    else:
        print("Campo de senha não encontrado.")

time.sleep(2)

# Localiza e clica no botão de login
botao_login = pyautogui.locateCenterOnScreen(r'C:\Users\User\OneDrive\Documentos\botoes\botao_login.png', confidence=0.8)
if botao_login:
    pyautogui.click(botao_login)
    print('Clicou no botão de login')
else:
    print("Botão de login não encontrado")

time.sleep(5)  # Aguardar o login ser processado

# Localiza e clica no botão "Task List"
botao_tasklist = pyautogui.locateCenterOnScreen(r'C:\Users\User\OneDrive\Documentos\botoes\botao_tasklist.png', confidence=0.8)
if botao_tasklist:
    pyautogui.click(botao_tasklist)
    print('Clicou no botão Task List')
else:
    print("Botão Task List não encontrado")

time.sleep(2)  # Aguardar a Task List abrir

# Localiza todos os botões "Run"
botoes_run = list(pyautogui.locateAllOnScreen(r'C:\Users\User\OneDrive\Documentos\botoes\botao_run.png', confidence=0.8))

if len(botoes_run) >= 2:
    # Seleciona o segundo botão "Run" da lista
    segundo_botao_run = botoes_run[1]  # O segundo botão é o índice 1 (o primeiro é o índice 0)
    pyautogui.click(segundo_botao_run)
    print('Clicou no segundo botão Run')
else:
    print("Segundo botão Run não encontrado")

time.sleep(40)  # Esperar o processo de extração começar

# Verifica se a janela de extração foi finalizada
# Isso é feito esperando a presença de uma janela específica que aparece após o término da extração
# Vamos procurar pela janela de confirmação

# A janela de "exportar dados" aparecerá após a extração. Localizamos o botão de exportação na tela.
botao_exportar = pyautogui.locateCenterOnScreen(r'C:\Users\User\OneDrive\Documentos\botoes\botao_exportar.png', confidence=0.8)

if botao_exportar:
    pyautogui.click(botao_exportar)
    print("Clicou no botão Exportar")
else:
    print("Botão de exportação não encontrado")

time.sleep(5)  # Esperar o processo de exportação ser realizado

# Agora, esperar a janela de confirmação e descer a barra de rolagem para encontrar o botão de confirmação
time.sleep(2)  # Aguardar o tempo necessário para a janela de confirmação aparecer

# Usando o comando de rolagem (scroll) ao invés de pressionar a tecla 'down'
for _ in range(2):  # Tentando rolar 5 vezes, pode aumentar ou diminuir conforme necessário
    pyautogui.scroll(-300)  # Valor negativo para rolar para baixo
    time.sleep(3)  # Espera 3 segundos entre as rolagens

# Localizar o botão de "Confirmar" na janela (ajuste a imagem de acordo)
botao_confirmar = pyautogui.locateCenterOnScreen(r'C:\Users\User\OneDrive\Documentos\botoes\botao_confirmar.png', confidence=0.8)

if botao_confirmar:
    pyautogui.click(botao_confirmar)
    print("Clicou no botão Confirmar")
else:
    print("Botão Confirmar não encontrado")

time.sleep(3)  # Esperar o processo de confirmação ser realizado

# Agora, depois de clicar no botão Confirmar e a janela de "Salvar Como" abrir

time.sleep(2)  # Aguardar um pouco para a janela "Salvar Como" aparecer

# Localiza e clica no botão "Desktop" na janela "Salvar Como"
botao_desktop = pyautogui.locateCenterOnScreen(r'C:\Users\User\OneDrive\Documentos\botoes\botao_desktop.png', confidence=0.8)

if botao_desktop:
    pyautogui.click(botao_desktop)  # Clica no botão "Desktop"
    print("Clicou no botão Desktop.")
else:
    print("Botão Desktop não encontrado. Continuando o processo.")

time.sleep(1)  # Aguardar um segundo para garantir que o "Desktop" seja aberto

# Agora, localize o botão "Salvar" na janela "Salvar Como"
botao_salvar = pyautogui.locateCenterOnScreen(r'C:\Users\User\OneDrive\Documentos\botoes\botao_salvar.png', confidence=0.8)

if botao_salvar:
    pyautogui.click(botao_salvar)  # Clica no botão "Salvar"
    print("Clicou no botão Salvar.")
else:
    print("Botão Salvar não encontrado.")

time.sleep(5)  # Espera o processo de salvamento ser concluído

# Após concluir a exportação e o salvamento
print("Processo de exportação e salvamento finalizado.")
