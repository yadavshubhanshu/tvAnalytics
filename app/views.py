import os,subprocess
import helperFunctions
from app import app
from flask import Flask,render_template, flash, redirect, request, url_for
from forms import SearchForm


@app.route('/',methods = ['GET', 'POST'])
@app.route('/index',methods = ['GET', 'POST'])
@app.route('/searchSeries', methods = ['GET', 'POST'])
def searchSeries():
    form = SearchForm()

    #Redirect to the same page after recieving request
    if form.validate_on_submit() and request.method=='POST':
    	#print request.method

    	flash('Series requested is : '+form.seriesName.data)

    	message = form.seriesName.data
        message =  helperFunctions.processSeriesString(message)

    	message[1] = message[1]+".json"

        showExists =  os.path.isfile(os.getcwd()+"/app/static/"+message[1])
        
        #if show file exists, then use that file otherwise use scrapy to generate the json and then use that
    	if showExists:
            return render_template("generateChart.html",showName = message[1])
        else:
            subprocess.check_call(['scrapy', 'crawl', 'imdb', '-a', 'category=%s' % (message[0]), '-o', './app/static/%s' % (message[1]), '-t', 'json'])
            return render_template("generateChart.html",showName = message[1])	

    return render_template('inputs.html', title = 'Do Your Searches',form = form)