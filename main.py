class User():
    def __init__(self, id, name, account):
        self.id = id
        self.name = name
        self.account = account



class Admin (User):
    def __init__(self,id, name, account, adm_account):
        super().__init__(id, name, account)
        self.adm_account = {}

    def add_user (self):
        self.adm_account[self.name] = 'User account'
        print(f"{self.name} got an account")

    def remove_user(self):
        if self.name in self.adm_account:
            del self.adm_account[self.name]
            print(f"{self.name} was removed from the list")
        else:
            print(f"{self.name}is not found in the list")


admin1 = Admin(14,"Thomas", "AB14","Admin14")
admin2 =Admin(18,"Wolfram","BC18", "Admin18")

user1 = User("17","Ivan","useraccount1")

admin1.add_user()
admin2.add_user()









