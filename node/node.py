from flask import Flask
import utils
import os

app = Flask(__name__)

@app.route('/ip/<interface>')
def ip(interface):
    return utils.get_ip_address(str(interface))

@app.route('/hostname')
def hostname():
    return utils.get_hostname()

@app.route('/load_averages')
def load():
    ld_avg = os.getloadavg()
    f = "{0:.2f}"
    return f.format(ld_avg[0]) + ", " + f.format(ld_avg[1]) + ", " + f.format(ld_avg[2])

if __name__ == "__main__":
    app.run()
