#remember change authen key openai 

source envs/bin/activate


python3 manage.py runserver &

cd hpcg_frontend && yarn dev &