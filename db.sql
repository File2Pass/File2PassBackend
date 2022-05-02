DROP DATABASE IF EXISTS `file2pass`;
CREATE DATABASE `file2pass`;
USE `file2pass`;

CREATE TABLE `project` (
  `id` INT AUTO_INCREMENT COMMENT "项目编号",
  `type` VARCHAR(25) NOT NULL COMMENT "项目类型",
  `summary` TEXT NOT NULL COMMENT "项目摘要",
  `name` VARCHAR(25) NOT NULL COMMENT "项目名称",
  `manager_id` INT NOT NULL COMMENT "项目负责人id",
  `unit_id` INT NOT NULL COMMENT "依托单位id",
  `text_id` int not null COMMENT "项目正文id",
  PRIMARY KEY(`id`)
) ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;

INSERT INTO project values(1, "一般项目", "本项目主要是为了帮助代价合理的学习计算机", "学习法则", 1, 1, 1);
INSERT INTO project values(2, "大型项目", "本项目主要是为了计算机的进阶学习的方式", "进阶学习", 2, 2, 2);

CREATE TABLE `manager` (
  `id` INT AUTO_INCREMENT COMMENT "项目负责人id",
  `name` VARCHAR(10) NOT NULL COMMENT "项目负责人姓名",
  `unit` VARCHAR(25) NOT NULL COMMENT "项目负责人目前所在单位",
  `position` VARCHAR(25) NOT NULL COMMENT "项目负责人目前职位",
  `gender` varchar(10) NOT NULL COMMENT "性别 0-男性 1-女性",
  `nationality` varchar(10) not null COMMENT "项目负责人的民族",
  `birthday` varchar(30) not null COMMENT "项目负责人的生日",
  `expertise` varchar(20) not null COMMENT "项目负责人的专长",
  `tutor` varchar(10) not null COMMENT "项目负责人担任的导师类型",
  `system` varchar(15) not null COMMENT "项目负责人所属的系统",
  PRIMARY KEY(`id`)
) ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;

INSERT INTO manager values(1, "张旷", "华中师范大学", "主任",  "男", "汉", "2002-5-1", "计算机", "硕士生导师", "教育系统");
INSERT INTO manager values(2, "张广", "华中科技大学", "主任",  "男", "汉", "2002-5-1", "计算机", "硕士生导师", "教育系统");

CREATE TABLE `unit` (
  `id` INT AUTO_INCREMENT COMMENT "依托单位id",
  `name` VARCHAR(10) NOT NULL COMMENT "依托单位名称",
  `phone` VARCHAR(30) NOT NULL COMMENT "依托单位的电话信息",
  `post` varchar(10) not null COMMENT "依托单位的邮政编码",
  `location` varchar(30) not null COMMENT "依托单位的地址",
  PRIMARY KEY(`id`)
) ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;

INSERT INTO unit values(1, "华中师范大学", "10068", "2245", "洪山去");
INSERT INTO unit values(2, "华中科技大学", "10068", "2245", "洪山去");

create table  `member_info` (
   `id` int AUTO_INCREMENT  COMMENT "成员id",
   `name` varchar(10) not null COMMENT "成员姓名",
   `gender` varchar(10) not null COMMENT "成员性别",
   `birthday` varchar(20) not null COMMENT "成员生日",
   PRIMARY KEY(`id`)
) ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;

INSERT INTO member_info values(1, "崔劲", "女", "2003-4-5");
INSERT INTO member_info values(2, "卢杰", "男", "2003-4-5");
INSERT INTO member_info values(3, "涛涛", "女", "2003-4-5");

create table `member2pro` (
    `id`  int AUTO_INCREMENT,
    `mid` int COMMENT "成员的id",
    `pid` int COMMENT "项目的id",
    PRIMARY KEY(`id`)
) ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;

INSERT INTO member2pro values(1,1,1);
INSERT INTO member2pro values(2,1,2);
INSERT INTO member2pro values(3,2,1);
INSERT INTO member2pro values(4,3,1);

create table `TextInfo` (
    `id` int AUTO_INCREMENT,
    `argument` text COMMENT "项目论证信息",
    `guarantee` text COMMENT "项目基础与保障",
    PRIMARY KEY(`id`)
) ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;

INSERT into TextInfo values(1, "好项目", "我们是一定能够完成的");
INSERT into TextInfo values(2, "大项目", "我们一定会全力以赴的去实现的");