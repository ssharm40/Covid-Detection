from flask import Flask
from flask import render_template
from flask import request 
from covid import *
covid=Covid()

app = Flask(__name__)

# open a file, where you stored the pickled data
import pickle
obj = open('model.pkl', 'rb')

# dump information to that file
data = pickle.load(obj)

obj.close() 

@app.route("/")
def indexD():
    return render_template('indexD.html')

@app.route("/caseforIndia")
def caseforIndia():
    l=[]
    a=covid.get_status_by_country_id(80)
    return render_template('case.html',a=a)

@app.route("/caseforUsa")
def caseforUsa():
    l=[]
    a=covid.get_status_by_country_id(182)
    return render_template('case.html',a=a)

@app.route("/caseforFrance")
def caseforFrance():
    l=[]
    a=covid.get_status_by_country_id(63)
    return render_template('case.html',a=a)

@app.route("/caseforRussia")
def caseforRussia():
    l=[]
    a=covid.get_status_by_country_id(145)
    return render_template('case.html',a=a)

@app.route("/caseforJapan")
def caseforJapan():
    l=[]
    a=covid.get_status_by_country_id(88)
    return render_template('case.html',a=a)


@app.route('/index', methods=['GET','POST'])  
def index():
    if request.method == "POST":
        myDict=request.form
        age=int(myDict['age'])
        fever=int(myDict['fever'])
        tiredness=int(myDict['tiredness'])
        smell=int(myDict['smell'])
        headache=int(myDict['headache'])
        breath=int(myDict['breath'])
        inputfeature=[age,fever, tiredness,smell,headache,breath]
        infprob=data.predict_proba([inputfeature])[0][1]
        infprob=str(infprob)[2:4]
        print(infprob)
        return render_template('show.html', inf=infprob)

    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)


    