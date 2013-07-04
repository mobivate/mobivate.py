import mobivate
import time


def main():
    email = ''
    password = ''
    #m = mobivate.Api(email, password)
    options = {
        'proxy': True
    }
    m = mobivate.Api(options=options)
    m.send(originator='07822222222', recipient='447811111111', message="Hello world.")

if __name__ == '__main__':
    main()