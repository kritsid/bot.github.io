from flask import Flask,redirect,url_for,render_template,request,g,session
app=Flask(__name__)


@app.route('/', methods = ['GET','POST'])
def index():
    return render_templete('index.html')



if __name__ == '__main__':
    app.run(debug=True)