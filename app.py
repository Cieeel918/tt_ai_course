from flask import Flask, render_template,request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openai

app = Flask(__name__)


user_history = pd.DataFrame()


@app.route('/',methods=["GET","POST"])
def home():
    """
    允许用户输入信息，保存到user_history这个dataframe里面
    允许多次输入信息
    允许跳转另外两个页面
    """

    return render_template('home.html')

@app.route('/analysis')
def analysis():




    return render_template('analysis.html')


@app.route('/suggestion',methods=["GET","POST"])
def suggestion():

    if request.method == "POST":
        user_prompt = request.form.get('user_prompt', '')
        if not user_prompt:
            return render_template('suggestion.html', message="Please enter a requirment.")
        

    return render_template('index.html')






    user_prompt = request.get_data('prompt')
    prompt = prepare_prompt(user_history,user_prompt)

    return render_template('suggestion.html')


if __name__ == '__main__':
    app.run(debug=True)
