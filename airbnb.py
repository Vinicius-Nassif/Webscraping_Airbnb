import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import re

# Operando o Selenium
options = Options()
options.add_argument('window-size=maximized')  # Especifica as dimensões da janela aberta
options.add_experimental_option("detach", True) # Manter o Chrome aberto
## options.add_argument('--headless')  # Realiza a rotina sem abrir o navegador

# Indicando a automação do Chrome 
navegador = webdriver.Chrome(options=options)
navegador.get('https://www.airbnb.com')

# Indica quantos segundos aguarda para continuar executando o código
sleep(10)

# Indentificando o botão de busca
button = navegador.find_element(By.TAG_NAME, "button")
button.click()

sleep(3)

# Identificando o input e enviando a busca desejada
input_place = navegador.find_element(By.XPATH, "//*[@id='bigsearch-query-location-input']")
input_place.send_keys('Rio de Janeiro')
input_place.submit()

sleep(3)

# Integração com o BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}
page_content = navegador.page_source
site = BeautifulSoup(page_content, 'html.parser')

# Criação de uma lista a ser preenchida futuramente com um dataframe
dados_hospedagens = [] 

# Identificação do atributo raiz do anúncio
hospedagens = site.findAll('div', attrs={'itemprop': 'itemListElement'})

# Automação da busca das hospedagens 
for hospedagem in hospedagens:
	hospedagem_descricao = hospedagem.find('span', class_='tjbvqj3 dir dir-ltr').get_text()
	hospedagem_detalhes = hospedagem.find('span', class_='dir dir-ltr').get_text()
	hospedagem_valor = hospedagem.find('div', class_='p11pu8yw dir dir-ltr').get_text()
	hospedagem_url = hospedagem.find('meta', attrs={'itemprop': 'url'})
	hospedagem_avaliacao = hospedagem.find('span', class_='ru0q88m dir dir-ltr').get_text()

	print('Descrição:', hospedagem_descricao)
	print('Detalhes:', hospedagem_detalhes)

	# Regex para formatar a apresentação do valor
	valor_regex = re.search("R\$(\d{1,})", hospedagem_valor).group(1)

	print('Valor:', valor_regex)
	print('Avaliação:', hospedagem_avaliacao)

	#Adicionar a informação dentro do atributo content
	hospedagem_url = hospedagem_url['content'] 
	print('URL:', hospedagem_url)
	
	# Utilizado para quebra de linhas
	print() 


	# Criação do DataFrame
	dados_hospedagens.append([hospedagem_descricao, hospedagem_detalhes, valor_regex, hospedagem_avaliacao, hospedagem_url])

# Criação do .xlsx
dados = pd.DataFrame(dados_hospedagens, columns=['Descrição', 'Detalhes', 'Valor', 'Avaliação', 'URL'])
dados.to_excel('hospedagens.xlsx', index=False)


