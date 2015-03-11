
import numpy as np
import itertools
import subprocess
import matplotlib.pyplot as plt
import os

def get_all_pairs(atomtypes):
    '''
    Returns a list of all possible pairs from a list of atomic speicies.
    '''
    return list(itertools.combinations_with_replacement(atomtypes, 2))

def calculate_pair_corr(filepath, atom1, atom2):
    '''
    Convenience function to provide for fast calculations of pair correlation functions
    Strangely, I could not get StaticProps to dump to a specified folder/file, 
    so we have to take care to change directories and return data
    '''
    try:
        # If a path is spefified
        wd, filename = filepath.rsplit('.')[0].split('/')
    except:
        # If only filename is specified
        filename = filepath.rsplit('.')
        wd = '.'
        
    cmd = 'StaticProps -i {2}.dump -g --sele1="select {0}" --sele2="select {1}" '
    cmd = cmd.format(atom1, atom2, filename)
    cwd = os.getcwd()
    os.chdir(wd)
    subprocess.call(cmd, shell=True)
    os.chdir(cwd)
    return read_pair_corr('{0}/{1}.gofr'.format(wd, filename))

def read_pair_corr(filepath):
    '''Reads the pair correlation function from a gofr file'''
    return np.loadtxt(filepath, skiprows=3, unpack=True)

def read_msd(filepath):
   '''Reads the mean square displacement from the rcorr file'''
   return np.loadtxt(filepath, skiprows=4, unpack=True)

def read_vel_corr(filepath):
    '''Reads the velocity correlation function from the vcorr file'''
    return np.loadtxt(filepath, skiprows=4, unpack=True)

def read_power_spectrum(filepath):
    '''
    Reads the power spectrum from a pspect file
    '''    
    return np.loadtxt(filepath, unpack=True)
   
def msd_slope_and_interval(t, msd, tstart=0):
    '''
    Linear regression fitting for MSD data
    '''
    t_stack = np.column_stack([t[tstart:]**1, t[tstart:]**0])
    b, res, rank, s = np.linalg.lstsq(t_stack, msd)
    slope, interval = b
    return slope, interval

def get_D_einstien(t, msd, tstart=0, d=3):
    '''Diffusion coefficient from Einstien relation'''
    slope, interval = msd_slope_and_interval(t, msd, tstart) 
    return slope / 2. / d

def get_D_greenkubo(t, vcorr):
    '''Diffusion coefficeint from Green-Kubo
    Probably better to make this continuous
    '''
    return np.abs(np.trapz(vcorr, t) * 1/ 3.)
