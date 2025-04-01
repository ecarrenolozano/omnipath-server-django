class MyDatabaseRouter:
    """
    Routes:
    - Django internal tables -> 'default' (django_metadata_db)
    - 'api' app -> 'omnipath_data' (omnipath_db_sandbox)
    """

    django_apps = {
        "admin",
        "auth",
        "contenttypes",
        "sessions",
        "messages",
        "staticfiles",
        "postgres",
    }

    def db_for_read(self, model, **hints):
        """Direct read queries to the appropriate database."""
        if model._meta.app_label in self.django_apps:
            return "default"  # Use django_metadata_db
        if model._meta.app_label == "api":
            return "omnipath_data"  # Use omnipath_db_sandbox
        return None  # Let Django use default behavior

    def db_for_write(self, model, **hints):
        """Direct write queries to the appropriate database."""
        if model._meta.app_label in self.django_apps:
            return "default"
        if model._meta.app_label == "api":
            return "omnipath_data"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if both objects are in the same database."""
        db_set = {self.db_for_read(obj1), self.db_for_read(obj2)}
        return len(db_set) == 1  # Only allow relations within the same database

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure migrations go to the correct database."""
        if app_label in self.django_apps:
            return db == "default"  # Store Django internal tables in django_metadata_db
        if app_label == "api":
            return db == "omnipath_data"  # Store API app tables in omnipath_db_sandbox
        return None  # Let Django decide
