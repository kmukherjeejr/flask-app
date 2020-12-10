from flask import Flask, request, render_template, redirect, url_for

def configure_routes(app):

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/about-us')
    def aboutus():
        return render_template('about.html')

    @app.route('/contact-us')
    def contactus():
        return render_template('contact.html')

    @app.route('/contact-details', methods=['POST','GET'])
    def contactdetails():
        data = request.form
        return render_template("contactdetails.html", data = data)
    @app.route('/going-back', methods=['POST'])
    def goingback():
        return redirect(url_for('contactus'))