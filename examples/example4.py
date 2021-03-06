from flask import Flask, request
from flask_json import FlaskJSON, as_json_p

app = Flask(__name__)
json = FlaskJSON(app)

app.config['JSON_ADD_STATUS'] = False
app.config['JSON_JSONP_OPTIONAL'] = False


@app.route('/show_message')
def show_message():
    return """
    <!DOCTYPE html>
    <html>
        <body>
            <script type="application/javascript"
                    src="%smessage/hello?callback=alert">
            </script>
        </body>
    </html>
    """ % request.host_url


@app.route('/message/<text>')
@as_json_p
def message(text):
    return text


@app.route('/show_quoted')
def show_quoted():
    return """
    <!DOCTYPE html>
    <html>
        <body>
            <script type="application/javascript"
                    src="%squote_message?callback=alert">
            </script>
        </body>
    </html>
    """ % request.host_url


@app.route('/quote_message')
@as_json_p
def quote_message():
    return 'Hello, "Sam".'


@app.route('/dict')
@as_json_p
def dict():
    return {'param': 42}


if __name__ == '__main__':
    app.run()
