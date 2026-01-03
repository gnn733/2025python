# author:R
# 2026年01月03日09时35分30秒
import os


def seek_start():
    """
    相对于开头进行偏移
    :return:
    """
    file = open('file1', mode='r+', encoding='utf8')
    file.seek(6, os.SEEK_SET)  # 汉字的偏移是3B的整数倍
    text = file.read(5)
    print(text)
    file.close()


def seek_end():
    """
        相对于末尾进行偏移
        :return:
        """
    file = open('file1', mode='r+', encoding='utf8')
    file.seek(0, os.SEEK_END)
    text = file.read(5)
    print(text)  # 读不到文件内容
    file.close()


def seek_cur():
    """
        相对于当前位置进行偏移
        :return:
        """
    file = open('file1', mode='r+', encoding='utf8')
    file.seek(0, os.SEEK_CUR)
    text = file.read(5)
    print(text)  # 读不到文件内容
    file.close()


def seek_b_cur():
    file = open('file1', mode='rb+')
    text = file.read()
    print(text)  # 得到的是字节流
    file.close()


def copy_file():
    file_1 = open('img.png', mode='rb+')
    file_2 = open('copy_file.png', mode='wb')
    b = file_1.read()
    file_2.write(b)
    file_1.close()
    file_2.close()

if __name__ == '__main__':
    copy_file()
