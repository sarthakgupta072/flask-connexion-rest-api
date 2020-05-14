from flask import render_template
import connexion

# Creat the application instance using connexion
""" specification_dir informs Connexion the directory to look in for its
config file """
app = connexion.App(__name__, specification_dir='./')

"""This tells the app instance to
 read the file swagger.yml from the specification
 directory and configure the system to
 provide the Connexion functionality. """
app.add_api('swagger.yaml')


@app.route("/")
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
