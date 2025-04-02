# Instructions for Postgres container usage

## Run container
1. Open a terminal window and run the command to start the postgres container
```bash
docker compose up
```
2. Automatically the container will create two databases:
	- `django_metadata_db`: stores all data related to the internal workings and operations of the Django backend.
	- `omnipath_db_sandbox`: stores test data for validating and simulating Omnipath features.

## Populate databases with data
3. Create the first "migration" (data population) for the Django database.
```bash
poetry run python manage.py migrate
```
4. With a Database administration tool like [DBeaver](https://dbeaver.io/) or [pgAdmin](https://www.pgadmin.org/) check that new tables have been added into the `django_metadata_db' database`.

- Connection data
  - **user**: postgres
  - **password**: postgres
  - **host**: localhost
  - **port**: 5432

5. Populate the sandbox database ('omnipath_db_sandbox') with data.
```bash
poetry run python ./_scripts/legacy_loader.py
```
6. Check if the data has been loaded by running the following queries as experiment:
```sql
-- count the number of rows in the 'interactions' table.
SELECT count(*)
FROM interactions;
```

```sql
-- retrieve the column and data type from the 'interactions' table.
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'interactions';
```

## Appendix

### Useful Docker command

#### Containers
- `docker ps -a`
- `docker stop <container-id-name>`
- `docker rm <container-id-name>`

#### Images
- `docker images`
- `docker image rm <image-name>`
- `docker image prune`

#### Volumes
- `docker volume rm <container-id-name>`

#### Composer
- `docker compose up`
