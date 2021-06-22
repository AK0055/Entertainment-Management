ENTERTAINMENT MANAGEMENT SYSTEM
19BPS1093
19BAInnnn
19BAInnnn
================================================================================
SQL QUERIES


 USE A1;
Database changed
 create table CLIENT(userID varchar(4) primary key not null unique,pwrd varchar(10) unique not null,name varchar(10) not null,dob date not null,
email varchar(10) unique not null,region varchar(10) not null,pref varchar(10) not null check(pref='a' or pref='m' or pref='both'),
pic_type varchar(5) not  null check(pic_type='FHD' or pic_type='UHD'));
Query OK, 0 rows affected (1.37 sec)

 DESC CLIENT;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| userID   | varchar(4)  | NO   | PRI | NULL    |       |
| pwrd     | varchar(10) | NO   | UNI | NULL    |       |
| name     | varchar(10) | NO   |     | NULL    |       |
| dob      | date        | NO   |     | NULL    |       |
| email    | varchar(10) | NO   | UNI | NULL    |       |
| region   | varchar(10) | NO   |     | NULL    |       |
| pref     | varchar(10) | NO   |     | NULL    |       |
| pic_type | varchar(5)  | NO   |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
 insert into CLIENT values('U001','1@Abc','James','2000-12-09','jam@g.com','UK','both','FHD');
Query OK, 1 row affected (0.10 sec)

 insert into CLIENT values('U002','2@ABc','Danny','1995-12-11','dan@r.com','US','m','UHD');
Query OK, 1 row affected (0.19 sec)

 insert into CLIENT values('U003','3@ABC','Raj','2005-12-11','raj@s.com','IND','a','UHD');
Query OK, 1 row affected (0.10 sec)

 insert into CLIENT values('U004','4@abC','Zoro','2001-12-25','zor@j.com','JAP','a','FHD');
Query OK, 1 row affected (0.18 sec)

 insert into CLIENT values('U005','5@aBc','Natasha','2002-03-21','nat@t.com','AUS','both','FHD');
Query OK, 1 row affected (0.09 sec)

 SELECT * FROM CLIENT;
+--------+-------+---------+------------+-----------+--------+------+----------+
| userID | pwrd  | name    | dob        | email     | region | pref | pic_type |
+--------+-------+---------+------------+-----------+--------+------+----------+
| U001   | 1@Abc | James   | 2000-12-09 | jam@g.com | UK     | both | FHD      |
| U002   | 2@ABc | Danny   | 1995-12-11 | dan@r.com | US     | m    | UHD      |
| U003   | 3@ABC | Raj     | 2005-12-11 | raj@s.com | IND    | a    | UHD      |
| U004   | 4@abC | Zoro    | 2001-12-25 | zor@j.com | JAP    | a    | FHD      |
| U005   | 5@aBc | Natasha | 2002-03-21 | nat@t.com | AUS    | both | FHD      |
+--------+-------+---------+------------+-----------+--------+------+----------+
5 rows in set (0.00 sec)

 create table TRANSACT(userID varchar(4) not null unique,AC_num integer(20) unique not null,pay_amt integer(5),pay_status varchar(10) not null check(pay_status='paid' or pay_status='notpaid'));
Query OK, 0 rows affected, 2 warnings (0.60 sec)

 desc transact;
+------------+-------------+------+-----+---------+-------+
| Field      | Type        | Null | Key | Default | Extra |
+------------+-------------+------+-----+---------+-------+
| userID     | varchar(4)  | NO   | PRI | NULL    |       |
| AC_num     | int(20)     | NO   | UNI | NULL    |       |
| pay_amt    | int(5)      | YES  |     | NULL    |       |
| pay_status | varchar(10) | NO   |     | NULL    |       |
+------------+-------------+------+-----+---------+-------+
4 rows in set (0.00 sec)

 create table ANIM(AID varchar(4) unique not null primary key,A_name varchar(20) unique not null,
A_genre varchar(10) not null,release_yr decimal(4,0) not null,sub_dub varchar(3) not null check(sub_dub="sub" or sub_dub="dub"),
score decimal(2,1) not null,rating varchar(5) not null check(rating in ('M','E','T')));
Query OK, 0 rows affected (1.82 sec)

 create table MOVIE(MID varchar(4) unique not null primary key,M_name varchar(20) unique not null,M_genre varchar(10) not null,release_date date not null,sub_dub varchar(3) not null check(sub_dub="sub" or sub_dub="dub"),score decimal(2,1) not null,rating varchar(5) not null check(rating in ('M','E','T')));
Query OK, 0 rows affected (1.79 sec)

 ALTER TABLE ANIM ADD(episodes integer(3) not null);
Query OK, 0 rows affected, 1 warning (1.92 sec)
Records: 0  Duplicates: 0  Warnings: 1

 desc anim;
+------------+--------------+------+-----+---------+-------+
| Field      | Type         | Null | Key | Default | Extra |
+------------+--------------+------+-----+---------+-------+
| AID        | varchar(4)   | NO   | PRI | NULL    |       |
| A_name     | varchar(20)  | NO   | UNI | NULL    |       |
| A_genre    | varchar(10)  | NO   |     | NULL    |       |
| release_yr | decimal(4,0) | NO   |     | NULL    |       |
| sub_dub    | varchar(3)   | NO   |     | NULL    |       |
| score      | decimal(2,1) | NO   |     | NULL    |       |
| rating     | varchar(5)   | NO   |     | NULL    |       |
| episodes   | int(3)       | NO   |     | NULL    |       |
+------------+--------------+------+-----+---------+-------+
8 rows in set (0.05 sec)

 desc movie;
