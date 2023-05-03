-- Active: 1675115094804@@db.ethereallab.app@3306@sk3395
/*ALTER TABLE IS601_Users
ADD
    COLUMN username varchar(30) not null unique default (substring_index(email, '@', 1)) COMMENT 'Username field that defaults to the name of the email';*/

ALTER TABLE IS601_Users MODIFY username varchar(30) not null unique default (substring_index(email, '@', 1)) COMMENT 'Username field that defaults to the name of the email';