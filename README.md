# Letras de Músicas 🎵
Este é um projeto simples desenvolvido em Python utilizando a biblioteca Streamlit para criar uma interface interativa e a API Lyrics.ovh para buscar letras de músicas.

### Funcionalidades
- Buscar letras de músicas de diversas bandas e artistas.
- Exibir a letra diretamente na interface após a busca.
- Interface amigável e intuitiva.
##
# Pré-requisitos
  Certifique-se de ter o Python 3.8+ instalado em sua máquina e as dependências necessárias instaladas.
 ### instale as dependências
Execute o comando abaixo para instalar as bibliotecas necessárias:<br>
### No terminal digite o código <br>
#### pip install streamlit requests
##
# Como Executar
 ### 1 : Clone este repositório ou copie o código para sua máquina.
#### 2: No terminal, navegue até o diretório do projeto.
### 3: Execute o comando abaixo para iniciar o aplicativo Streamlit:
### streamlit run app.py
### 4: Acesse o aplicativo no navegador pelo link exibido no terminal (geralmente em http://localhost:8501).
##
# Uso
### 1: Digite o nome da banda ou artista no campo correspondente.
### 2: Digite o nome da música no campo apropriado.
### 3: Clique no botão Pesquisar.
###  Se a letra for encontrada, ela será exibida na tela. Caso contrário, uma mensagem de erro será exibida.
##
# Estrutura do Código

- ### buscar_letra(banda, musica): Função para consumir a API e retornar a letra da música.
- ### Streamlit: Utilizado para criar a interface interativa.
- ### API Lyrics.ovh: Fonte de letras de músicas.


