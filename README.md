# logical_rush
Batch-computing solution for cashflow calculations.

# Developed by Rodolfo Blasser 
https://www.linkedin.com/in/rodblasser/

## Usage
Prototype batch-computing library for calculating loan amortization tables.

## Example
```python
import random
import pandas as pd
import time
import logical_rush


products = ['Auto', 'Personal', 'Commercial', 'Mortgage', 'MicroCredit']
terms = [5, 10, 15, 20, 25, 30]
#terms = [5, 10, 15]
rates = [0.04, 0.05, 0.06, 0.07, 0.08]
amounts = [10000, 20000, 30000, 50000, 60000] 
freqs = [1,2,3,6]

# =============================================================================
# Testing performance
# =============================================================================
res = []
for each_i in range(*{'start':100,'stop':500,'step':5}.values()):

    dx = pd.DataFrame(index=range(each_i), columns=['id','amt','rate','pers','int_freq','cap_freq'],)
    print("\ndx created with {} rows".format(dx.shape[0]))
    
    dx['id'] = (dx.index + 1000)
    dx['amt'] = dx['amt'].apply(lambda x:random.choice(amounts))
    dx['rate'] = dx['rate'].apply(lambda x:random.choice(rates)) / 12
    dx['pers'] = dx['pers'].apply(lambda x:random.choice(terms)) * 12 #* 30 # daily flows
    dx['int_freq'] = dx['int_freq'].apply(lambda x:random.choice(freqs))
    dx['cap_freq'] = dx['cap_freq'].apply(lambda x:random.choice(freqs))
    dx['id'] = dx['id'].astype(str)
    dx['amt'] = dx['amt'].astype(float)
    dx['rate'] = dx['rate'].astype(float)
    
    dx_dict = dx.to_dict(orient="records")
    
    
    dxs = dx.copy()
    for c in dxs.columns:
        dxs[c] = dxs[c].astype(str)
        
    dxs_dict = dxs.to_dict(orient="records")
    
    # Sequential
    tic = time.time()
    i = logical_rush.cashflower_fn(dx_dict)
    tac = time.time()
    tictac_seq = tac - tic
    print("SEQ: {}".format(tictac_seq))
    
    flows_len = len(i)
    del i
    
    # Parallel
    tic = time.time()
    ipar = logical_rush.cashflower_par(dxs_dict)
    tac = time.time()
    tictac_par = tac - tic
    print("PAR: {}".format(tictac_par))
    
    del ipar
    
    # GIL Release
    tic = time.time()
    igil = logical_rush.cashflower_gil(dxs_dict)
    tac = time.time()
    tictac_gil = tac - tic
    print("GIL: {}".format(tictac_gil))
    
    del igil
    
    res.append([each_i, flows_len, tictac_seq,  tictac_par, tictac_gil])
    print("\t{} SEQ loans @ {} seconds | output: {} flows".format(each_i,round(tictac_seq,4),flows_len))
    print("\t{} PAR loans @ {} seconds | output: {} flows".format(each_i,round(tictac_par,4),flows_len))
    print("\t{} GIL loans @ {} seconds | output: {} flows".format(each_i,round(tictac_gil,4),flows_len))

# Export comparison
pd.DataFrame(res).to_csv("benchmarking_results_seq_par_gil_flows.csv")
```
