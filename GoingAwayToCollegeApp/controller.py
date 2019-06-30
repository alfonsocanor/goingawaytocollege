from model import Session, Profile, Usuario
from marshmallow import Schema, fields
import json

#Schema is used for retriving information from the DB and 
# then transform the data into JSON formatting
class ProfileSchema(Schema):
    id = fields.Number()
    name = fields.Str()

session = Session()

class profileDML():
    initialId = 'p00'
    def create(name):
        currentProfiles = session.query(Profile).all()
        #From the Class ProfileSchema
        schema = ProfileSchema(many=True)
        profiles = schema.dump(currentProfiles).data

        for p in json.loads(json.dumps(profiles)):
            print(p.get('name'))

        profile = Profile(name)
        session.add(profile)
        session.commit()

    def createMultiples(self, name):
        profile = Profile(name)
        session.add(profile)
        session.commit()