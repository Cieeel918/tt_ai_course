from flask import Flask, render_template,request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openai
from datetime import datetime

app = Flask(__name__)


user_history = pd.DataFrame(columns=['timestamp','income_or_spending', 'type', 'amount'])


@app.route('/',methods=["GET","POST"])
def home():
    """
    允许用户输入信息，保存到user_history这个dataframe里面
    允许多次输入信息
    允许跳转另外两个页面
    """
    global user_history
    if request.method == "POST":
    
        income_or_spending = int(request.form['income_or_spending'])
        transaction_type = request.form['type']
        amount = float(request.form['amount'])
        timestamp = datetime.now().strftime('%Y/%m/%d')

        
        new_entry = pd.DataFrame({
            'timestamp': [timestamp],
            'income_or_spending': [income_or_spending],
            'type': [transaction_type],
            'amount': [amount]
        })

        user_history = pd.concat([user_history,new_entry],ignore_index = True)
        #print(user_history)

    return render_template('home.html')

@app.route('/analysis')
def analysis():

    return render_template('analysis.html')


@app.route('/suggestion',methods=["GET","POST"])
def suggestion():
    generated_text = None
    a = ""
    if request.method == "POST":
        a = request.form.get('user_prompt', '')
        if not a:
            return render_template('suggestion.html', message="Please enter a requirment.")
        
        prompt = prepare_prompt(a,user_history)
        generated_text = chat_with_gpt(prompt)
    
    return render_template('suggestion.html', user_prompt=a, generated_text=generated_text)





if __name__ == '__main__':
    app.run(debug=True)
