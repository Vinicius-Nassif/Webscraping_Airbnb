import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import re

# Operando o Selenium
def config_inicial():

	options = Options()
	options.add_argument('window-size=maximized')  # Especifica as dimensões da janela aberta
	options.add_experimental_option("detach", True) # Manter o Chrome aberto
	## options.add_argument('--headless')  # Realiza a rotina sem abrir o navegador

	return options

def conecta_navegador(options):

	# Indicando a automação do Chrome 
	navegador = webdriver.Chrome(options=options)
	navegador.get('https://www.airbnb.com')

	return navegador

def raspagem_dados(topico, classe):
	return hospedagem.find(topico, class_=classe).get_text()

def retorna_hospedagem_url():
	hospedagem_url = hospedagem.find('meta', attrs={'itemprop': 'url'})
	hospedagem_url = hospedagem_url['content'] 
	print('Descrição:', hospedagem_descricao)
	print('Detalhes:', hospedagem_detalhes)

	return hospedagem_url

def formata_valor():
	print('Valor:', valor_regex)
	print('Avaliação:', hospedagem_avaliacao)
	return  re.search("R\$(\d{1,})", hospedagem_valor).group(1)

def cria_xlsx():
	dados_hospedagens = [] 
	dados_hospedagens.append([hospedagem_descricao,
							  hospedagem_detalhes,
							  valor_regex, 
							  hospedagem_avaliacao, 
							  hospedagem_url])
							  
	dados = pd.DataFrame(dados_hospedagens, columns=['Descrição', 
													'Detalhes', 
													'Valor', 
													'Avaliação', 
													'URL'])

	dados.to_excel('hospedagens.xlsx', index=False)

def clica_busca(navegador):
# Indentificando o botão de busca
	button = navegador.find_element(By.TAG_NAME, "button")
	button.click()

def input_cidade(navegador, cidade):

	# Identificando o input e enviando a busca desejada
	input_place = navegador.find_element(By.XPATH, "//*[@id='bigsearch-query-location-input']")
	input_place.send_keys(cidade)
	input_place.submit()

def integra_beautifulsoup(navegador):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}
	page_content = navegador.page_source
	site = BeautifulSoup(page_content, 'html.parser')

	return site

def identifica_anuncio(site_entrada):
	site_saida = site_entrada.findAll('div', attrs={'itemprop': 'itemListElement'})

	return site_saida

options = config_inicial()

navegador = conecta_navegador(options)
# Indica quantos segundos aguarda para continuar executando o código
sleep(10)

clica_busca(navegador)

sleep(3)

input_cidade(navegador, 'Rio de Janeiro')

sleep(3)

# Integração com o BeautifulSoup
site = integra_beautifulsoup(navegador)

# Identificação do atributo raiz do anúncio
hospedagens = identifica_anuncio(site)

# Automação da busca das hospedagens 
for hospedagem in hospedagens:
	hospedagem_descricao = raspagem_dados('span', 'tjbvqj3 dir dir-ltr')
	hospedagem_detalhes = raspagem_dados('span', 'dir dir-ltr')
	hospedagem_valor = raspagem_dados('div', 'p11pu8yw dir dir-ltr')
	hospedagem_avaliacao = raspagem_dados('span', 'ru0q88m dir dir-ltr')
	hospedagem_url = retorna_hospedagem_url()


	valor_regex = formata_valor()

	# Adicionar a informação dentro do atributo content

	print('URL:', hospedagem_url)
	
	# Utilizado para quebra de linhas
	print() 


	# Criação do DataFrame
	
cria_xlsx()





