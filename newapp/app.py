from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about-us')
def about_us():
    return render_template('about.html')


@app.route('/contact-us')
def contactus():
    return render_template('contact.html')


@app.route('/contact-details', methods=['POST', 'GET'])
def contact_details():
    data = request.form
    return render_template("contactdetails.html", data=data)


@app.route('/going-back', methods=['POST'])
def going_back():
    return redirect(url_for('contactus'))


if __name__ == '__main__':
    app.run(debug=True)
