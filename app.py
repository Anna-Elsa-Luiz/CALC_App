from flask import Flask , render_template , url_for , request , redirect 

App = Flask(__name__)

@App.route('/')
def Home():
    return render_template('index.html')


@App.route('/calculate',methods=['POST'])
def calculate():
    expression = request.form['expression']
    result = eval(expression)
    return render_template('index.html', result=result, expression=expression)

if __name__ == '__main__':
    App.run(debug=True)