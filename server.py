from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'hola'


@app.route('/')
def home():
    if 'contador' in session:
        session['contador']+=1
    else:
        session['contador']=1
    return render_template ('index.html')

@app.route('/masdos')
def dos():
    session['contador']+=2
    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')





if __name__== "__main__":
    app.run(debug=True)