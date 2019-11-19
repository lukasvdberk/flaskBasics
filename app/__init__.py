from flask import Flask

# Initialize the app
app = Flask(__name__, instance_relative_config=True)
# Load the config file
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Load the views
from app import views

app.run(debug=True, host='0.0.0.0')