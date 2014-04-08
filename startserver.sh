screen -dmS "runserver"
screen -r "runserver" -p 0 -X stuff $'cd /vagrant/review\n'
screen -r "runserver" -p 0 -X stuff $'python manage.py runserver 0.0.0.0:8000 --settings=review.settings.local\n'
