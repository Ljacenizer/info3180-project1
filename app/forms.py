from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class PropertyForms(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    roomnum = StringField('Room Number', validators=[InputRequired()])
    bathnum = StringField('Bathroom Number', validators=[InputRequired()])
    property = SelectField('Property Type', choices=[('house', 'House'), ('apartment', 'Apartment')])
    location = StringField('Location', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])

class UploadForm(FlaskForm):
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg','png'], 'Images only!')])