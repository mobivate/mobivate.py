import mobivate


def main():
    email = 'test@test1.com'
    password = 'password'
    m = mobivate.Api(email, password)
    print m.send(originator='07811111111', recipient='447800000000', message='Hello world!')

if __name__ == '__main__':
    main()