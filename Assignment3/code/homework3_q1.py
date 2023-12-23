import math
import numpy as np

def my_Bayes_candy(pi_list, p_list, c_list):
    posterior_probabilities = [[0] * 5 for i in range(10)]  
    for i in range(10):
        count=0
        for k in range(5): 
            current_pi=pi_list[k]  
            for j in range(i+1):
                if c_list[j]==0:
                    current_pi*=p_list[k]
                if c_list[j]==1:
                    current_pi*=(1-p_list[k])
            count+=current_pi
        for j in range(5):
            final_answer=pi_list[j]  
            for l in range(i+1):
                if c_list[l]==0:
                    final_answer*=p_list[j]
                if c_list[l]==1:
                    final_answer*=(1-p_list[j])
            posterior_probabilities[i][j]=final_answer/count
    for i in range(10):
        print(posterior_probabilities[i])
    return posterior_probabilities
