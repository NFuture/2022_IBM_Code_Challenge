from flask import Flask
from flask import render_template, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField, SelectField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from flask import request
import  random

app = Flask(__name__)

database = {
            '000000001': {
                    'Name': 'Noel Thekethala',
                    'blocked': False,
                    'class': 'Student',
                    'balance':  100,
                },
            '000000002': {
                'Name': 'Richard S',
                'blocked': False,
                'class': 'Farmer',
                'balance': 170,
            },
            '00000003': {
                'Name': 'Shimron Watiti',
                'blocked': False,
                'class': 'Disabled',
                'balance': 140,
            },
            '000000004': {
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
    submit = SubmitField('Submit')

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
        return render_template('recharge_successful.html')

def calculate_distance():

    if request.method == 'GET':
        pass
    else:
        form = RechargeForm(request.form)
        pickup_location = form.get('pickup')
        dropoff_location = form.get('dropoff')
        # Random function because we had no time to setup a system to determine the fair prices for this demonstration.
        fair = random.randint(13, 50)
        temp = f'The Total amount to be paid is {fair}'
        database[form.get('card_no')]['balance'] -= fair
        return render_template('fair_price.html', fair=fair)

if __name__ == '__main__':
    app.run()
