from flask import Flask, render_template, request
from agent import agent

app = Flask(__name__)


@app.route('/', methods = ['GET','POST'])
def astro():
    info = None
    if request.method == 'POST':
        name = request.form['name']
        birth_date = request.form['dob']
        birth_time = request.form['tob']
        city = request.form['city']
        country = request.form['country']
        question = request.form['question']
        print(name,birth_date,birth_time,city,country)
        print("Hello world")
        info = agent(name,birth_date,birth_time,city,country,question)
        
    return render_template("index.html", info = info)





if __name__ == "__main__":
    app.run(debug = True)