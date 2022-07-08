#### Digital Innovation One
#### Curso de Desenvolvimento para Internet e Banco de Dados com Python e Django
#### Aplicação Agenda

#### Tecnologias utilizadas:

- python 3.7
- Pycharm Community
- Django 2.1
- pip 
- Virtualenv

#### Estrutura da Agenda
DJANGO-ADMIN
MANAGE
WSGI
SETTINGS
URLS
VIEWS
MODELS
ADMIN
STATIC
TEMPLATES

django-admin.py

É o utilitário de linha de comando do Django para tarefas administrativas
django-admin --help

Fica no pacote do django e não no pacote do meu projeto

MANAGE

É um wrapper em volta do django-admin.py
Ele delega tarefas para o django-admin.py
Responsável por colocar o pacote do projeto no sys.path
Ele define a variável de ambiente django-settings_module que aponta para o arquivo settings.py
Por isso, o manage.py é gerado automaticamente junto ao projeto, para facilitar a uso de comandos do django-admin.py (comandos administrativos)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agenda.settings')

execute_from_command_line(sys.argv)

WSGI
web Server Gateway Interface - Interface de porta de entrada do servidor web
Plataforma padrão para aplicação web em Python
Serve de interface do Servidor Web e a Aplicação Web
O Django com o comando startproject inicia uma configuração WSGI padrão para que se possa executar sua aplicação web
Quando se inicia a aplicação Django com o comando runserver é iniciado um servidor de aplicação web leve. Esse servidor é especificado pela configuração wsgi_application

SETTINGS
É o responsável pelas configurações do Django.

Nele é possível configurar por exemplo apps, conexão com banco de dados, templates, time zone, cache, segurança, arquivos estáticos, etc.

URLS
É um Schema de URL.
Responsável por gerenciar as Rotas da URLs, onde é possível configurar para onde cada rota será executada.
É uma forma limpa e elegante para gerenciar URLs.

WIEWS
Responsável por processar e retornar uma resposta para o cliente que fez a requisição.

MODELS
Define o modelo de dados inteiramente em Python.
Faz a abstração dos objetos de banco parea o Python, transformando todas as tabelas em classes e os acessos são feito utilizando linguagem Python, onde o Django realiza a transformação para SQL. 

ADMIN
Interface administrativa gerada automaticamente pelo Django.

Ele lê os metadados que estão nos models e fornece uma interface poderosa e pronta para manipulação de dados.

STATIC
Responsável por armazenar os arquivos estáticos 
CSS, JavaScript, imagens

TEMPLATES
Responsável por armazenar os arquivos HTML
O diretório templates é diretório padrão para armazenarmos todo o conteúdo HTML da nossa aplicação.