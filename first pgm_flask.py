# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 14:31:05 2023

@author: user
"""



from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
app=Flask(__name__) 

pickle_in=open('classifier.pkl','rb')   
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "welcome to my first pgm "



    
    
if __name__=="__main__":
        app.run()