import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    query = "Ljubljana"
    unit = "metric"
    api_key = "API KEY INSERT!!"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}".format(query, unit, api_key)
    data = requests.get(url=url)

    return render_template("index.html", data=data.json())

if __name__=='__main__':
    app.run()