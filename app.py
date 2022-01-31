from flask import Flask, session,redirect, url_for, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jfhwha'

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/set_background/<mode>')
def set_background(mode):
    session['mode'] = mode
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)