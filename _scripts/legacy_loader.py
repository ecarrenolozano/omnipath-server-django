from omnipath_server.loader import _legacy as legacy_loader

# -------------------------------------------------
# ----      Parameters sandbox database      -----
PATH_DATA_SANDBOX = "./_data_sandbox/"
CON_PARAM_SANDBOX = {
    "user": "omnipathuser",  # Must coincide with the data in _scripts/sql/initial_db_sandbox_setup.sql
    "password": "omnipath123",  # Must coincide with the data in _scripts/sql/initial_db_sandbox_setup.sql
    "host": "localhost",
    "port": "5432",
    "database": "omnipath_db_sandbox",
}

# ----------------------------------------------------
# ----      Parameters Production database      -----
PATH_DATA_PRODUCTION = ""
CON_PARAM_PRODUCTION = {
    "user": "omnipath",  # Must coincide with the data in _scripts/sql/initial_db_production_setup.sql
    "password": "omnipath123456",  # Must coincide with the data in _scripts/sql/initial_db_production_setup.sql
    "host": "localhost",
    "port": "5432",
    "database": "omnipath_db",
}


def invoke_loader(option: str):

    if option == "sandbox":
        path = PATH_DATA_SANDBOX
        con = CON_PARAM_SANDBOX
    elif option == "production":
        path = PATH_DATA_PRODUCTION
        con = CON_PARAM_PRODUCTION
    else:
        raise ValueError

    loader_database_sandbox = legacy_loader.Loader(
        path=path,
        con=con,
    )

    print("Creating database...")
    loader_database_sandbox.create()
    print("Creating database...DONE")

    print("Populating database in {option}...")
    loader_database_sandbox.load()
    print("Populating database in {option}...DONE")
    print("End of process")


def main():
    option = "sandbox"

    invoke_loader(option=option)


if __name__ == "__main__":
    main()
