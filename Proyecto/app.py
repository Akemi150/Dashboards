from flask import Flask, render_template
#from flask_mysqldb import MySQL
from flaskext.mysql import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''
mysql = MySQL()


@app.route('/')
def consulta():
    return render_template('Consulta.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)