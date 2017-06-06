# bashion_ktv
1.Django 1.10   Python2.7
2.在数据库中执行以下语句
CREATE TABLE `room`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `type` varchar(255) NOT NULL,
    `room_number` int(11) NOT NULL,
    `name` varchar(255) NOT NULL,
    PRIMARY KEY(`id`),
    UNIQUE KEY(`room_number`)
    )ENGINE=InnoDB DEFAULT CHARSET=UTF8;


CREATE TABLE `room_use_time`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `room_number` int(11) NOT NULL,
    `start_time` datetime(6) NOT NULL,
    `end_time` datetime(6) NOT NULL,
    PRIMARY KEY(`id`)
    )ENGINE=InnoDB DEFAULT CHARSET=UTF8;


CREATE TABLE `staff`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `staff_number` int(11) NOT NULL,
    `name` varchar(255) NOT NULL,
    `gender` int(1) NOT NULL,
    `age` int(11) NOT NULL ,
    `status` int(11) NOT NULL ,
    `join_time` datetime(6) NOT NULL,
    PRIMARY KEY(`id`)
    )ENGINE=InnoDB DEFAULT CHARSET=UTF8;


CREATE TABLE `order`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `room_number` int(11) NOT NULL,
    `fee` int(11) NOT NULL,
    `finish_time` datetime(6) NOT NULL,
    PRIMARY KEY(`id`)
    )ENGINE=InnoDB DEFAULT CHARSET=UTF8;

CREATE TABLE `user_room`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    'phone' int(11) NOT NULL,
    `start_time` datetime(11) NOT NULL,
    `end_time` datetime(6) NOT NULL,
    PRIMARY KEY(`id`)
    )ENGINE=InnoDB DEFAULT CHARSET=UTF8;

CREATE TABLE `room_reserve`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `room_number` int(11) NOT NULL,
    `type` varchar(255) NOT NULL,
    `name` varchar(255) NOT NULL,
    `current_use` int(1) NOT NULL,
    PRIMARY KEY(`id`)
    )ENGINE=InnoDB DEFAULT CHARSET=UTF8;

CREATE TABLE `room_call`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `room_number` int(11) NOT NULL,
    `call_time` datetime(6) NOT NULL,
    PRIMARY KEY(`id`)
    )ENGINE=InnoDB DEFAULT CHARSET=UTF8;

CREATE TABLE `songs`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `room_number` int(11) NOT NULL,
    `call_time` datetime(6) NOT NULL,
    PRIMARY KEY(`id`)
    )ENGINE=InnoDB DEFAULT CHARSET=UTF8;


CREATE TABLE `user_room`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `user_name` varchar(255) NOT NULL,
    `room_number` int(11) NOT NULL,
    `user_phone` varchar(255) NOT NULL,
    `start_time` varchar(255) NOT NULL,
    `end_time` varchar(255) NOT NULL,
    PRIMARY KEY(`id`)
    )ENGINE=InnoDB DEFAULT CHARSET=UTF8;