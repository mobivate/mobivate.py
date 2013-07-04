import mobivate


def main():
    email = 'user@email.com'
    password = 'password'
    #m = mobivate.Api(email, password)
    m = mobivate.Api()
    m.send(originator='07855555555', recipient='447801234567', message='Hello world')

if __name__ == '__main__':
    main()