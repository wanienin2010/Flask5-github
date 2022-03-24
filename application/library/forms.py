from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, IntegerField
from wtforms.validators import DataRequired


class EditForm(FlaskForm):
    title=StringField('Title', validators=[DataRequired()])
    format=StringField('Format',validators=[DataRequired()])
    num_pages=StringField('Pages',validators=[DataRequired()])
    submit=SubmitField('Update')