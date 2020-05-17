BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'LYU','lyu1025@nate.com','010-6755-7969','lyu.com','2020-03-19 23:58:50');
INSERT INTO "users" VALUES(2,'Park','Park@naver.com','010-1111-1111','Park.com','2020-03-19 23:58:50');
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com','010-2222-2222','Lee.com','2020-03-19 23:58:50');
INSERT INTO "users" VALUES(4,'Cho','Cho@naver.com','010-3333-3333','Cho.com','2020-03-19 23:58:50');
INSERT INTO "users" VALUES(5,'Yoo','Yoo@naver.com','010-4444-4444','Yoo.com','2020-03-19 23:58:50');
COMMIT;
