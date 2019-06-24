from model import Session, Profile, Usuario
from marshmallow import Schema, fields
import json

class TestSchema(Schema):
    id = fields.Number()
    name = fields.Str()

session = Session()

class profileDML():
    def create(name):
        currentProfiles = session.query(Profile).all()
        schema = TestSchema(many=True)
        profiles = schema.dump(currentProfiles).data
        print(type(profiles))
        print(profiles)
        print(type(json.dumps(profiles)))
        print(json.dumps(profiles))
        print(type(json.loads(json.dumps(profiles))))
        print(json.loads(json.dumps(profiles)))

        for p in json.loads(json.dumps(profiles)):
            print(p.get('name'))

        profile = Profile(name)
        session.add(profile)
        session.commit()


    def createMultiples(self, name):
        profile = Profile(name)
        session.add(profile)
        session.commit()