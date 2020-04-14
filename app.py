import logging

import daiquiri
from flask import Flask, render_template, request, escape

from ham.util.mm2nec import mm2nec

logging.basicConfig(level=logging.DEBUG)
LOGGER = daiquiri.getLogger(__name__)
LOGGER.info(f"{__name__} Starting")
app = Flask(__name__)


@app.route('/')
def getmmdata():
    return render_template('MMAMA.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        engine = mm2nec.mm2nec()
        mmana_def = result['mmana']
        nec_wire = engine.convert(mmana_def)
        # LOGGER.debug(f"Data passed is {mmana_def}")
        LOGGER.debug(f"nec_wire is {nec_wire}")
        #nec_wire = nec_wire.replace('\n','<BR>')
        LOGGER.debug(f"nec_wire_html is {nec_wire}")
        return render_template("nec4.html", rec=nec_wire, name="tim")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
