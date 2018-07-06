from flask import Flask, render_template,flash,redirect,request,jsonify
from flask_sslify import SSLify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
from recommend import reco
import pygal
import pygal.style as st
dd={}
class Config(object):
	SECRET_KEY=os.environ.get('SECRET_KEY') or "you-will-never-guess"
app = Flask(__name__)
sslify = SSLify(app)
app.config.from_object(Config)
class enterfrom(FlaskForm):
	access_id=StringField("Enter id",validators=[DataRequired()])
	submit=SubmitField('Recommend!')
@app.route("/",methods=['GET','POST'])
def hello():
	f=enterfrom()
	if f.validate_on_submit():
		id=f.access_id.data
		flash("{}".format("Your recommended Subreddits are:"))
		id=f.access_id.data
		p=reco(id)
		for i in p:
			flash("{}".format(i))
		return redirect("/")
	return render_template("kain.html",form=f)
@app.route("/graph")
def gr():
	global dd
	bar_chart = pygal.Bar(margin=30,width=1400, height=700,explicit_size=True,inner_radius=.4,style=st.DarkStyle)
	bar_chart.title="Frequency of liked subreddits"
	for key,value in dd.items():
		bar_chart.add(key,value)
	return(bar_chart.render())

@app.route("/result")
def result():
	return render_template('sub.html')
@app.route('/background_process')
def background_process():
	global dd
	try:
		lang = request.args.get('proglang', 0, type=str)
		print(lang)
		k=['bad login gateway']
		if lang != 'none':
			a,l,lt,rt,tyy=reco(lang)
			dd=tyy
			return jsonify(result=a,lol=l,lt=lt,rt=rt)
		else:
			return jsonify(result=k,status=0)
	except Exception as e:
		return str(e)
@app.route("/privacy")
def priv():
    return render_template("priv.html")
@app.route("/likes")
def who():
	return render_template('likes_list.html')
@app.route("/main",methods=['GET','POST'])
def ma():
    f=enterfrom()
    if f.validate_on_submit():
        id=f.access_id.data
        flash("{}".format("Your recommended Subreddits are:"))
        id=f.access_id.data
        p=reco(id)
        for i in p:
            flash("{}".format(i))
        return redirect("/main")
    return render_template("main.html",form=f)


if __name__ == "__main__":
    app.run(debug=True)