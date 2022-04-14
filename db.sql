DROP DATABASE IF EXISTS `file2pass`;
CREATE DATABASE `file2pass`;
USE `file2pass`;
CREATE TABLE `project` (
  `id` INT AUTO_INCREMENT COMMENT "项目编号",
  `type` VARCHAR(25) NOT NULL COMMENT "项目类型",
  `summary` TEXT NOT NULL COMMENT "项目摘要",
  `name` VARCHAR(25) NOT NULL COMMENT "项目名称",
  `manager_id` INT NOT NULL COMMENT "项目负责人id",
  `uint_id` INT NOT NULL COMMENT "依托单位id",
  `expected_performance_id` INT NOT NULL COMMENT "项目的预期信息id",
  `content` TEXT NOT NULL COMMENT "项目正文",
  PRIMARY KEY(`id`)
) ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;
CREATE TABLE `manager` (
  `id` INT AUTO_INCREMENT COMMENT "项目负责人id",
  `name` VARCHAR(10) NOT NULL COMMENT "项目负责人姓名",
  `unit` VARCHAR(25) NOT NULL COMMENT "项目负责人目前所在单位",
  `position` VARCHAR(25) NOT NULL COMMENT "项目负责人目前职位",
  `sex` TINYINT(1) NOT NULL COMMENT "性别 0-男性 1-女性",
  PRIMARY KEY(`id`)
) ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;
CREATE TABLE `uint` (
  `id` INT AUTO_INCREMENT COMMENT "依托单位id",
  `name` VARCHAR(10) NOT NULL COMMENT "依托单位名称",
  `location` VARCHAR(30) NOT NULL COMMENT "依托单位所属地",
  PRIMARY KEY(`id`)
) ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;
CREATE TABLE `expected_performance` (
  `id` INT AUTO_INCREMENT COMMENT "依托单位id",
  `name` VARCHAR(10) NOT NULL COMMENT "依托单位名称",
  `expenses` DOUBLE NOT NULL COMMENT "项目经费",
  `deadline` DATETIME NOT NULL COMMENT "项目预期的完成时间",
  PRIMARY KEY(`id`)
) ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;