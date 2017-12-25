
# ##### This file contains commonly used functions

from __future__ import division 
import numpy as np
import scipy.stats as stats

# Let us calcluate the z-statistic
def z_statistic(x,mu0,sd_population):
    '''calculates the z statistic and p_value of an array x, given 
    population mean and standard deviation'''
    xbar = np.mean(x) - mu0
    std_err = sd_population / np.sqrt(x.shape[0])
    z_stat = xbar / std_err
    p_value = stats.norm.sf(abs(z_stat))
    return z_stat,p_value


def ecdf(data):
    '''Takes in an array and returns two arrays - sorted data set and a uniform scale'''
    sorted_data=np.sort(data)
    scale=np.arange(1,len(data)+1)/len(data)
    return sorted_data,scale


def bootstrap_replicate_1d(data, func):
    '''Takes an array and function as paremeters and returns the 
    bootstrap sample with the function applied'''
    return func(np.random.choice(data, size=len(data)))


def draw_bs_reps(data, func, size=1):
    '''Takes an array, function and size as parametes and returns the 
    array of bootstrap samples with the function applied'''
    return np.array([bootstrap_replicate_1d(data, func) for _ in range(size)])

def permutation_sample(data1, data2):
    '''Takes two data sets, performs permutation and returns it back'''
    sample = np.concatenate((data1, data2))
    permuted_data = np.random.permutation(sample)    
    return permuted_data[:len(data1)], permuted_data[len(data1):]
    
def draw_perm_reps(data_1, data_2, func, size=1):
    '''Generates permutation replicates'''
    perm_reps = np.empty(size)
    for i in range(size):
        perm_sample_1, perm_sample_2 = permutation_sample(data_1,data_2)
        perm_reps[i] = func(perm_sample_1, perm_sample_2)        
    return perm_reps
    
def diff_of_means(data_1,data_2):
    '''returns the difference in means of two arrays.'''
    return np.mean(data_1)-np.mean(data_2)
    
def z_prop(c1,c2,n1,n2):
     '''Calculate the a Test statistic for two proportions'''
     '''c1,c2: success count of first and second sample'''
     '''n1,n2: count of first and second sample'''
     numerator = c1/n1 - c2/n2
     p = (c1+c2)/(n1+n2)
     q = 1 - p
     denominator = np.sqrt(p*q*(1/n1 + 1/n2))
     return numerator/denominator
    