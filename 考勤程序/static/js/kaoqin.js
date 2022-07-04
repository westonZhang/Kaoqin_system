/*globals $:false */

// 选择班级的复选框的点击事件
function checkboxOnclick(checkbox, cls) {
    "use strict";
    if (checkbox.checked === true) {
        show_students(cls);
    } else {
        remove_students(cls);
    }
}

// 显示学生
function show_students(cls) {
    "use strict";
    var req = new XMLHttpRequest();  // 1 创建对象
    req.open("GET", "http://127.0.0.1:5000/get_cls_students/" + cls + "/");  // 2 初始化
    req.send();  // 3 发送
    /*
    * 页面发送出请求后，往往无法得知什么时候才能完成这个请求并获得回应，所以要使用一个事件机制来捕获请求完成的状态。
    * XmlHttpRequest对象的onreadystatechange函数就实现了此功能。
    * */
    req.onreadystatechange = function () {  // 4 时间绑定
        // req.readyState=4 表示数据解析完毕，可以通过XMLHttpRequest对象的相应属性取得数据。
        if (req.readyState === 4 && this.status === 200) {
            var res = JSON.parse(req.response);  // 将字符串类型转为json类型
            var students = res.students;
            //获取标签名字为tbody的第一个标签，并将其赋值给tbody
            var tbody = document.getElementsByTagName("tbody")[0];
            for (var i = 0; i < students.length; i++) {
                var name = students[i];
                var newTr = tbody.firstElementChild.cloneNode(true); // 产生一个tr
                newTr.removeAttribute("style");
                newTr.children[0].innerHTML = cls;  // 第一个表格中填班级
                newTr.children[1].innerHTML = name;  // 第二个表格中填学生姓名
                newTr.children[2].children[0].children[0].setAttribute("name", "kq-" + cls + "-" + name);  // 设置select标签的name属性
                tbody.appendChild(newTr);
            }
        }
    };
}

// 移除学生
function remove_students(cls) {
    "use strict";
    var tbody = document.getElementById("tbody");
    var rows = tbody.rows;
    var len = rows.length;
    for (var i = len - 1; i >= 1; i--) {
        var now_row = rows[i];
        var cells = now_row.cells;
        var table_cls = cells[0].firstChild.nodeValue;  // 班级
        var table_student = cells[1].firstChild.nodeValue;  // 学生姓名
        if (cls === table_cls) {
            tbody.deleteRow(i);  // 移除行
        }
    }
}

function submitClick(s) {
    "use strict";
    window.alert(s);
}
