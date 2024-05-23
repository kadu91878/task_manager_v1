# Documentação Task Manager

Uma API para gerenciar um sistema de tarefas e projetos, permitindo que usuários criem projetos e associem tarefas a eles.

## Sumário
1. [Instalação](#instalação)
   - [Docker](#docker)
   - [Ambiente Local](#ambiente-local)
2. [Exemplos de Uso](#exemplos-de-uso)
3. [Testes pelo Swagger](#testes-pelo-swagger)
   - [Primeiro Passo](#primeiro-passo)
   - [Segundo Passo](#segundo-passo)
4. [Criando Projetos](#criando-projetos)
5. [Criando Tags](#criando-tags)
6. [Criando Tarefas](#criando-tarefas)
7. [Outros Endpoints](#outros-endpoints)
8. [Flake8 e Black](#flake8-e-black)
9. [Debug](#debug)
10. [Testes](#testes)
11. [Segurança](#segurança)

## Instalação

Certifique-se de que tenha Python e/ou Docker instalado.

### Docker

Subir o projeto com o seguinte comando:

```docker build -t task_manager:v1 . ```

```docker-compose run web python manage.py migrate ```

```docker-compose up -d ```

### Ambiente Local

Este projeto está configurado para executar com Docker, mas caso queira utilizar um ambiente local siga alguns passos:

Primeiro virifique o settings.py, existe um código comentado de DATABASE que deve ser adicionado (enquanto o existente deve ser removido). Em seguida um arquivo .env deve ser adicionado com as informações de acesso ao banco de dados. neste modelo:

```
DATABASE_NAME=nome_da_database
DATABASE_USER=nome_de_usuario
DATABASE_PASSWORD=senha_de_usuario
DATABASE_HOST=host_do_banco
DATABASE_PORT=porta
DATABASE_SCHEMA=schema_a_ser_utilizado
```

Uma vez isso verificado e feito, execute seu ambiente python e em seguida faça:

```pip install -r requirements.txt```

Caso queira Flake8 e Black use:

```pip install flake8 black```

Em seguida rode as migrações com o seguinte comando:

```python manage.py migrate```

Feito isso, e se tudo estiver correto, execute o seguinte comando:

```python manage.py runserver```

## Exemplos de Uso
Uma vez que a API esteja rodando, deve se acessar a URL `http://127.0.0.1:8000/swagger/` para visualizar a documentação da API.

## Testes pelo Swagger

### Primeiro Passo
Deve se criar um usuário na parte de users e depois post /users/. clicando em Try it Out no canto direito superior. 
Uma opção para editar o JSON irá aparecer e você deve preenche-lo com as informações de seu usuário. como no exemplo:

```json
{
  "username": "usuario",
  "email": "user@example.com",
  "password": "123user"
}
```

### Segundo Passo
Uma vez isso feito, você deve ir até o topo da página do Swagger e clicar em Authorize. Passe o username e o password criado no passo anterior, e você deverá receber o token JWT para acessar os outros recursos da API.

## Criando Projetos
Ainda no Swagger, após ter logado e recebido o token JWT. Você deve ir até a parte de projects, POST /projects/.
Clicando em Try It Out novamente, deve aparecer uma caixa para editar o JSON.

Exemplo:
```json
{
  "name": "Projeto Teste",
  "description": "Este é apenas um teste de criação de projeto",
  "members": [
    1
  ]
}
```

Ao clicar em Execute. Um novo projeto deve ser criado com o usuário criado no passo anterior como membro desse projeto.

No Json members recebe uma lista de ids dos usuários que devem ser adicionados ao projeto.

PS: Se um novo usuário for criado, e tentar adicionar membros a esse projeto no PATCH/POST /projects/{id}/
Ele deve receber um erro:
"Apenas o criador do projeto pode adicionar ou remover membros."

A mesma coisa deve acontecer caso se tente excluir o projeto utilizando o login de outro usuário que não seja o criador do projeto. Apenas o criador do projeto pode adicionar ou remover membros, e deletar o projeto.

## Criando Tags

Importante! As Tags devem ser criadas ANTES das tarefas, caso contrário as tarefas não serão criadas, pois todas as tarefas precisam ser associadas a uma tag.

Ainda logado com seu usuário, vá até tags, em seguida POST /tags/. Clicando em Try It Out novamente, deve aparecer uma caixa para editar o JSON.

Exemplo:

```json
{
  "title": "Homologação"
}
```

Ao clicar em Execute. Uma nova tag deve ser criada.

## Criando Tarefas

Ainda logado com seu usuário, você deve ir até a parte de tasks, POST /tasks/. Clicando em Try It Out novamente, deve aparecer uma caixa para editar o JSON.

Exemplo:
```json
{
  "title": "Criar API Django-Rest",
  "description": "Criação de uma API Django-Rest para gerenciar projetos e tarefas",
  "status": "PENDING",
  "project": 1,
  "tags": [
    1
  ]
}
```

Ao clicar em Execute. Uma nova tarefa deve ser criada.

O status de uma tarefa pode ser: "PENDING", "IN_PROGRESS" ou "COMPLETED". Elas estão arranjadas em um ENUM no model.

O project do JSON deve receber o id do projeto para o qual a tarefa deve ser criada.

O tag do JSON deve receber o id da tag para a qual a tarefa deve ser criada.


## Outros Endpoints

```
GET /tasks/ /projects/ /tags/ /users/
```

Trazem uma lista paginada de tarefas, projetos, tags e usuários respectivamente.

```
GET /tasks/{id}/ /projects/{id} /tags/{id} /users/{id}
```

Trazem uma lista paginada de tarefas, projetos, tags e usuários respectivamente pelo id.

```
PUT/PATCH /tasks/{id}/ /projects/{id} /tags/{id} /users/{id}
```

Atualiza os dados de tarefas, projetos, tags e usuários.

```
DELETE /tasks/{id}/ /projects/{id} /tags/{id} /users/{id}
```

Deleta tarefas, projetos, tags e usuários.

PS:Estes endpoints podem ser utilizados pelo Postman ou Insomnia também.

## Flake8 e Black

Para rodar o Flake8 e o Black, execute os comandos:

Para Flake8:

``` python manage.py lint ```

Para Black:

``` python manage.py format ```

## Debug

Um registro de logs é criado no arquivo `debug.log`.

## Testes

Se a API estiver rodando, testes podem ser realizados para verificação dos serializers, views e models.
Utilize o comando:

```docker-compose run web python manage.py test core.tests```

## Segurança

Por questões práticas algumas coisas foram ignoradas neste projeto, afim de servir como um demonstrativo, e ter fácil utilização por qualquer pessoa que o clonar. 

Coisas que devem ser feitas para uso de segurança:

Em settings.py, remova:

```
ALLOWED_HOSTS = ['*']
```
Coloque apenas os HOSTS que sua aplicação deve servir. Deixei como * para que qualquer um possa testar irrestritamente.

```
DEBUG = True
```

Deve ser False para que o projeto funcione em produção.

```
SECRET_KEY = "django-insecure-v_6d6k3pm3l_e1$#^^!rqfkez%adgpab0dcbq*qen9p#7nz^3&"
```

Isto deve ser colocado no arquivo .env. e o .env deve ser passado no gitignore. Caso contrário qualquer pessoa terá acesso a sua aplicação irrestritamente e a autenticação será inútil.
