# Step by Step Development of Omnipath Web server (Fullstack + API)

**Repository name**: omnipath-server-django

**Minimum Viable Product (MVP)**:

- Load a subset of the interactions table (100 rows) into a PosgreSQL database.
- Build an API to retrieve information from this database.


## Software required
- Python: >= 3.10
- Poetry
- Docker
- PosgreSQL: >=15
- pgAdmin or dBeaver
- Postman

## Setting up pre-requirements
1. Configure Poetry environment to be created inside of project's folder
```bash
poetry config virtualenvs.in-project true
```

## Setting up main project
### Installing required Python packages
1. Create an empty project using Poetry
- Poetry ~1.8
```bash
poetry new omnipath-server-django
```
- Poetry >2.0
```bash
poetry new omnipath-server-django --flat
```

2. Install Django Framework

The current version of Django by the time of writing this document is 5.1.6. We are going to install this version by using `poetry add`.
```bash
poetry add Django="5.1.6"
```

3. Install Django REST Framework

```bash
poetry add djangorestframework="^3.15"
```

4. Install CORS headers support for Django
```bash
poetry add django-cors-headers="^4.7.0"
```

5. Install Psycopg (PostgreSQL driver for Python)
```bash
# Psycopg 3 (recommended for new projects)
poetry add psycopg[binary]
```
### Create the main Django project
1. Go to the root of the recently created project.
```bash
cd omnipath-server-django
```
2. Delete the folder `omnipath_server_django`. This folder was created by Poetry. By doing this we are avoiding a possible conflict with the folder that Django will create.
```bash
rm -rf omnipath_server_django
```
3. Create an empty Django project (main project)

> **Note:** do no forget the dot (.) at the end, this allows Django to create the project in the current folder

```bash
poetry run django-admin startproject omnipath_server_django .
```

In the end of this process, you should check that the folder `omnipath_server_django` and a Python file have been created. The structure of the project should look like this:
```markdown
omnipath-server-django/
├── manage.py                # Django CLI tool
├── omnipath_server_django/  # Django project settings
│   ├── asgi.py              # ASGI entry point
│   ├── __init__.py          # init file│   
│   ├── settings.py          # project settings
│   ├── urls.py              # root URL config
│   └── wsgi.py              # WSGI entry point
├── poetry.lock              # poetry lock file
├── pyproject.toml           # poetry dependencies
├── README.md                # project documentation
├── tests                    # test suite folder (unit, integration, etc.)
|   └── __init__.py          # init file
└── .venv/                   # virtual environment (optional)
```

## Configure PostgreSQL as default Database
1. By default Django uses SQLite, for our project we are going to configure PosgreSQL as the default database. Open the `omnipath_server_django/settings.py` file and add the following parameters in the `DATABASES` section:

- Connection details:
  - Database name: `omnipath_db`
  - User: `postgres`
  - Password: `omnipath_admin_123` (for the superuser `postgres`)
  - Host: 127.0.0.1 (localhost)
  - Port: 5432 (default for PostgreSQL)
  
```python
DATABASES = {
	# ---------------------------
	# --  PostgreSQL Settings  --
	# ---------------------------
	"default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "omnipath_db",
        "USER": "postgres",
        "PASSWORD": "omnipath_admin_123",
        "HOST": "127.0.0.1",
        "PORT": 5432,
    }

    # --------------------------
	# --   SQLite Settings    --
	# --------------------------
	# "default": {
	#   "ENGINE": "django.db.backends.sqlite3",
	#   "NAME": BASE_DIR / "db.sqlite3",
	# }
}
```

## Create the API app
1. Create a Django app as part of the overall project, this app will be our API.
```bash
poetry run python startapp api
```
1. Register the following apps including the `api` as part of the project in the file `omnipath_server_django/settings.py`. Add the following elements in `INSTALLED_APPS` list:

- "django.contrib.postgres"
- "rest_framework"
- "corsheaders"
- "api"

The `INSTALLED_APPS` should look like this:
```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "rest_framework",
    "corsheaders",
    "api",
]
```
2. Add the CORS middleware in the `MIDDLEWARE` section by adding the following:
- "corsheaders.middleware.CorsMiddleware"

The `MIDDLEWARE` section should look like this:
```python
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
```

### Creating the Django Model
A **model** is a class that represents a table or collection in a database. Our naming convention for tables will be the following:

- Use only lowercase letters and underscore to separate words.
- Add the suffix `omnipath` at the end of the name.

The table names for the Omnipath database will be:
- `interactions_omnipath`
- `enzsub_omnipath`
- `complexes_omnipath`
- `intercell_omnipath`
- `annotations_omnipath`

For our MVP we will be working on the `interactions_omnipath` table. This table consist of the following schema:

