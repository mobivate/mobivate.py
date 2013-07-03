from mobivate import Mobivate


def main():
    email = '87742579@mailinator.com'
    password = 'KWsgUeOrOtAmfkjT'
    m = Mobivate(email, password)
    print m.send('Hello world')


if __name__ == '__main__':
    main()