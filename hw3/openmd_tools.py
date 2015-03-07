
import numpy as np
import itertools
import subprocess
import matplotlib.pyplot as plt

def get_all_pairs(atomtypes):
    return list(itertools.combinations_with_replacement(atomtypes, 2))

def calculate_pair_corr(filename, atom1, atom2):
    cmd = 'StaticProps -i {2}.dump -g --sele1="select {0}" --sele2="select {1}" > {0}-{1}.gofr'.format(atom1, atom2, filename)
    subprocess.call(cmd, shell=True)
    return read_correlation_fn('{0}.gofr'.format(filename))
    
def read_correlation_fn(filepath):
   return np.loadtxt(filepath, skiprows=3, unpack=True)

def read_msd(filepath):
   '''Reads the mean square displacement from the rcorr file'''
   return np.loadtxt(filepath, skiprows=4, unpack=True)

def read_vel_corr(filepath):
   return np.loadtxt(filepath, skiprows=4, unpack=True)

def read_power_spectrum(filepath):
    return np.loadtxt(filepath, unpack=True)
   
def msd_slope_and_interval(t, msd, tstart=0):
   t_stack = np.column_stack([t[tstart:]**1, t[tstart:]**0])
   b, res, rank, s = np.linalg.lstsq(t_stack, msd)
   slope, interval = b
   return slope, interval

def get_D_einstien(t, msd, tstart=0, d=3):
   slope, interval = msd_slope_and_interval(t, msd, tstart) 
   return slope / 2. / d

def get_D_greenkubo(t, vcorr):
    return np.abs(np.sum(t * vcorr / 3) /len(vcorr))
