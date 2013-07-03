import mobivate

def main():
    email = 'carl000@gmail.net'
    password = 'password'
    m = mobivate.Api(email, password)
    print m.send('Hello world')


if __name__ == '__main__':
    main()