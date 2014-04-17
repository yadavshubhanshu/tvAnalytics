import os,subprocess
import helperFunctions
from app import app
from flask import Flask,render_template, flash, redirect, request, url_for
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit() and request.method=='POST':
    	#print request.method
    	flash('Series requested is : '+form.seriesName.data)
    	message = "30 rock"
        message =  helperFunctions.processSeriesString(message)

    	message[1] = message[1]+".json"
        showExists =  os.path.isfile(os.getcwd()+"/app/static/"+message[1])
    	if showExists:
            return render_template("generateChart.html",showName = message[1])
        else:
            subprocess.check_call(['scrapy', 'crawl', 'imdb', '-a', 'category=%s' % (message[0]), '-o', './app/static/%s' % (message[1]), '-t', 'json'])
            return render_template("generateChart.html",showName = message[1])	

    return render_template('inputs.html', title = 'Do Your Searches',form = form)