# author:R
# 2026年01月03日10时08分25秒
import os


def use_rename():
    os.rename('dir\\file_3', 'dir\\file')


def use_dir_func():
    file_list = os.listdir('.')
    print(file_list)

    # os.mkdir('dir2')
    # os.rmdir('dir')
    print(os.getcwd())

    os.chdir('dir2')
    file = open('file1', mode='w', encoding='utf-8')
    file.close()


def use_chdir():
    print(os.getcwd())
    os.chdir('dir2')
    print(os.getcwd())


def scan_dir(num, current_dir):
    """
    目录深度优先遍历
    :param current_dir:
    :return:
    """
    file_list = os.listdir(current_dir)
    for file in file_list:
        for i in range(num):
            print('    ', end='')
        new_path = current_dir + '/' + file
        print(new_path)
        if os.path.isdir(new_path):
            scan_dir(num + 1, new_path)


def use_stat(file_path):
    file_info=os.stat(file_path)
    print('size{},uid{},mode{:x},mtime{}'.format(file_info.st_size, file_info.st_uid, file_info.st_mode, file_info.st_mtime))
    from time import strftime
    from time import gmtime
    # 把秒数转为字符串时间
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime(file_info.st_mtime)))

if __name__ == '__main__':
        use_stat('file2')
