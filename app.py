"""Flask App Project."""
import logging
from time import strftime

from flask import Flask, request

app = Flask(__name__)
app.logger.setLevel(logging.INFO)


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    if request.method == 'POST':
        data = request.get_data(cache=True, as_text=True, parse_form_data=True)
    else:
        data = None

    request_info = {
        "content-type": request.content_type,
        "data": data,
        "headers": dict(request.headers),
        "method": request.method,
        "path": path,
        "query": request.query_string.decode(),
        "timestamp": strftime("%Y-%b-%d %H:%M:%S"),
    }
    app.logger.info(str(request_info))
    return request_info


if __name__ == '__main__':
    app.run()
