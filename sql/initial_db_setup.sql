-- ------------------------------------------------------------
-- ------      POSTGRESQL INITIAL SETUP for OMNIPATH      -----
-- ------------------------------------------------------------
-- Authors: 
--	Omnipath Team
--	Scientific Software Center
-- Last update: 10.03.2025

-- Conventions:
--      Database: omnipath_db
--      Role: role_omnipath_admin
--      User: user_omnipath_admin
--      Tables: omnipath_interactions

-- Step 1. Create the OMNIPATH database
--DROP DATABASE omnipath_db;
CREATE DATABASE omnipath_db;

-- Step 2. Create an admin role (group) WITHOUT privileges
--      Privileges: 
--          - login or connection
--          - database access
--          - object ownership or permissions
CREATE ROLE role_omnipath_admin;

-- Step 3. Grant privileges to the admin role
-- Grant the ability to connect and create objects in the database
GRANT CONNECT, CREATE ON DATABASE omnipath_db TO role_omnipath_admin;

-- Grant usage and create permissions on the public schema
GRANT USAGE, CREATE ON SCHEMA public TO role_omnipath_admin;

-- Grant only the necessary privileges on existing tables (SELECT, INSERT, UPDATE, DELETE)
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO role_omnipath_admin;

-- Grant necessary privileges on sequences (USAGE, SELECT, UPDATE)
GRANT USAGE, SELECT, UPDATE ON ALL SEQUENCES IN SCHEMA public TO role_omnipath_admin;

-- Grant EXECUTE privileges on all functions
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO role_omnipath_admin;

-- Step 4. Set Default Privileges for Future Objects in the Schema
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO role_omnipath_admin;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE, SELECT, UPDATE ON SEQUENCES TO role_omnipath_admin;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT EXECUTE ON FUNCTIONS TO role_omnipath_admin;

-- Step 5. Create an admin user and set a secure password
CREATE USER user_omnipath_admin WITH PASSWORD 'omnipath123';

-- Step 6. Assign the role to the user
GRANT role_omnipath_admin TO user_omnipath_admin;
