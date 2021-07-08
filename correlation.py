# Add the functions in this file
import json
import math


def load_journal(name):

    with open(name) as f:
        data = json.load(f)
    return (data)

    
def compute_phi(name,event):
    
    data = load_journal(name)
    
    # X : event and Y : squirrel

    n11,n00,n10,n01 = 0,0,0,0
    n1p,n0p,np1,np0 = 0,0,0,0

    for i in data:

        if event in i['events']:
            n1p+=1

            if i['squirrel']:
                n11+=1
                np1+=1
            else:
                n10+=1
                np0+=1
        else:
            n0p+=1

            if i['squirrel']:
                n01+=1
                np1+=1
            else:
                n00+=1
                np0+=1

    if n1p == 0:
        n1p =1
    if n0p == 0:
        n0p =1
    if np1 == 0:
        np1 =1
    if np0 == 0:
        np0 =1



    phi = (n11 * n00 - n10 * n01) / math.sqrt(n1p * n0p * np1 * np0)

    return phi


def compute_correlations(name):
    data = load_journal(name)
    event_set = set()
    phi_dict = {}

    for i in data:
        event_set.update(set((i['events'])))
    
    for event in event_set:
        phi_dict[event] = compute_phi(name,event)
    
    return phi_dict


def diagnose(name):
    corr_data = compute_correlations(name)
    event_max, event_min = max(corr_data, key = corr_data.get), min(corr_data, key = corr_data.get)

    return event_max,event_min



