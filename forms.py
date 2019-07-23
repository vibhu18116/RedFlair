from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import URL


class AcceptURL(FlaskForm):

	url = StringField('Enter the Post URL', validators = [URL(require_tld=True, message="Enter valid URL")])

	submit = SubmitField('Find Flair')