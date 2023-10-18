-- Set the default character set and collation for the entire database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Set the character set and collation for the first_table table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Set the character set and collation for the name field in the first_table table
ALTER TABLE first_table MODIFY COLUMN name varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
