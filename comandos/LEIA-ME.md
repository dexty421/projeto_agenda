Iniciar o projeto Django
###########

python -m venv venv
.\venv\Scripts\activate 
pip install django
django-admin startproject project .
python manage.py startapp "nome_do_projeto"  #AQUI É O NOME Q VC ESCOLHER SEM ASPAS

#########
Configurar o git
#########

git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT
#####