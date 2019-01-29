from flask import Flask, request, render_template
import numpy as np
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('rayleigh.html')

@app.route('/', methods=['POST'])
def compton_post():
    incident = float(request.form['rayleigh_wl'])
    wavelength = incident*1E-9
    h = 1.24E-6
    scattered_photon = h/wavelength
    return render_template('rayleigh.html', rayleigh_energy = scattered_photon)

app.run()