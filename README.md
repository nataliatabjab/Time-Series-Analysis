# Time Series Analysis (PHY408)

This repository contains my labs and assignments for **PHY408 – Time Series Analysis**.  
The course introduces methods for processing and modeling time-ordered data, with applications to seismology, acoustics, and atmospheric measurements.  
We use Python and Jupyter notebooks to perform convolution, Fourier analysis, spectral estimation, and autoregressive modeling.

## Repository structure

```
.
├── Lab 0/   # Introduction & setup
│   └── Tabja_Natalia_Lab0.pdf
├── Lab 1/   # Convolution & filtering
│   ├── lab1.py, discrete.py, part3.py
│   └── seismogram data
├── Lab 2/   # AR models & spectral estimation
│   ├── argon.py, testing.py
│   └── Notebook + report
├── Lab 3/   # Fourier analysis
│   ├── q1.py, q2.py …
├── Lab 4/   # Digital filter design & coherence
│   └── lab4.py, spectra plots
```

## Highlights
- Implemented discrete convolution and filtering from scratch.  
- Used FFTs for spectral analysis.  
- Designed digital filters and applied them to seismogram data.  
- Built autoregressive models and estimated power spectral densities.  
- Explored cross-correlation and spectral coherence.  

## Usage
Install dependencies:
```bash
pip install numpy matplotlib scipy
```

Run any script directly, e.g.:
```bash
python "Lab 1/lab1.py"
```
Or open the Jupyter notebooks for interactive analysis.
