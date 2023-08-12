recreatedb:
	dropdb -U postgres -h localhost -p 5432 dictio
	createdb -U postgres -h localhost -p 5432 dictio
	python manage.py migrate

build:
	docker build -t lucastamoios/dictio -f docker/Dockerfile .

fast-run:
	docker compose -f docker/docker-compose.yml up

run: build fast-run
