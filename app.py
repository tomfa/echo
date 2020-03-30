"""Flask App Project."""
from time import strftime

from flask import Flask, request
app = Flask(__name__)


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    if request.method == 'POST':
        data = request.get_data(cache=True, as_text=True, parse_form_data=True)
    else:
        data = None

    request_info = {
        'timestamp': strftime('%Y-%b-%d %H:%M:%S'),
        'path': path,
        'query': request.query_string.decode(),
        'method': request.method,
        'headers': dict(request.headers),
        'data': data
    }
    app.logger.error(str(request_info))
    return request_info


if __name__ == '__main__':
    app.run()
