from wtforms import Form, BooleanField, StringField, PasswordField, validators

class CreateProfile(Form):
    name = StringField('Profile Name')
    