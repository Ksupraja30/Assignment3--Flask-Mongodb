from flask import Flask, request, redirect, url_for, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("your_mongodb_connection_string")
db = client.test_db
collection = db.users

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']

            collection.insert_one({
                "name": name,
                "email": email
            })

            return redirect(url_for('success'))

        except Exception as e:
            return render_template(
                'form.html',
                error=str(e)
            )

    return render_template('form.html')


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
