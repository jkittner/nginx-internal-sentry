import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn='https://<id>@o<id>.ingest.sentry.io/<id>',
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0,
)

app = Flask(__name__)


@app.route('/')
def index() -> str:
    return 'hello'


@app.route('/is_authenticated')
def auth() -> str:
    return 'OK'


if __name__ == '__main__':
    app.run()
