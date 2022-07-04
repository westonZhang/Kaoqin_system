import os.path
import sys

sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('./0-说明文档和配置文档'))
sys.path.append(os.path.abspath('./1-学生名单表'))
sys.path.append(os.path.abspath('./2-考勤结果'))
sys.path.append(os.path.abspath('./考勤程序'))
sys.path.append(os.path.abspath('./考勤程序/utils'))
from 考勤程序 import server, service
from 考勤程序.utils import file_utils

settings = file_utils.read_settings(os.getcwd() + "/0-说明文档和配置文档/配置文档.txt")


def init():
    """ 初始化:复制文件 """
    source_file = service.get_read_file()
    if not os.path.exists(file_utils.FILE_SAVE):
        file_utils.copy_file(source_file, file_utils.FILE_SAVE)


if __name__ == '__main__':
    init()
    server.app.run(host='0.0.0.0', port=5000, debug=True)
