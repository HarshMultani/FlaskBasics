from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def helloWorld():
    return 1/0
    #return "Hello World"


@app.route("/processjson", methods=["POST"])
def processjson():

    if (request.data):
        data = request.get_json()
        name = data['name']
        return name
    else :
        return "There is no data"


@app.route("/static", methods=["GET"])
def static_data():
    return render_template('readdata.html', data="Harsh")

@app.route("/dynamic/<value>", methods=['GET','POST'])
def dynamic_data(value):
    return render_template('readdata.html', data=value)


@app.errorhandler(404)
def not_found_exception(error):
    return "Requested URL    not found ",404

@app.errorhandler(500)
def server_error(error):
    return render_template('500error.html')



if __name__ == "__main__":
    app.run(debug=True)
