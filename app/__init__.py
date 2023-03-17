"""Sample hello world Flask app"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1> Hello, World!</h1>"


@app.route("/")
def products():
    product_list = ["Apples", "Oranges", "Banannas"]
    bullet_list = "".join(
        "<li>%s</li>" % product for product in product_list
    )
    
    return "<ul>%s</ul>" % bullet_list