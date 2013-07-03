import mobivate

def main():
    email = 'myname@gmail.com'
    password = 'password'
    m = mobivate.Api(email, password)
    print m.send('Hello world')


if __name__ == '__main__':
    main()