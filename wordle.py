from flask import *

app=Flask(__name__)


@app.route("/")
def home():
	return render_template("index.html")


'''
@app.route("/sub",methods=['POST','GET'])
def  submi():
	if request.method=="POST":
		name=request.form["submit_button"]
		return render_template("index.html",n=name)'''


@app.route("/keys",methods=['POST','GET'])

def alpha():


	if request.method=="POST" and request.form["A"]:

		def letter_a():

			a=request.form["A"]
		
			return render_template("index.html",a=a)
		letter=letter_a()
		return letter






if __name__=="__main__":
	app.run(debug=True)


	'''def alpha():

	if request.method=="POST":

		if request.form=="A":
			def letter_a():
				a=request.form["A"]
				return render_template("index.html",a=a)


			return letter_a'''
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
	
