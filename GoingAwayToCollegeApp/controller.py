from model import Session, Profile, Usuario

session = Session()
print('What is the value of session: ' + str(session))
print(dir(session))
class profileDML():
    def create(name):
        profile = Profile(name)
        session.add(profile)
        session.commit()

    def createMultiples(self, name):
        profile = Profile(name)
        session.add(profile)
        session.commit()