# django-test-notebook
Collection Exercise and Give a random examination.

## Env
Python3.6 + Django 2.2

## Server Install
In my server, I put it in jupyter notebook control document.

    /home/ipynb/Notebook/django-test-notebook/

After checkout from this repository and cd to "Notebook". Then run django server

    python3 manage.py runserver 

Or If you want to let others see your demo through Internet, then:

    python3 manage.py runserver 0.0.0.0:<your port>

Then search it in browser.

## Database security strategy
1. Remove from git 
2. Backup every hour
3. Keep backup as 3 days