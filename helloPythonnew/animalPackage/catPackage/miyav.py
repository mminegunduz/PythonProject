def speak():
    print("meow direct")


def speak2():
    print("meow imported")

if __name__ == '__main__':
    speak()
else:
    speak2()