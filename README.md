 API FLASK KabumProject

Projeto executado buscando cumprir os requisitos do teste proposto. 
Utilizando flask_RESTful e MethodView 

Imagem Docker do projeto:
docker pull thailanhigor/kabumflask:v1

Executando normalmente sem o docker:

1 - Clonar o projeto.

2 - Abrir um Prompt de Comando na raiz do projeto e executar:
  pip install -r requirements.txt

3 - Após instalação dos pacotes, ainda no Prompt de Comando, Executar o codigo para execução do Flask.
  flask run -p 80 -h 0.0.0.0

4 - Abrir o navegador em localhost:80. Se for executado via docker, utilizar a porta que for disponiibilizada pelo container do docker.


Rotas de produtos disponível:

http://localhost/product/85197
http://localhost/product/78974
http://localhost/product/87400


Retorno: Informações dos produtos.
