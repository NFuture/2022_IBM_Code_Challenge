from flask import Flask
from flask import render_template, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField, SelectField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from flask import request
import  random

app = Flask(__name__)

database = {
            '01': {
                    'Name': 'Noel Thekethala',
                    'blocked': False,
                    'class': 'Student',
                    'balance':  100,
                },
            '02': {
                'Name': 'Richard S',
                'blocked': False,
                'class': 'Farmer',
                'balance': 170,
            },
            '03': {
                'Name': 'Shimron Watiti',
                'blocked': False,
                'class': 'Disabled',
                'balance': 140,
            },
            '04': {
                'Name': 'Shimron Watiti',
                'blocked': False,
                'class': 'SeniorCitizen',
                'balance': 140,
            },
}
class RechargeForm(FlaskForm):
    card_no = IntegerField('card_no', validators=[DataRequired(), Length(min=16, max=16)])
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=30)])
    recharge_amount = IntegerField()
    submit = SubmitField('Register')

@app.route('/')
def home():  # put application's code here
    return render_template('index.html')

def recharge():
    if request.method =='GET':
        return render_template('recharge.html')
    else:
        form = RechargeForm(request.form)
        amount = form.get('recharge_amount')
        database[form.get('card_no')]['balance'] += amount
        return f' Recharged with {amount} Successfully'

def calculate_distance():
    form = RechargeForm(request.form)
    pickup_location = form.get('pickup')
    dropoff_location = form.get('dropoff')
    fair = random.randint(13, 50)
    temp = f'The Total amount to be paid is {fair}'

if __name__ == '__main__':
    app.run()

