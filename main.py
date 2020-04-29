from flask import Flask,render_template,request
app=Flask(__name__,template_folder='C:\\Users\\acer')
import pickle
file=open('model.pkl','rb')
clf=pickle.load(file)
file.close()
@app.route('/',methods=["GET","POST"])


def hello_world():
    if request.method=="POST":
        #print(request.form)
        myDict=request.form
        fever=int(myDict['FEVER'])
        age=int(myDict['AGE'])
        pain=int(myDict['PAIN'])
        runnynose=int(myDict['RUNNYNOSE'])
        diffBreath=int(myDict['diff'])

        inputs=[fever,pain,age,runnynose,diffBreath]
        info=clf.predict_proba([inputs])[0][1]
        print(info)
        return render_template('show.html',inf=round(info*100))
    return render_template('in.html')
    #return 'HELLO,world'+str(info)+render_template('in.html')



if __name__=="__main__":
      app.run(debug=True)