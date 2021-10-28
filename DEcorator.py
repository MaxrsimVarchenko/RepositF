from datetime import datetime


def timit(arg):
    print(arg)
    def outer(func):
        def wap(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result
        return wap
    return outer


@timit('name')
def one(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    return l


@timit('name')
def second(n):
    l = [x for x in range(n) if x % 2 == 0]
    return l


one(10)


