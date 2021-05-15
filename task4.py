def func(*args):
    num = 0
    for i in args:
        try:
            num += i
        except:
            continue
    return num