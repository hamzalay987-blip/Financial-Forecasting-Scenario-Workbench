import csv

def forecast(values,months=3,multiplier=1.0):
    step=sum(b-a for a,b in zip(values,values[1:]))/(len(values)-1)*multiplier
    return [round(values[-1]+step*i,2) for i in range(1,months+1)]

def run(path='data/revenue.csv'):
    with open(path,newline='') as f: values=[float(r['revenue']) for r in csv.DictReader(f)]
    if len(values)<3: raise ValueError('At least three months are required')
    holdout=forecast(values[:-1],1)[0]
    return {'baseline':forecast(values),'upside':forecast(values,multiplier=1.3),
            'downside':forecast(values,multiplier=0.5),'holdout_abs_error':round(abs(holdout-values[-1]),2)}

if __name__ == '__main__':
    import json
    print(json.dumps(run(), indent=2))
