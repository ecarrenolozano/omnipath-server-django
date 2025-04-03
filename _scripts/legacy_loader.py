from omnipath_server.loader import _legacy as legacy_loader

sample_dir = "./_data_sandbox"
con_param = {
    "user": "omnipathuser",
    "password": "omnipath123",
    "host": "localhost",
    "port": "5432",
    "database": "omnipath_db_sandbox",
}

loader = legacy_loader.Loader(
    path=sample_dir,
    con=con_param,
)
loader.create()
loader.load()
