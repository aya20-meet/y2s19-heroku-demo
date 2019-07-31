from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home_page():
	fave=["Burger","Pasta","pizza"]
	not_food=["yams","menta","yasa"]
	return render_template("index.html", fave=fave, not_food=not_food, yuval=False)
@app.route('/singup')
def singup_page():
    return render_template("singup.html","")
@app.route('/thankyou')
def thankyou():
    return render_template("thankyou.html")
if __name__ == '__main__':
    app.run(debug = True, port=2000)
