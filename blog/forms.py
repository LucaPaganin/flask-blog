from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired("Campo obbligatorio")])
    password = PasswordField('Password', validators=[DataRequired("Campo obbligatorio")])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')
    
class PostForm(FlaskForm):
    title = StringField("Titolo", 
                        validators=[DataRequired("Campo obbligatorio"), 
                                    Length(min=3, max=120, message="Assicurati che il titolo abbia tra i 3 e i 120 caratteri")]) 
    description = TextAreaField("Descrizione", 
                                validators=[Length(max=240, message="Assicurati che la descrizione non superi i 240 caratteri")])
    body = TextAreaField("Contenuto", 
                         validators=[DataRequired("Campo obbligatorio")])
    submit = SubmitField("Pubblica Post")
