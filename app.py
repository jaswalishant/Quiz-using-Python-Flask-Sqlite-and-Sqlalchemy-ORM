from flask import Flask, render_template, request,session, redirect, url_for
from data import engine, User, userScore, GK_questions, sports_questions, animals_questions, science_questions, computer_questions
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

Session= sessionmaker(bind=engine)
session=Session()
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method=="POST":
        q=request.form.get('question')
        c=request.form.get('correct')
        i1=request.form.get('incorrect1')
        i2=request.form.get('incorrect2')
        i3=request.form.get('incorrect3')

        Q=animals_questions(question=q, correct=c, incorrect1=i1, incorrect2=i2, incorrect3=i3)
        session.add(Q)
        session.commit()
    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)
