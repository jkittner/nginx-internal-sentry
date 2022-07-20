import sentry_sdk
from flask import Flask
from flask import Response
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn=None,
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0,
)

app = Flask(__name__)


@app.route('/')
def index() -> Response:
    return '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <link
      rel="stylesheet"
      type="text/css"
      href="https://cdn.datatables.net/v/dt/jq-3.6.0/dt-1.11.3/b-2.1.1/b-html5-2.1.1/sl-1.3.4/datatables.min.css"
    />
    <script
      type="text/javascript"
      src="https://cdn.datatables.net/v/dt/jq-3.6.0/dt-1.11.3/b-2.1.1/b-html5-2.1.1/sl-1.3.4/datatables.min.js"
    ></script>
    <title>Test</title>
  </head>
  <body>
    <table id="table_id">
      <thead>
        <tr>
          <th>firstname</th>
          <th>lastname</th>
        </tr>
      </thead>
    </table>
    <script>
      $(document).ready(function () {
        let table = $("#table_id").DataTable({
          ajax: { type: "POST", url: "/ajax_route", timeout: 1000, },
          serverSide: true,
          columns: [
            { data: "firstname", render: DataTable.render.text() },
            { data: "lastname", render: DataTable.render.text() },
          ],
        });
      });
    </script>
  </body>
</html>
'''


@app.route('/is_authenticated')
def auth() -> Response:
    return 'OK'


@app.route('/ajax_route', methods=['GET', 'POST'])
def ajax() -> Response:
    return {
        'draw': 1,
        'data': [
            {'firstname': 'test', 'lastname': 'testing'},
            {'firstname': 'test2', 'lastname': 'testing2'},
        ],
        'recordsTotal': 2,
        'recordsFiltered': 2,
    }


if __name__ == '__main__':
    app.run()
