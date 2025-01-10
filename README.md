Letras de Músicas 🎵
Este é um projeto simples desenvolvido em Python utilizando a biblioteca Streamlit para criar uma interface interativa e a API Lyrics.ovh para buscar letras de músicas.

Funcionalidades
Buscar letras de músicas de diversas bandas e artistas.
Exibir a letra diretamente na interface após a busca.
Interface amigável e intuitiva.
Pré-requisitos
Certifique-se de ter o Python 3.8+ instalado em sua máquina e as dependências necessárias instaladas.

Instale as dependências
Execute o comando abaixo para instalar as bibliotecas necessárias:

bash

pip install streamlit requests
Como Executar
Clone este repositório ou copie o código para sua máquina.
No terminal, navegue até o diretório do projeto.
Execute o comando abaixo para iniciar o aplicativo Streamlit:
bash

streamlit run app.py
Acesse o aplicativo no navegador pelo link exibido no terminal (geralmente em http://localhost:8501).
Uso
Digite o nome da banda ou artista no campo correspondente.
Digite o nome da música no campo apropriado.
Clique no botão Pesquisar.
Se a letra for encontrada, ela será exibida na tela. Caso contrário, uma mensagem de erro será exibida.
Captura de Tela


Estrutura do Código
buscar_letra(banda, musica): Função para consumir a API e retornar a letra da música.
Streamlit: Utilizado para criar a interface interativa.
API Lyrics.ovh: Fonte de letras de músicas.
Melhorias Futuras
Adicionar suporte a múltiplos idiomas.
Permitir salvar letras em arquivos locais.
Melhorar a exibição da letra com formatações adicionais.
Implementar um sistema de histórico de buscas.
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

Licença
Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
