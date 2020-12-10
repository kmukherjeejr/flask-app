from flask import Flask, request, render_template, redirect, url_for
from handlers.routes import configure_routes

app = Flask(__name__)

configure_routes(app)

if __name__ == '__main__':
    app.run(debug=True)