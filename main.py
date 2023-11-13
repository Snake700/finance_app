# 1 регистрация и авторизация
# 2 app_financy -> main.py, users.txt(login:password)
# пароль больше 4 цифр, + буквы
# логин без двоеточия,  4 символа

def user_info():
    users = []
    with open('users.txt', 'r') as file:
        lst = file.readlines()
        for i in lst:
                i = i[:-1]
                users.append(i)
        log_and_password = []
        users_login = []
        users_password  =[]
        for log in users:
            log_and_password.append(log.split(':'))#логины и пароли

        for i in log_and_password:
            users_login.append(i[0])#список логинов
        for i in log_and_password:
            users_password.append(i[1])#список паролей

        return users_login,users_password

def register(user_login, user_password):
    users_login, users_password = user_info()
    if user_login in users_login and user_password in users_password:
         print('\nУ вас уже есть аккаунт.')
         print('Вам нужно авторизироваться.\n')
         print(login(input('Введите логин: '), input('Введите пароль: ')))

    else:
        while True:
            if len(user_login) >= 4 and user_login.find(':') == -1 and len(user_password) >= 4 and user_password.isalnum():
                    with open('users.txt', 'a') as file:
                        file.write(f'{user_login}:{user_password}\n')
                        print('Вы зарегистрированы!\n')
                        break

            else:
                print('Тип пароля или логина неверный.')
                user_login = input('Введите корректный логин: ')
                user_password = input('Введите корректный пароль: ')

def login(user_login, user_password):
    users_login, users_password = user_info()
    if user_login in users_login and user_password in users_password:
        message = 'Вы успешно авторизировались!'
        return message
    else:
        print('Вы не зарегистрированы. Просим вас пройти регистрацию.\n')
        register(input('Введите логин: '), input('Введите пароль: '))
    # print(users_login)
    # print(users_password)

    
question_1 = input('У вас есть аккаунт? (y/n): ')
if question_1 == 'n':
    print('Вам нужно создать аккаунт')
    result = register(input('Введите логин: '), input('Введите пароль: '))
else:
    print('Вам нужно войти в аккаунт')
    print(login(input('Введите логин: '), input('Введите пароль: ')))

