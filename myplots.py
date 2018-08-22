#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 23:04:59 2018

@author: michal
"""

# 2.Visualization libraries
import matplotlib.pyplot as plt
import numpy as np


def plot_samples(data,output,names,title="Sample_images",fig_size =(30,30),title_font = 50, data_num = 6,n_rows = 2,n_cols = 3, save_fig = False):
    
    """
    Description : Plot sample images from dataset
    
    Input : 
        * data -- picture dataset
        * title -- title of figure
        * title_font -- title of figure font
        * data_num -- number of pictures to plot
        * n_rows -- number of rows
        * n_cols -- number of columns
        
    """
    
    plt.figure(1,figsize = fig_size)
    for i in range(1,int((data_num+1))):
        plt.subplot(n_rows,n_cols,i)
        a = (np.asscalar(output[i]))
        plt.title(names[a],fontsize = 35)
        plt.imshow(data[i])
    
    plt.suptitle(title,fontsize=title_font)

    if save_fig == True:
        plt.savefig(title)
    
    del i
    return 0

    
    
    
def plot_training(history,val = False):
    
    if history.history["acc"]:
        acc = history.history["acc"]
    if history.history["loss"]:
        loss = history.history["loss"]
    
    if val == True :
        if history.history["val_acc"]:
            val_acc = history.history["val_acc"]
    
        if history.history["val_loss"]:
            val_loss = history.history["val_loss"]
    
    epoch = range(len(acc))
    
  # plot part...
    