-- Check if the database hbnb_test_db already exists
SELECT SCHEMA_NAME
FROM INFORMATION_SCHEMA.SCHEMATA
WHERE SCHEMA_NAME = 'hbnb_test_db';

-- Create the database hbnb_test_db if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Check if the user hbnb_test@localhost already exists
SELECT User, Host
FROM mysql.user
WHERE User = 'hbnb_test' AND Host = 'localhost';

-- Create the user hbnb_test@localhost if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED WITH mysql_native_password BY 'hbnb_test_pwd';

-- Grant all privileges on hbnb_test_db to hbnb_test@localhost
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_test@localhost
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Apply the changes to the privilege tables
FLUSH PRIVILEGES;