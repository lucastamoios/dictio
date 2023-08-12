cd dictio/
git checkout master
git pull
python manage.py migrate
docker build -t lucastamoios/dictio -f docker/Dockerfile .
docker compose -f docker/docker-compose.yml up -d --force-recreate