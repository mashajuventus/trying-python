
def unique(e):
    return sorted(set(e))
    

def transposeDict(d):    
    return {d[a]: a for a in d.keys()}

    
def mex(e):
    for p in range(1, len(e) + 2):
        if p not in e:
            return p
            
            
def frequencyDict(s):
    return {a: s.count(a) for a in s}
    
