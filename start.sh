#remember change authen key openai 

source envs/bin/activate

lsof -nti:8000 | xargs kill -9     

python3 manage.py runserver &

cd hpcg_frontend && yarn dev &