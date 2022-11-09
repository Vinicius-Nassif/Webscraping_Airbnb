# Projeto Web Scraping

## 1. Introdução 

​		Web Scraping, ou raspagem de dados, é uma modalidade de mineração que admite a extração de dados de sites da web convertendo em informação estruturada para análise futura. Geralmente, essa técnica é realizada por meio de um software que simula uma navegação humana nos sites desejados, extraindo informações específicas. 

​		Nesse projeto, o Python foi adotado como linguagem de programação para instrumentalizar o serviço de um freelancer responsável que deveria ir até o site do Airbnb (http://www.airbnb.com.br), realizar a varredura de todos os anúncios de hospedagens referentes a busca de uma cidade específica para obter as seguintes informações:

- Descrição;
- Detalhes;
- Leitos disponíveis;
- Valor da diária;
- URL; e 
- Avaliação dos usuários.

  ​	Após a obtenção das informações de todos os anúncios, esses dados serão inseridos e armazenados em uma planilha do Excel (.xlsx).

  ​	O intuito dessa atividade irá expor mais intensivamente a automação web, loops, variáveis, manipulações de arquivos e tratamento de exceções, conforme será demonstrado a seguir.



## 2. Bibliotecas

​		O projeto teve início com a importação das bibliotecas e funções utilizadas na elaboração do código em Python:

![1](https://user-images.githubusercontent.com/111388699/200918704-c78b07b2-7de7-4155-9217-a38339a2f372.png)

​		Primeiramente, ocorreu a importação da R*equests*, que é uma biblioteca HTTP para a linguagem de programação e tem como funcionalidade tornar as solicitações HTTP mais simples e mais fáceis de usar. 

​		Na sequência, a biblioteca *BeautifulSoup*, tem como funcionalidade a extração de dados de arquivos HTML e XML, funciona também como interpretador (parser). Já a biblioteca *Selenium* é uma ferramenta empregada para automatização de testes de sistemas que permite ao usuário reproduzi-los em passo acelerado no ambiente real da aplicação, em função da sua integração direta com o navegador.

​		Da biblioteca *time*, foi importado o método *sleep* com o objetivo de suspender a execução pelo número de segundos informado em seu parâmetro. Por último, foi importada a biblioteca *Pandas* como a sigla“pd”, com o objetivo de manipulação e análise de dados.



## 3. Código

### def __init__(self, url, cidade, arquivo):

​		O código teve início com a denominação de uma classe chamada “*WebScraping():*” e sua primeira função foi a __init__():, como podemos ver a seguir:

![2](https://user-images.githubusercontent.com/111388699/200918760-a911667a-f25e-4839-badc-866b8f6878f3.png)

​		O método *“__init__():*” é um método especial para que o Python execute automaticamente sempre que criarmos uma nova instância baseada na classe “WebScraping():” e foi definido para ter quatro parâmetros: o self, url, cidade e arquivo.

​		Logo abaixo, iniciam-se os objetos *self.site*, *self.navegador*e *self.hospedagens* como vazios com o objetivo de receberem seus valores no desenvolvimento do código. O objeto *self.dados_hospedagens* foi criado como uma lista vazia a ser preenchida futuramente com um *dataframe*. 

​		Já o *self.options* recebeu o método “*Options()*”, nativo da biblioteca *Selenium*, que por sua vez recebeu as configurações de inicialização do navegador, sendo a linha 25 para especificar as dimensões da janela do navegador a ser aberta e, na linha 26, para que seja toda rotina realizada sem ser fechada. 

​		A linha 27 foi deixada comentada como opção a ser habilitada em momento oportuno, caso seja desejado que toda a rotina seja realizada sem abrir o navegador. 

​		Na sequência, com o objetivo de demonstrar que a inicialização de todo método *“__init__():”* ocorreu com êxito, na linha 29 foi definido para exibir uma mensagem pelo método *print(‘WebScraping inicializado’)*. 


### def run(self):

​		O próximo método criado é a função “*run(self):*” e tem o objetivo de orquestrar a execução sequencial de todas as fases do *Web Scraping*, como um índice representativo e intuitivo com o chamado de todos os métodos que serão executados e também explicados ao longo desse documento, e trazendo também mensagens de êxito nas conclusões de cada etapa pelo método *print()*. 

![3](https://user-images.githubusercontent.com/111388699/200918823-92bebad6-196e-4075-ab0b-79330d8b0d2e.png)

​		Nesse momento, é necessário chamar a atenção aos passos das linhas 43 a 59 que abordam a criação do laço de paginação empregado no próprio método “*run(self):*”. 

​		O laço teve início com a criação da variável *“botao_prox_pag”* e a ela foi atribuído o valor *True*. Na linha subsequente, essa variável foi alocada em um laço *while* atribuindo o funcionamento das etapas indentadas (linhas 47 a 59) enquanto o *“botao_prox_pag”* permaneça com o valor de verdadeiro (*True*). Assim, a variável *“botao_prox_pag”* foi atribuída a função *self.prox_pag():*. 

​		A análise de valor como verdadeiro ou falso será feita pela função *self.prox_pag()*:,encerrando o laço while e que terá explicação mais detalhada retratada no desenvolvimento.


### def get_url(self):

​		Essa função indica a automação do navegador Google Chrome.

![4](https://user-images.githubusercontent.com/111388699/200918923-845b2011-6933-4561-8c39-1b3e1240f891.png)

​		A automação iniciou-se por meio do "*self.navegador*" recebendo *o webdriver* do *Selenium*, com as opções atribuídas no método *__init__*. A função do *webdriver* é manipular o navegador nativamente, como um usuário faria, por meio de automação, seja localmente ou em uma máquina remota usando o servidor *Selenium*.

​		Na sequência, trazendo o método "*self.navegador.get(self.url)*" com a biblioteca *Requests*, realizando a solicitação HTTP para a linguagem de programação. 

​		O método *sleep* recebeu como parâmetro 5 segundos para aguardar seguir para o próximo método, evitando erros no processo enquanto ocorre a abertura do navegador e a solicitação do HTTP. 


### def clica_busca(self): 

Essa função identifica o botão de busca do site airbnb. 

![5](https://user-images.githubusercontent.com/111388699/200919005-78bb4bf2-e7a7-4a28-9b4a-7ca53ef95efe.png)

​		A imagem demonstra que foi criada a variável button e ela recebeu o "*self.navegador*" com o método "*find_element*" (pertencente à biblioteca do *Selenium*) para encontrar o elemento pelo nome da tag, alocando os atributos entre parênteses após inspeção da estrutura HTML do site. 

​		Encontrado o elemento, a variável "button" recebe o comando de clicar por meio do método "*click()*", ficando o espaço apto para receber o nome da cidade desejada por meio da próxima função (imagem a seguir).

​		O método *sleep* recebeu como parâmetro 3 segundos para aguardar seguir para o próximo método, evitando erros na execução enquanto o ocorre a abertura do campo de busca.

![6](https://user-images.githubusercontent.com/111388699/200919051-041ddb6e-897c-4da9-b6be-368f1d909400.png)



### def input_cidade(self):

​		Essa função identifica o input e envia a busca desejada.

![7](https://user-images.githubusercontent.com/111388699/200919100-be534be2-e059-4367-aa4b-14e1e5269eb1.png)

​		Foi criada a variável "*input_place*" e ela recebeu o "*self.navegador*" com o método "*find_element*" (pertencente à biblioteca do Selenium) para encontrar o elemento pelo "*xpath*", alocando os atributos entre parênteses após inspeção da estrutura HTML do site.

​		Encontrado o elemento, a variável "*input_place*" recebe as letras que compõem o nome da cidade pelo método "*input_place.send_keys(self.cidade)*".

​		O método *sleep* da linha 84 recebeu como parâmetro 1 segundo para permitir a visualização do "*input*" e na sequência seguir para o método "*submit()*", que serviu para dar um "*Enter*" na navegação, então houve nova chamada do método sleep por 3 segundos na linha 86, evitando erros na execução enquanto ocorre a navegação pelo site.

![8](https://user-images.githubusercontent.com/111388699/200919154-9e94d854-4028-48ef-842a-bca3bfc2be88.png)



### def integracao_bs(self):

​		Essa função indica o início da integração com a biblioteca *BeautifulSoup*. 

![9](https://user-images.githubusercontent.com/111388699/200919216-94ebe893-af1b-4bf5-8b73-70bf555f46e9.png)

​		A variável "*self.site*" recebeu o método *BeautifulSoup*, tendo como parâmetros o "*self.navegador.page_source*" e o *html.parser*. Aqui ocorre preparação para identificação do conteúdo a ser extraído e interpretação do conteúdo HTML. 


### def identifica_auncio(self):

​		Essa função identifica o atributo raiz do anúncio.

![10](https://user-images.githubusercontent.com/111388699/200919237-2cd2e136-ee2e-4fcb-9f5f-8e39885a3b08.png)

​		Já com a biblioteca *BeutifulSoup* integrada com o *Selenium*, a variável "*self.hospedagens*" recebeu a variável "*self.site*" com o método "*findAll*", com os parâmetros inspecionados da estrutura HTML: div e o atributo de classe a partir da interpretação do conteúdo HTML.

​		Esses parâmetros foram observados como padrões na estrutura raiz dos anúncios de cada hospedagem, ou seja, é igual para todos eles.  Portanto, dessa forma a função foi orientada para identificar o bloco raiz de todos os anúncios da estrutura HTML de cada página a ser percorrida durante a execução do *Web Scraping*. A imagem a seguir ilustra a inspeção desse elemento:

![11](https://user-images.githubusercontent.com/111388699/200919262-0b3e7f03-7e00-41e9-be35-3ed3a7009e79.png)


### def raspagem_dados(self):

​		Essa função é responsável pela automação da raspagem de dados de cada anúncio das hospedagens. 

![12](https://user-images.githubusercontent.com/111388699/200919296-4f06dd97-e533-46b1-aeab-bd924fd9e1e0.png)

​		Para que a raspagem ocorresse da forma desejada, a função foi introduzida por um laço de repetição *for*. Para cada hospedagem dentro da variável "*self.hospedagens*", seria extraída a descrição, os detalhes, leitos disponíveis, o valor, a *URL* e a avaliação. 

​		Cada variável recebeu a hospedagem com o método "*find*" e entre os parênteses os parâmetros encontrados na inspeção da estrutura HTML. 

​		Para as variáveis "hospedagem_descricao", "hospedagem_valor", "hospedagem_leitos", "hospedagem_avaliação" foi chamado o método "*get_text()*" com o objetivo de trazer as informações limpas, sem trechos das estruturas HTML. 

​		A variável "hospedagem_url" recebeu o atributo [*‘content’*] para trazer apenas o link quando fosse chamada, desprezando também os trechos das estruturas HTML. 

​		Após definida a estrutura da extração de dados de cada variável, o método "*print()*" foi chamado, para cada uma delas, de forma que ficasse organizado no terminal do interpretador, sendo que foi utilizado um "*print()*" vazio para realizar uma quebra de linha entre as informações extraídas dos anúncios. 

![13](https://user-images.githubusercontent.com/111388699/200919378-ecef9e51-c8fa-4146-8bd6-9d0a7bf5cbb5.png)

​		Encerrando o laço *for*, foi criado um *dataframe* na variável "*self.dados_hospedagens*" com o método *append*, que serviu para anexar as informações extraídas em cada campo especificado.


### def prox_pag(self):

​		Essa função é responsável em encontrar e executar a paginação do website.

![14](https://user-images.githubusercontent.com/111388699/200919418-eadb012a-e937-4a35-ad0a-f60ec3b57de1.png)

​		É iniciada com a orientação *try*, ou seja, que o *Python* realize a tentativa recebendo a variável "*next_button*" com a variável "*self.navegador*" com o método "*find_element*"pelos parâmetros do HTML. Esse elemento é para identificar o botão de próxima página (“setinha”) que se encontra no próprio site, como se o usuário estivesse visualizando onde clicar desejando a paginação.

![15](https://user-images.githubusercontent.com/111388699/200919467-40d2a3ff-71d3-40bc-8593-e344ee0c2b28.png)

​		Na sequência, a variável "*botao_vazio*" recebeu o "*next_button*" com o método "*get_property(‘disabled’)*" para identificar caso o botão de passar para a próxima página tenha em sua propriedade que está desabilitado, com o intuito de evitar erros. 

​		Assim, ao se iniciar a condicional "*if botao_vazio is True*:", deve o *Python* encerrar a raspagem de dados, dando o retorno *False* para o laço de paginação *While* criado na função "*run(self)*": citada nas primeiras páginas, ou seja, se o botão estiver com a propriedade de desabilitado, ele não poderá mais ser clicado para passar a página e indica que é a última página a ser raspada, encerrando o laço. 

​		Enquanto o "*next_button*" permanecer sendo encontrado com a propriedade habilitada, será aguardado 2 segundos pelo método "*sleep()*" e, então clicado, retornando o valor de *True* para o laço de paginação citado no parágrafo anterior, prosseguindo para raspagem de dados da página seguinte. 

​		Ao ser finalizada a orientação *try:*, é indicado o "*except Exception as e:*" para que seja colocado em um método *print()* a exceção que ocorreu no código.


### def criar_tabelas(self):

​		Essa função é responsável pela criação da planilha no Excel. 

![16](https://user-images.githubusercontent.com/111388699/200919536-49982572-cf7e-4c1a-b1c2-0304934e511d.png)

​		A variável dados recebeu o Pandas com a sigla pd e o método "*DataFrame*", atribuindo à "*self.dados_hospedagens*" as colunas ‘Descrição’, ‘Detalhes’,‘Leitos’, ‘Valor’, ‘Avaliação’ e ‘URL’. 

​		Cada uma dessas colunas receberá o dataframe com os dados correspondentes que foram raspados do site airbnb. 

​		Por fim, a variável dados, que detém todo o dataframe, foi colocada com o método *to_excel* com os parâmetros "*self.nome_arquivo*" e "*index=False*", indicando a criação da planilha. 


## 4. Execução

![17](https://user-images.githubusercontent.com/111388699/200919569-975c6322-cf87-4d35-a68e-2ff3951bfb16.png)

​		Por fim, foi criada a variável airbnb recebendo a classe WebScraping, dando como parâmetros a url=‘http://www.airbnb.com.br’, a cidade=’Rio de Janeiro’ e o arquivo=’dados_hospedagem.xlsx’. Lembrando que esses parâmetros estavam sendo preparados desde a *def __init__():*.

​		Em seguida, a variável airbnb foi chamada com o método "*run()*", executando todo o *web scraping*. 


## 5. dados_hospedagens.xlsx

​		Vejamos como ficou parte da planilha após receber o *dataframe* criado:

![18](https://user-images.githubusercontent.com/111388699/200919620-625bcd0e-265c-4fb1-9127-28a59e5e98da.png)



## 6. Conclusão

​		Esse projeto foi criado para melhor elucidar o conhecimento trazido pela extração de dados, pois no seu desenvolvimento foi necessária a interação de várias bibliotecas do Python, bem como entender conceitos e aplicações da lógica de programação.

​		Percebeu-se também que para solucionar o problema principal foi necessário dividi-lo em pequenas tarefas para o desenvolvimento. 

​		Portanto, essa é uma forma de usar a coleta e manipulação de dados a seu favor, seja para uso pessoal ou profissional.



