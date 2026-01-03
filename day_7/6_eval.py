# author:R
# 2026年01月03日11时14分13秒

def read_conf():
    """
    读取配置
    :return:
    """

    file=open('file2',mode='r+',encoding='utf-8')
    text=file.read()
    print(type(text))
    my_dict=eval(text)
    print(type(my_dict))

if __name__ == '__main__':
    read_conf()
    print(eval('1+1'))