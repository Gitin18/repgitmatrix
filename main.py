class User():
    def __init__(self, id, name, account):
        self.id = id
        self.name = name
        self.account = account

class Admin (User):
    def __init__(self,id,name,account, adm_account):
        super().__init__(id,name,account)
        self.adm_account =  []

    