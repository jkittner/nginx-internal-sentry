from flask import Flask
from flask import Response
app = Flask(__name__)


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
