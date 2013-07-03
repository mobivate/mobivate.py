import mobivate

def main():
    email = '87742579@mailinator.com'
    password = 'KWsgUeOrOtAmfkjT'
    m = mobivate.Api(email, password)
    print m.send('Hello world')


if __name__ == '__main__':
    main()