+--------------+--------------+------+-----+---------+-------+
| Field        | Type         | Null | Key | Default | Extra |
+--------------+--------------+------+-----+---------+-------+
| MID          | varchar(4)   | NO   | PRI | NULL    |       |
| M_name       | varchar(20)  | NO   | UNI | NULL    |       |
| M_genre      | varchar(10)  | NO   |     | NULL    |       |
| release_date | date         | NO   |     | NULL    |       |
| sub_dub      | varchar(3)   | NO   |     | NULL    |       |
| score        | decimal(2,1) | NO   |     | NULL    |       |
| rating       | varchar(5)   | NO   |     | NULL    |       |
+--------------+--------------+------+-----+---------+-------+
7 rows in set (0.00 sec)

 insert into anim values('A001','Death note','mystery',2006,'dub',9.1,'T',37);
Query OK, 1 row affected (0.09 sec)

 insert into anim values('A002','DragonBallz','action',1986,'sub',8.4,'E',293);
Query OK, 1 row affected (0.23 sec)

 insert into anim values('A003','One Piece','adventure',1999,'sub',8.9,'T',915);
Query OK, 1 row affected (0.09 sec)

 insert into anim values('A004','FMA:B','thriller',2010,'dub',9.3,'E',64);
Query OK, 1 row affected (0.14 sec)

 insert into anim values('A005','One punch man','comedy',2017,'sub',9.2,'T',26);
Query OK, 1 row affected (0.09 sec)

 insert into anim values('A006','Code geass','war',2006,'sub',9.4,'T',25);
Query OK, 1 row affected (0.19 sec)

 insert into anim values('A007','My hero academia','fantasy',2015,'sub',8.3,'T',80);
Query OK, 1 row affected (0.09 sec)

 insert into anim values('A008','Naruto:Shippuden','drama',2007,'sub',9.0,'T',500);
Query OK, 1 row affected (0.19 sec)

 insert into anim values('A009','Attack on Titan','gore',2013,'dub',8.1,'M',59);
Query OK, 1 row affected (0.09 sec)

 insert into anim values('A010','Black clover','magic',2015,'sub',8.7,'E',114);
Query OK, 1 row affected (0.12 sec)

 SELECT * FROM ANIM;
+------+------------------+-----------+------------+---------+-------+--------+----------+
| AID  | A_name           | A_genre   | release_yr | sub_dub | score | rating | episodes |
+------+------------------+-----------+------------+---------+-------+--------+----------+
| A001 | Death note       | mystery   |       2006 | dub     |   9.1 | T      |       37 |
| A002 | DragonBallz      | action    |       1986 | sub     |   8.4 | E      |      293 |
| A003 | One Piece        | adventure |       1999 | sub     |   8.9 | T      |      915 |
| A004 | FMA:B            | thriller  |       2010 | dub     |   9.3 | E      |       64 |
| A005 | One punch man    | comedy    |       2017 | sub     |   9.2 | T      |       26 |
| A006 | Code geass       | war       |       2006 | sub     |   9.4 | T      |       25 |
| A007 | My hero academia | fantasy   |       2015 | sub     |   8.3 | T      |       80 |
| A008 | Naruto:Shippuden | drama     |       2007 | sub     |   9.0 | T      |      500 |
| A009 | Attack on Titan  | gore      |       2013 | dub     |   8.1 | M      |       59 |
| A010 | Black clover     | magic     |       2015 | sub     |   8.7 | E      |      114 |
+------+------------------+-----------+------------+---------+-------+--------+----------+
10 rows in set (0.00 sec)

 insert into movie values('M001','Knives Out','mystery','2019-11-29','dub',8.1,'E');


 insert into movie values('M002','Ford V Ferrari','sport','2019-11-15','dub',8.3,'E');


 insert into movie values('M003','Joker','thriller','2019-10-02','dub',8.7,'M');


 insert into movie values('M004','John Wick 3','action','2019-05-09','sub',7.5,'T');


 insert into movie values('M005','Frozen 2','drama','2019-11-22','dub',7.2,'E');


 insert into movie values('M006','STAR WARS IX','action','2019-12-20','dub',6.9,'E');


 insert into movie values('M007','Avengers Endgame','sci-fi','2019-04-26','sub',8.5,'E');


 insert into movie values('M008','Spiderman FFH','fantasy','2019-06-26','sub',7.6,'E');


 insert into movie values('M009','1917','drama','2019-12-25','dub',8.7,'M');


 insert into movie values('M010','Spies in disguise','spy','2019-12-25','dub',8.8,'E');


 SELECT * FROM movie;
+------+-------------------+----------+--------------+---------+-------+--------+
| MID  | M_name            | M_genre  | release_date | sub_dub | score | rating |
+------+-------------------+----------+--------------+---------+-------+--------+
| M001 | Knives Out        | mystery  | 2019-11-29   | dub     |   8.1 | E      |
| M002 | Ford V Ferrari    | sport    | 2019-11-15   | dub     |   8.3 | E      |
| M003 | Joker             | thriller | 2019-10-02   | dub     |   8.7 | M      |
| M004 | John Wick 3       | action   | 2019-05-09   | sub     |   7.5 | T      |
| M005 | Frozen 2          | drama    | 2019-11-22   | dub     |   7.2 | E      |
| M006 | STAR WARS IX      | action   | 2019-12-20   | dub     |   6.9 | E      |
| M007 | Avengers Endgame  | sci-fi   | 2019-04-26   | sub     |   8.5 | E      |
| M008 | Spiderman FFH     | fantasy  | 2019-06-26   | sub     |   7.6 | E      |
| M009 | 1917              | drama    | 2019-12-25   | dub     |   8.7 | M      |
| M010 | Spies in disguise | spy      | 2019-12-25   | dub     |   8.8 | E      |
+------+-------------------+----------+--------------+---------+-------+--------+
10 rows in set (0.00 sec)

