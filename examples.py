import mobivate
import time

def main():
    email = 'user@email.com'
    password = 'password'
    #m = mobivate.Api(email, password)
    options = {
        'proxy': True
    }
    m = mobivate.Api(options=options)
    m.send(originator='07888888888', recipient='44781111111', message='Hello world')

if __name__ == '__main__':
    main()