-- --------------------------------------------------------------------
-- ------      POSTGRESQL INITIAL SETUP for OMNIPATH SANDBOX      -----
-- --------------------------------------------------------------------
-- Authors:
--	Omnipath Team
--	Scientific Software Center
-- Last update: 01.04.2025

-- Conventions:
--      Database: omnipath_db_sandbox
--      User: omnipathuser
--      Tables:
--          * omnipath_annotations
--          * omnipath_complexes
--          * omnipath_enzptm
--          * omnipath_interactions
--          * omnipath_intercell

-- RUN WITH ROOT ('postgres')
CREATE DATABASE omnipath_db_sandbox;
CREATE USER omnipathuser WITH PASSWORD 'omnipath123';
ALTER DATABASE omnipath_db_sandbox OWNER TO omnipathuser;
GRANT ALL PRIVILEGES ON DATABASE omnipath_db_sandbox TO omnipathuser;


-- GRANT ALL ON SCHEMA public TO omnipathuser;
-- GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO omnipathuser;
-- GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO omnipathuser;
-- GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public TO omnipathuser;
-- ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO omnipathuser;
-- ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO omnipathuser;
-- ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON FUNCTIONS TO omnipathuser;

-- Connection with 'omnipathuser'
--$ psql -h localhost -p 5432 -d omnipath_db_sandbox -U omnipathuser

-- Connection with root (postgres)
--$ sudo -u postgres psql
