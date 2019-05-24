from flask import Flask, redirect, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/moto')
def all():
    return render_template('all.html')

@app.route('/moto/<moto_color>')
def color(moto_color):
    
    print(color)
    if moto_color == 'blue':
        return render_template('color.html', color = moto_color)
    if moto_color == 'red':
        return render_template('color.html', color = moto_color)
    if moto_color == 'purple':
        return render_template('color.html', color = moto_color)
    if moto_color == 'orange':
        return render_template('color.html', color = moto_color)
    else:
        return render_template('not_moto.html')

app.run(debug=True)