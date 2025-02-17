create database hotel;

use hotel;

create table roommaster
(
    roomno int(3) primary key,
    roomtype varchar(15),
    charges decimal(10,2),
    status varchar(20)
);

create table checkin
(
    roomno int(3),
    customername varchar(30),
    phone varchar(15),
    checkindate date,
    status varchar(30)
);

create table checkout
(
    roomno int(3),
    customername varchar(30),
    checkindate date,
    checkoutdate date,
    nodays int(3),
    roomchargesperday decimal(8,2),
    totalcharges decimal(8,2)
 );

 insert into roommaster values(1,'AC',5000,'Vacant');
 insert into roommaster values(2,'NON AC',2000,'Vacant');
 insert into roommaster values(3,'Super Deluxe',9000,'Vacant');
 insert into roommaster values(4,'AC',5000,'Vacant');
 insert into roommaster values(5,'Super Deluxe',9000,'Vacant');

 select customername,checkindate,datediff(curdate(),checkindate),charges,datediff(curdate(),checkindate)*charges
 from roommaster,checkin
 where roommaster.roomno = checkin.roomno and status = 'Occupied' and checkin.roomno = 5;
