class User:
    """
    Class User allow users to create user accounts, delete user accounts, validate sign up, validate
    login process and to render feedback messages inform of a dictionary
    """

    # Declaring static variables
    users = {}

    # Initializing  class instance variables
    def __init__(self):

        self.name = None
        self.email = None
        self.password = None

    # defining method to create account
    def create_account(self, name, email, passwd, c_passwd):

        # validating parameters to make sure none is empty
        if name is not None and name != '' and passwd is not None and passwd != '' and c_passwd is not None:
            if email is not None and email != '':

                if email not in self.users.keys():

                    if passwd == c_passwd:

                        self.name = name
                        self.email = email
                        self.password = passwd

                        self.save_data()

                        return self.users
                    else:
                        msg = {
                            'error': "Password Mismatch"
                        }
                else:
                    msg = {
                        'error': "User already Exist. Please Login"
                    }
            else:
                msg = {
                    'error': "Fill all Fields"
                }
        else:
            msg = {
                'error': "Fill all Fields"
            }
        return msg

    # defining method to delete a user account
    def del_account(self, email):

        msg = {
            'error': "Sorry, could not delete your account",
        }

        if email in self.users.keys():
            self.users.pop(email)
            msg = {
                'success': "You have successfully deleted your account",
            }
        return msg

    # defining method to validate credentials for login purpose
    def login(self, email, passwd):
        msg = {
            'error': 'Incorrect Login'
        }
        if email is None or email == '' or passwd is None or passwd == '':
            msg = {
                'error': 'Fill all Fields'
            }

        if email in self.users.keys():
            res = self.users[email]
            password = res['pass']

            if passwd == password:
                return self.users

        return msg

    # defining helper method to save user data to a dictionary
    def save_data(self):

        self.users[self.email] = {
            'name': self.name,
            'email': self.email,
            'pass': self.password,
        }
