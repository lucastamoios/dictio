recreatedb:
	dropdb -U postgres -h localhost -p 5432 dictio
	createdb -U postgres -h localhost -p 5432 dictio
	python manage.py migrate