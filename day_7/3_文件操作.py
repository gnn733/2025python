# author:R
# 2026年01月02日20时41分02秒
def open_r():
    file = open('file2', mode='r+', encoding='utf-8')
    text = file.readline()

    print(text)
    file.write('world')
    file.close()


def open_r_all():
    file = open('file2', mode='r+', encoding='utf-8')

    while True:
        text = file.readline()
        if not text:
            break
        print(text,end='')

    file.close()


def open_w():
    file = open('file2', mode='w', encoding='utf-8')  # 有则覆盖、无则创造
    file.write('123')
    file.close()


def open_a():
    file = open('file2', mode='a', encoding='utf-8')  # r+开头覆盖、a写在末尾
    file.write('aaaa')
    file.close()


if __name__ == '__main__':
    open_r_all()
