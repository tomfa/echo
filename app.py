"""Flask App Project."""
from collections import OrderedDict
import logging
from time import strftime

import colors
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

    ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    log_params = [
        ('path', request.path, 'blue'),
        ('method', request.method, 'blue'),
        ('query', request.query_string.decode(), 'blue'),
        ('ip', ip, 'red'),
        ('data', str(data), 'white'),
        ('headers', dict(request.headers), 'yellow'),
    ]

    parts = []
    for name, value, color in log_params:
        part = colors.color("{}: {}\n\t".format(name, value), fg=color)
        parts.append(part)

    app.logger.info(" ".join(parts))

    return {key: value for key, value, color in log_params}


if __name__ == '__main__':
    app.run()
