import import_ipynb

from flask import Flask, render_template, url_for, flash, redirect
from forms import AcceptURL
from predicting_output import predict

app = Flask(__name__)

app.config['SECRET_KEY'] = '612202c1ba464e2083b8287e8a1f5554'

@app.route("/", methods = ['GET', 'POST'])
@app.route("/home", methods = ['GET', 'POST'])
def home():
	form = AcceptURL()

	if form.validate_on_submit():
		u = form.url.data
		p = predict(u)
		p = str(p)
		p = p[2:-2]
		flash(f'Predicted Flair: {p}', 'success')
		return redirect(url_for('home'))
	return render_template("home.html", form = form)

@app.route("/statistics")
def stats():
	return render_template("stats.html")

if __name__ == "__main__":
	app.run(debug = True)