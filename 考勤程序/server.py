import os.path

from flask import Flask, redirect, request, render_template, url_for, send_from_directory
import service

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 解决flask接口中文数据编码问题


@app.route('/get_courses/')
def get_courses():
    """ 获取科目 """
    ccs_info = service.read_cs()  # 班级和学生信息
    if not ccs_info:
        return "目录中没有可读取文件，或者不是'xlsx'文件，请联系联想班学员帮您解决问题 ^_^"
    return {"courses": list(ccs_info.keys())}  # 课程：如政治、语文


@app.route("/get_classes/<course>/")
def get_classes(course):
    """ 根据科目，获取它对应的哪些班级 """
    ccs_info = service.read_cs()  # 科目、班级和学生信息
    if not ccs_info:
        return "目录中没有可读取文件，或者不是'xlsx'文件，请联系联想班学员帮您解决问题 ^_^"
    cs_info = ccs_info.get(course)  # 班级、学生信息
    if not cs_info:
        return "目录中没有可读取文件，或者不是'xlsx'文件，请联系联想班学员帮您解决问题 ^_^"
    d = {"course": course, "classes": list(cs_info.keys())}
    return d


@app.route('/get_cls_students/<cls>/')
def get_cls_students(cls):
    """ 获取某班级的学生名单 """
    data = {"classes": cls, "students": []}  # 班级、学生名单
    ccs_info = service.read_cs()  # 科目、班级和学生信息
    if not ccs_info:
        return "目录中没有可读取文件，或者不是'xlsx'文件，请联系联想班学员帮您解决问题 ^_^"
    for course, cs_info in ccs_info.items():
        if cls in list(cs_info.keys()):
            data["students"] = cs_info[cls]
            return data
    return data


@app.route('/')
@app.route('/home/')
def home():
    """ 主页 """
    course = request.args.get("course")
    courses = get_courses().get('courses')  # 获取所有科目
    if not course:
        course = courses[0]

    data = {
        "description": service.get_desc(),  # 设置文件中的"介绍信息"
        "settings": service.get_settings(),  # 读取设置信息
        "cls_imgs": service.get_imgs(),  # 班级图片
        "stu_img_dict": service.get_imgs("student"),  # 学生的图片
        "student_intro_dict": service.read_students_introduction()  # 学生的简介
    }
    return render_template('home.html', data=data)


@app.route('/kaoqin/')
def kaoqin():
    """ 科目的考勤 """
    course = request.args.get("course")
    courses = get_courses().get('courses')  # 获取所有科目
    if not course:
        course = courses[0]

    data = {
        "courses": courses,  # 所有课程
        "course": course,  # 当前请求的课程
        "cs_info": service.read_cs()[course],  # 班级和学生信息
        "kaoqin": service.all_situation(),  # 考勤的所有情况
        "classes": get_classes(course)["classes"],
        "lessons": service.get_lessons()
    }
    return render_template('kaoqin.html', data=data)


@app.route('/submit_kq/<course>/', methods=['GET', "POST"])
def submit_kq(course):
    """ 考勤数据的提交 """
    if request.method == "POST":
        kaoqin_info = request.form.to_dict()
        kaoqin_info['course'] = course
        # 将数据保存到excel
        service.save_kaoqin_data(kaoqin_info)
        return redirect(url_for('kaoqin'))
    return """<script>alert("现在是get请求，请求有误，请联系联想班学员处理。")</script>"""


@app.route("/settings/", methods=["POST"])
def submit_settings():
    """ 接收提交的配置信息，并保存到配置文件中 """
    old_sett = service.get_settings()  # 读取原配置，方便后面做对比
    if request.method == "POST":
        new_sett = request.form.to_dict()
        # 判断原设置数据和提交上来的配置数据是否相同
        # 如果不同，则按照提交配置进行更改
        for k, v in new_sett.items():
            # 如果配置相同，则无需更改，跳过
            if old_sett[k].replace('\n', "") == new_sett[k].replace('\r', "").replace('\n', ""):
                continue
            # 不同的数据，判断是哪些地方不同
            # 如果是考勤情形不同，则修改考勤内容
            # 如果是上课情形不同，则修改上课情形
            service.save_setting(old_sett[k], v)
    return redirect(url_for('home'))


@app.route('/random_choice/')
def random_choice():
    """ 随机点名 """
    # todo 未完成
    course = request.args.get("course")
    courses = get_courses().get('courses')  # 获取所有科目
    if not course:
        course = courses[0]

    data = {
        "courses": courses,  # 所有课程
        "course": course,  # 当前请求的课程
        "cs_info": service.read_cs()[course],  # 班级和学生信息
        "kaoqin": service.all_situation(),  # 考勤的所有情况
        "classes": get_classes(course)["classes"],
        "lessons": service.get_lessons()
    }
    return render_template('random_choice.html', data=data)


@app.route('/download_file/')
def download_file():
    """ 下载模版文件 """
    # path = os.path.abspath('.') + '/1-学生名单表/学生名单.xlsx'
    # return send_from_directory(path, filename="学生名单.xlsx", as_attachment=True)
    # todo


@app.route('/upload_file/')
def upload_file():
    """ 上传文件 """
    pass
    # todo
