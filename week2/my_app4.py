from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def hello():
	return render_template('index4.html')

@app.route('/page2')
def page2():
	return render_template('page_2.html')

@app.route('/graph')
def page3():
	return render_template('edges.html', title='NER - realations between targets in medical article')


@app.route('/greet')
def greeting():
	user = {'username': 'Сережа'}
	return render_template('hi.html', title='Приветствие', user=user)


if __name__ == "__main__":
	app.run(debug=True)
