from flask import Flask, jsonify, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('frontend.html')

@app.route('/data')
def data():
    try:
        with open("data.txt", "r") as file:
            value = file.read()
    except FileNotFoundError:
        value = "Data nejsou dostupná"
    return jsonify(value=value)

if __name__ == '__main__':
    app.run(debug=True)
