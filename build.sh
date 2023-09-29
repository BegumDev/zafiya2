set -o errexit
pip install -r requirements.txt
mython manage.py collectstatic --noinput
python manage.py makemigrations && python manage.py migrate
