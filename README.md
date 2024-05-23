# Desafio Backend | Django

Olá, candidato! Se você chegou até aqui, é porque demonstrou interesse em fazer parte do nosso time. Preparamos um desafio para entendermos um pouco mais sobre suas habilidades como desenvolvedor backend em Django.

## 🚀 Objetivo:

Desenvolver uma API para gerenciar um sistema de tarefas e projetos, permitindo que usuários criem projetos e associem tarefas a eles.

## 📖 Regras de Negócio:

1. Somente o criador do projeto pode adicionar ou remover membros.
2. Tarefas só podem ser criadas por membros do projeto ao qual a tarefa pertence.
3. Um usuário só pode ser adicionado a um projeto se ele já estiver registrado na plataforma.
4. Tarefas concluídas não podem ser editadas.
5. As tarefas precisam ter tags.

## 💻 Tecnologias:

- Django

# Desafio Backend | Django

Olá, candidato! Se você chegou até aqui, é porque demonstrou interesse em fazer parte do nosso time. Preparamos um desafio para entendermos um pouco mais sobre suas habilidades como desenvolvedor backend em Django.

## 🚀 Objetivo:

Desenvolver uma API para gerenciar um sistema de tarefas e projetos, permitindo que usuários criem projetos e associem tarefas a eles.

## 📖 Regras de Negócio:

1. Somente o criador do projeto pode adicionar ou remover membros.
2. Tarefas só podem ser criadas por membros do projeto ao qual a tarefa pertence.
3. Um usuário só pode ser adicionado a um projeto se ele já estiver registrado na plataforma.
4. Tarefas concluídas não podem ser editadas.
5. As tarefas precisam ter tags.

## 💻 Tecnologias:

- Django
- PostgreSQL
- Django REST framework
- Django ORM

## 📜 Requisitos:

### 1. Configuração Inicial:

- Configurar um projeto usando Django.
- Configurar um banco de dados PostgreSQL (Local).
- Utilizar o Django ORM.

### 2. Modelo de Dados:

#### Usuário (`User`):

- ID: ID gerado automaticamente.
- Nome: Texto.
- Email: Texto, único.
- Senha: Texto, encriptada.

#### Projeto (`Project`):

- ID: ID gerado automaticamente.
- Nome: Texto.
- Descrição: Texto.
- Membros: Lista de usuários associados ao projeto.

#### Tarefa (`Task`):

- ID: ID gerado automaticamente.
- Título: Texto, máximo de 255 caracteres.
- Descrição: Texto.
- Data de criação: Data e hora, gerada automaticamente.
- Status: Enum (Pendente, Em andamento, Concluída).
- Projeto: Referência ao projeto ao qual pertence.

#### Tag (`Tag`):

- ID: ID gerado automaticamente.
- Título: Texto.
- Tarefa: Referência a tarefa ao qual pertence.

### 3. Autenticação e Autorização:

- Implementar autenticação usando Django Rest Framework com JWT.
- Garantir que somente usuários autenticados possam acessar os endpoints.
- Implementar permissões para garantir que somente o criador do projeto possa adicionar ou remover membros.

### 4. Validações e Erros:

- Implemente validações para garantir a integridade dos dados.
- Responda com mensagens de erro claras e status HTTP apropriados.

## 🥇 Diferenciais:

- Testes unitários e/ou de integração.
- Documentação com Swagger ou DRF-YASG.
- Paginação nos endpoints.
- Registro de logs.
- Dockerização da aplicação.
- Uso de um linter (como Flake8) e formatador de código (como Black).

## 🗳️ Instruções de Submissão:

1. Faça um fork deste repositório para sua conta pessoal do GitHub.
2. Commit e push suas mudanças para o seu fork.
3. Envie um e-mail para [arthur.olga@khipo.com.br] com o link do repositório.

## 🧪 Avaliação:

- Estrutura do código e organização.
- Uso adequado das ferramentas e tecnologias.
- Implementação dos requisitos e regras de negócio.
- Design e usabilidade.
- Funcionalidades extras (diferenciais).

Boa sorte com o desafio! Estamos ansiosos para ver sua solução.
