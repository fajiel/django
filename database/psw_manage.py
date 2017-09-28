import hashlib
from database.manage import Session
from database.models import AmazonUser

class PassWordManage():
    def __init__(self):
        self.key = 'the_key_you_design'
        self.session = Session()

    def md5(self, arg):
        md5_pwd = hashlib.md5(bytes(self.key, encoding='utf-8'))
        md5_pwd.update(bytes(arg, encoding='utf-8'))
        return md5_pwd.hexdigest()

    def login(self, name, pwd):
        name = name.lower()
        query = self.session.query(AmazonUser.name, AmazonUser.password)
        query_obj = query.filter_by(name=name, password=self.md5(pwd)).first()
        if query_obj:
            return True
        else:
            return False

    def register(self, name, pwd, level):
        query = self.session.query(AmazonUser.name)
        query_obj = query.filter_by().first()
        if query_obj and query_obj.name == name.lower():
            print("This account exists in database, change mail please!")
            return None

        item_dict = {
            "name": name.lower(),
            "password": self.md5(pwd),
            "level": level,
        }
        reg_item = AmazonUser(**item_dict)
        self.session.add(reg_item)
        self.session.commit()
        self.session.close()
