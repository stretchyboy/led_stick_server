from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

#app_blueprint = Blueprint('app_blueprint', __name__, static_url_path="app", static_folder="/home/meggleton/Projects/demo-progressive-web-app" )
app_blueprint = Blueprint('app_blueprint', __name__ )


@app_blueprint.route('/')
def index():
    return render_template("app/index.html")


    