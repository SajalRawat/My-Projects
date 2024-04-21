def findtime():
    import time
    a = time.asctime(time.localtime())
    d = a[4:11]
    b = a[20:24]
    return (f"{d}{b}")