| Column Name           | Data Type (SQL alchemy)   | Data Type (Django ORM)                                | Nullable | Auto Increment | Default   |
| --------------------- | ------------------------- | ----------------------------------------------------- |:--------:| -------------- | --------- |
| id                    | Integer                   | models.IntegerField(primary_key=True)                 |          | &check;        |           |
| source                | String                    | models.CharField(null=True, blank=True)               | &check;  |                |           |
| target                | String                    | models.CharField(null=True, blank=True)               | &check;  |                |           |
| source_genesymbol     | String                    | models.CharField(null=False, blank=True)              |          |                |           |
| target_genesymbol     | String                    | models.CharField(null=False, blank=True)              |          |                |           |
| is_directed           | Boolean                   | models.BooleanField()                                 |          |                |           |
| is_stimulation        | Boolean                   | models.BooleanField()                                 |          |                |           |
| is_inhibition         | Boolean                   | models.BooleanField()                                 |          |                |           |
| consensus_direction   | Boolean                   | models.BooleanField()                                 |          |                |           |
| consensus_stimulation | Boolean                   | models.BooleanField()                                 |          |                |           |
| consensus_inhibition  | Boolean                   | models.BooleanField()                                 |          |                |           |
| sources               | ARRAY(String)             | models.ArrayField(models.CharField(max_length=255))   |          |                |           |
| references            | String                    | models.CharField(null=False, blank=True)              |          |                |           |
| omnipath              | Boolean                   | models.BooleanField()                                 |          |                |           |
| kinaseextra           | Boolean                   | models.BooleanField()                                 |          |                |           |
| ligrecextra           | Boolean                   | models.BooleanField()                                 |          |                |           |
| pathwayextra          | Boolean                   | models.BooleanField()                                 |          |                |           |
| mirnatarget           | Boolean                   | models.BooleanField()                                 |          |                |           |
| dorothea              | Boolean                   | models.BooleanField()                                 |          |                |           |
| collectri             | Boolean                   | models.BooleanField()                                 |          |                |           |
| tf_target             | Boolean                   | models.BooleanField()                                 |          |                |           |
| lncrna_mrna           | Boolean                   | models.BooleanField()                                 |          |                |           |
| tf_mirna              | Boolean                   | models.BooleanField()                                 |          |                |           |
| small_molecule        | Boolean                   | models.BooleanField()                                 |          |                |           |
| dorothea_curated      | Boolean                   | models.BooleanField()                                 |          |                |           |
| dorothea_chipseq      | Boolean                   | models.BooleanField()                                 |          |                |           |
| dorothea_tfbs         | Boolean                   | models.BooleanField()                                 |          |                |           |
| dorothea_coexp        | Boolean                   | models.BooleanField()                                 |          |                |           |
| dorothea_level        | ARRAY(String)             | models.ArrayField(models.CharField(max_length=255))   |          |                |           |
| type                  | String                    | models.CharField(null=False, blank=True)              |          |                |           |
| curation_effort       | Integer                   | models.IntegerField()                                 |          |                |           |
| extra_attrs           | JSONB                     | models.JSONField(null=True, blank=True)               | &check;  |                |           |
| evidences             | JSONB                     | models.JSONField(null=True, blank=True)               | &check;  |                |           |
| ncbi_tax_id_source    | Integer                   | models.IntegerField()                                 |          |                |           |
| entity_type_source    | String                    | models.CharField(null=False, blank=True)              |          |                |           |
| ncbi_tax_id_target    | Integer                   | models.IntegerField()                                 |          |                |           |
| entity_type_target    | String                    | models.CharField(null=False, blank=True)              |          |                |           |

1. Create a model or blueprint for each table. Open the file `omnipath_server_django/api/models.py` file. This file will contains all the classes that represent the tables. In our case we are going to create just one class for the table `interactions_omnipath`

```python
from django.db import models


# Model for the table `interactions_omnipath`.
class InteractionsOmnipath(models.Model):
    source = models.CharField(null=True, blank=True)
    target = models.CharField(null=True, blank=True)
    source_genesymbol = models.CharField(null=False, blank=True)
    target_genesymbol = models.CharField(null=False, blank=True)
    is_directed = models.BooleanField()
    is_stimulation = models.BooleanField()
    is_inhibition = models.BooleanField()
    consensus_direction = models.BooleanField()
    consensus_stimulation = models.BooleanField()
    consensus_inhibition = models.BooleanField()
    sources = models.ArrayField(models.CharField(max_length=255))
    references = models.CharField(null=False, blank=True)
    omnipath = models.BooleanField()
    kinaseextra = models.BooleanField()
    ligrecextra = models.BooleanField()
    pathwayextra = models.BooleanField()
    mirnatarget = models.BooleanField()
    dorothea = models.BooleanField()
    collectri = models.BooleanField()
    tf_target = models.BooleanField()
    lncrna_mrna = models.BooleanField()
    tf_mirna = models.BooleanField()
    small_molecule = models.BooleanField()
    dorothea_curated = models.BooleanField()
    dorothea_chipseq = models.BooleanField()
    dorothea_tfbs = models.BooleanField()
    dorothea_coexp = models.BooleanField()
    dorothea_level = models.ArrayField(models.CharField(max_length=255))
    type = models.CharField(null=False, blank=True)
    curation_effort = models.IntegerField()
    extra_attrs = models.JSONField(null=True, blank=True)
    evidences = models.JSONField(null=True, blank=True)
    ncbi_tax_id_source = models.IntegerField()
    entity_type_source = models.CharField(null=False, blank=True)
    ncbi_tax_id_target = models.IntegerField()
    entity_type_target = models.CharField(null=False, blank=True)

    class Meta:
        db_table = "interactions_omnipath"  # Name of the table in the database
        verbose_name = (
            "Interactions Omnipath"  # Optional, for human-readable name in Django admin
        )
        ordering = ("id",)

```

