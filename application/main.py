from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Caminho do WebDriver do Edge
service = Service(r'C:\Driver_Notes\msedgedriver.exe') 
driver = webdriver.Edge(service=service)

# Lista de links dos produtos
links_produtos = [
    "https://www.atacadao.com.br/arroz-tio-joao-agulhinha---tipo-1-12158-15018/p",
    "https://www.atacadao.com.br/feijao-carioca-kicaldo-tipo-1-pacote-com-1kg-11874-9925/p",
    "https://www.atacadao.com.br/filezinho-de-frango-sadia-congelado-64823-12656/p",
]

# Lista para armazenar os dados extraídos
produtos = []

# Loop para acessar os links e extrair os dados
for link in links_produtos:
    driver.get(link)
    
    try:
        # Esperar o nome do produto estar visível
        nome_produto = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1[@data-test='product-details-title']"))
        ).text
        
        # Esperar o preço do produto estar visível
        preco_produto = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(@class, 'text-2xl') and contains(@class, 'font-bold')]"))
        ).text
        
        # Adicionar dados ao list
        produtos.append([nome_produto, preco_produto])

    except Exception as e:
        print(f"Erro ao extrair dados de {link}: {e}")

# Criar um DataFrame com os dados extraídos
df = pd.DataFrame(produtos, columns=['Produto', 'Preço'])

# Exibir o DataFrame
print(df)

# Fechar o navegador após o término
driver.quit()
