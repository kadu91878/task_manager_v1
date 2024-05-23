# Task Manager


Uma API para gerenciar um sistema de tarefas e projetos, permitindo que usuários criem projetos e associem tarefas a eles.

## Instalação

```docker build -t task_manager:v1 . ```

```docker run web python manage.py migrate ```

```docker-compose up -d ```

## Exemplos de Uso
Uma vez que a API esteja rodando, deve se acessar a URL `http://127.0.0.1:8000/swagger/` para visualizar a documentação da API.

## Testes pelo Swagger

### Primeiro Passo
Deve se criar um usuário na parte de users e depois post /users/. clicando em Try it Out no canto direito superior. 
Uma opção para editar o JSON irá aparecer e você deve preenche-lo com as informações de seu usuário. como no exemplo:

{
  "username": "usuario",
  "email": "user@example.com",
  "password": "123user"
}

### Segundo Passo
Uma vez isso feito, você deve ir até o topo da página do Swagger e clicar em Authorize. Passe o username e o password criado no passo anterior, e você deverá receber o token JWT para acessar os outros recursos da API.

## Criando Projetos
Ainda no Swagger, após ter logado e recebido o token JWT. Você deve ir até a parte de projects, POST /projects/.
Clicando em Try It Out novamente, deve aparecer uma caixa para editar o JSON.

Exemplo:
{
  "name": "Projeto Teste",
  "description": "Este é apenas um teste de criação de projeto",
  "members": [
    1
  ]
}

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

{
  "title": "Homologação"
}

Ao clicar em Execute. Uma nova tag deve ser criada.

## Criando Tarefas

Ainda logado com seu usuário, você deve ir até a parte de tasks, POST /tasks/. Clicando em Try It Out novamente, deve aparecer uma caixa para editar o JSON.

Exemplo:
{
  "title": "Criar API Django-Rest",
  "description": "Criação de uma API Django-Rest para gerenciar projetos e tarefas",
  "status": "PENDING",
  "project": 1,
  "tags": [
    1
  ]
}

Ao clicar em Execute. Uma nova tarefa deve ser criada.

O status de uma tarefa pode ser: "PENDING", "IN_PROGRESS" ou "COMPLETED". Elas estão arranjadas em um ENUM no model.

O project do JSON deve receber o id do projeto para o qual a tarefa deve ser criada.

O tag do JSON deve receber o id da tag para a qual a tarefa deve ser criada.


## Outros Endpoints

GET /tasks/ /projects/ /tags/ /users/

Trazem uma lista paginada de tarefas, projetos, tags e usuários respectivamente.

GET /tasks/{id}/ /projects/{id} /tags/{id} /users/{id}

Trazem uma lista paginada de tarefas, projetos, tags e usuários respectivamente pelo id.

PUT/PATCH /tasks/{id}/ /projects/{id} /tags/{id} /users/{id}

Atualiza os dados de tarefas, projetos, tags e usuários.

DELETE /tasks/{id}/ /projects/{id} /tags/{id} /users/{id}

Deleta tarefas, projetos, tags e usuários.