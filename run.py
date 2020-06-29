from user import User
from credential import Credential
##Creating user


def create_user(fname, lname, phone, password):

    new_user = User(fname, lname, phone, password)
    return new_user
##Save user


def save_users(user):

    user.save_user()
##Delete users


def del_user(user):

    user.delete_user()
##Find users


def find_user(name):

    return User.find_by_name(name)
##Check if a user exists


def check_existing_users(name):

    return User.user_exist(name)
##Displaying all users


def display_users():

    return User.display_users()
##Login 
def user_log_in(name, password):
    '''
    Function that allows a user to log into their credential account
    Args:
        name : the name the user used to create their user account
        password : the password the user used to create their user account
    '''
    log_in = User.log_in(name, password)
    if log_in != False:
        return User.log_in(name, password)

##Main function


def main():
    print("Welcome to your  password locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
                    print(
                        "Use these short codes : cu - create a new user, du - display users, fu -find a user,lu - log users ,ex -exit the users list ")

                    short_code = input().lower()

                    if short_code == 'cu':
                            print("New Credentials")
                            print("-"*10)

                            print("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Username ...")
                            p_name = input()

                            print("password ...")
                            u_name = input()

                            # create and save new contact.
                            save_users(create_user(
                                f_name, l_name, p_name, u_name))


                            print('\n')
                            print(f"New User {f_name} {l_name} created")
                            print('\n')

                    elif short_code == 'du':

                            if display_users():
                                    print("Here is a list of all your users")
                                    for user in display_users():
                                            print(
                                                f"{user.first_name} {user.last_name} .....{user.username}")
                            else:
                                    print("You dont seem to have any users saved yet")
                                    ####
                    elif short_code == 'lu':
                                    print("Log into Password Locker Account")
                                    print("Enter the user name")
                                    username = input()
                                    if user_log_in(username,u_name) == "":
                                        print("Please try again or create an account")
                                    else:
                                        user_log_in(username,u_name)
                                        print(f'''{username} welcome to your Credentials
                                        Use these short codes to get around''')
                                        print("Enter the password")
                                        u_name = input()

                                        

                    elif short_code == 'fu':

                            print("Enter the username you want to search")

                            search_name = input()
                            if check_existing_users(search_name):
                                    search_user = find_user(search_name)
                                    print(
                                        f"{search_user.first_name} {search_user.last_name}")
                                    print('-' * 20)

                                    print(
                                        f"Username.......{search_user.username}")
                                    print(
                                        f"Password.......{search_user.password}")
                            else:
                                    print("The user does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print(
                                "I didn't get what you typed. Please use short codes")

if __name__ == '__main__':

    main()
