from flask import Flask, request, render_template
import numpy as np
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('single_photon_page.html')

@app.route('/', methods=['POST'])
def photo_post():
    lamda = float(request.form['wavelength'])
    work_func = float(request.form['material'])
    h = 1.24E-6
    wave_length = lamda*1E-9
    photon_energy =  (h/wave_length) - work_func
    return render_template('single_photon_page.html', photo_energy = photon_energy)

@app.route('/', methods=['POST'])
def compton_post():
    incident = float(request.form['compton_wl'])
    angle = float(request.form['compton_angle'])
    compton_wavelength = 2.426E-12
    scattered_wavelength= compton_wavelength*(1-np.sin(angle))+incident
    h = 1.24E-6
    scattered_photon = h/scattered_wavelength
    return render_template('compton.html', compton_energy = compton_wavelength)


app.run()
