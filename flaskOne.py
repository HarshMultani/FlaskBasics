from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

## These are called as flask views
@app.route('/hello/')
def hello_world():
    return "Hello world"


@app.route('/number/<id>')
def id(id):
    return id


@app.route('/number/<int:num>')
def num(num):
    return str(num)

@app.route('/number/<float:num>')
def num2(num):
    return str(num)



@app.route('/admin')
def hello_admin():
    return "Hello Admin"

@app.route('/guest/<guest>')
def hello_guest(guest):
    return "Hello %s" % guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest = name))


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == "POST":
        user = request.form['nm']
        return redirect(url_for('success', name = user))
    elif request.args.get('nm') :
        user = request.args.get('nm')
        return redirect(url_for('success', name = user))
    else:
        return render_template('login.html', message="Hey there", marks=50)



@ app.route('/marks')
def marks():
    return render_template('login.html', marks = 50, message = "Heyyyyyy")


@app.route('/testrequest')
def testrequest():
    var = request.args.get("var")
    return var



if __name__ == '__main__':
    app.run(debug = True)
