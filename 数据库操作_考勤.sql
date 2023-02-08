-- 创建数据库：teach_manage_system
create database if not exists teach_manage_system default character set "utf8";
use teach_manage_system;

-- 创建表：students、subjects、kq_results
/*
students：id、姓名name、性别、专业major、班级cls、创建时间create_time
subjects：id、科目subject、班级cls
kq_results：id、班级cls、姓名name、考勤结果kq_res、日期date、周几weekday、第几节课cls_num
*/
create table if not exists students(
    id          int         not null primary key auto_increment comment "id",
    name        varchar(32) not null comment "姓名",
    age         tinyint     not null default 18 comment "年龄",
    gender      tinyint     not null default 1 comment "性别：1男生，2女生",
    cls         varchar(32) not null comment "班级",
    major       varchar(32) default "大数据" not null comment "专业",
    create_time datetime    default now() comment "创建时间"
);

create table if not exists subjects(
    id          int         not null primary key auto_increment comment "id",
    subject     varchar(32) not null comment "科目",
    cls         varchar(32) not null comment "班级",
    major       varchar(32) default "大数据" not null comment "专业",
    create_time datetime    default now() comment "创建时间"
);

create table if not exists kq_results(
    id          int         not null primary key auto_increment comment "id",
    cls         varchar(32) not null comment "班级",
    student     varchar(32) not null comment "姓名",
    kq_res      varchar(32) not null comment "考勤结果",
    kq_date     TIMESTAMP   default now() comment "创建时间",
    weekday     varchar(32) not null comment "周几",
    cls_num     varchar(32) not null comment "第几节课",
    create_time datetime    default now() comment "创建时间"
);

-- 删除表
-- drop table kq_results;
-- drop table students;
-- drop table subjects;

-- 插入数据
insert into students(`name`, `gender`, `cls`)
values 
("崔昊元",2, "1班"),
("贾靖程",2, "1班"),
("吴俊岳",1, "1班"),
("王浩羽",1, "1班"),
("吕梦丽",2, "1班"),
("牛皓冬",1, "1班"),
("张阔",1, "1班"),
("孙佳奇",1, "1班"),
("郑佳睦",1, "1班"),
("王孝天",1, "1班"),
("付一鸣",1, "1班"),
("李蓉轩",2, "1班"),
("陈观绅",1, "1班"),
("赵鑫博",1, "1班"),
("张子豪",1, "1班"),
("叶平",1, "1班"),
("李博远",1, "1班"),
("侯文杰",1, "2班"),
("黄新之",1, "2班"),
("杨智恒",1, "2班"),
("杨悦昕",1, "2班"),
("刘洋",1, "2班"),
("靳馨娴",1, "2班"),
("白轶臣",1, "2班"),
("蒋文拓",1, "2班"),
("赵梓豪",1, "2班"),
("杨梓琦",1, "2班"),
("吕铭",1, "2班"),
("刘子豪",1, "2班");

