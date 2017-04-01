from flask import Flask,render_template,request,jsonify, url_for,redirect,flash
import pymysql
import time
import memcache
import hashlib
import json
from datetime import datetime
#from application.models import Data
#import pymysql

app= Flask(__name__)
#app.config['SECRET_KEY']= '\xce\xd0=g\x8c\xb0U\xf9\xe6V\x044\xb1aR\xb7&Z^\xa55\xeb\x02\x02'
#APP_ROOT = os.path.dirname(os.path.abspath(__file__))
	
@app.route('/')
@app.route('/index')
def index():
    return  render_template('index.html')
	  
@app.route('/add', methods=['GET','POST'])
def add():
	return render_template('add.html')
	
@app.route('/upload',methods=['POST'])
def upload():
	#target= os.path.join(APP_ROOT, 'images/')
	#print(target)
	
	#if not os.path.isdir(target):
	    #os.mkdir(target)
	
	    #for file in request.files.getlist("file") :
		 #print(file)
		 #filename= file.filename
		 #destination="/".join([target,filename])
		 #print(destination)
		 #file.save(destination)
	return render_template("complete.html", image_name=filename)
		
		
# @app.route('/upload/<filename>')
# def send_image(filename):
	# return send_from_directory("images",filename)

	   # form1 = EnterDBInfo(request.form) 

       # #form2 = RetrieveDBInfo(request.form) 

    

    # if request.method == 'POST' and form1.validate():

        # data_entered = Data(notes=form1.dbNotes.data)

        # try:     

            # db.session.add(data_entered)

            # db.session.commit()        

            # db.session.close()

        # except:

            # db.session.rollback()

        # return render_template('complete.html', notes=form1.dbNotes.data)

        

    # if request.method == 'POST' and form2.validate():

        # try:   

            # num_return = int(form2.numRetrieve.data)

            # query_db = Data.query.order_by(Data.id.desc()).limit(num_return)

            # for q in query_db:

                # print(q.notes)

            # db.session.close()

        # except:

            # db.session.rollback()

        return render_template('complete.html')                

    

   # return render_template('index.html', form1=form1, form2=form2)
@app.errorhandler(404)
def page_not_found(e):
      return  render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
      return  render_template('500.html'), 500
	  
	  
if __name__== "__main__":
   app.run(debug=True)
