# analyze_particles_example.py

# Let's assume you have PSM, NAIS and DMPS data

from NpfEventAnalyzer import *
import numpy as np

############################
# PREPARING THE PSM DATA
# psm[1:,0]   time vector (days since beginning of year)
# psm[0,:]    limiting diameters for size bins (nm)
# psm[1:,2:]  unnormalized particle number concentrations in each bin (cm-3)

psm = np.loadtxt('/path/to/psm-data.dat')
psm_time = psm[1:,0]
psm_diam = np.sqrt(psm[0,1:]*psm[0,:-1])
psm_data = psm[1:,1:]/np.abs(np.diff(np.log10(psm[0,:])))


############################
# PREPARING THE NAIS DATA
# nais[1:,0]   time vector (days since beginning fo year)
# nais[0,2:]   geometric mean diameters of size bins (m)
# nais[1:,2:]  normalized particle number concentrations in each bin (cm-3)

nais = np.loadtxt('/path/to/nais-data.sum')
nais_time = nais[1:,0]
nais_diam = nais[0,2:]*1e9
nais_data = nais[1:,2:]


############################
# PREPARING THE DMPS DATA
# dmps[1:,0]   time vector (days since beginning of year)
# dmps[0,2:]   geometric mean diameters of size bins (nm)
# dmps[1:,2:]  normalized particle number concentrations in each bin (cm-3)

dmps = np.loadtxt('/path/to/dmps-data.sum')
dmps_time = dmps[1:,0]
dmps_diam = dmps[0,2:]
dmps_data = dmps[1:,2:]


############################
# RUN THE NPF EVENT ANALYZER

x = NpfEventAnalyzer()
particle_data = x.combine_sizedist([psm_time,nais_time,dmps_time],       # time vectors (doy)
                                    [psm_diam,nais_diam,dmps_diam],       # diameter vectors (nm)
                                    [psm_data,nais_data,dmps_data],       # data matrices (cm-3)
                                    [[1.0,2.5],[2.5,20.0],[20.0,1000.0]], # size limits (nm) 
                                    time_resolution=1/1440.)              # time resolution = 1 min
x.analyze_par(particle_data, temp = 273.15, pres = 101325.0)