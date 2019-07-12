import os
import math as m
import pandas as pd

os.chdir('dir on server that has the file')

dir = 'same as above' 

df_precalc = pd.read_csv(dir + '/needs_cost_calc.csv')

customers = df_precalc[df_precalc['user_type'] == 'Customer']

cost_calc = lambda minute: 2 + m.ceil(max((minute - 30), 0) / 15) * 3

customers['cost_to_ride'] = customers['duration_min'].apply(cost_calc)

subscribers = df_precalc[df_precalc['user_type'] == 'Subscriber']

cost_calc = lambda minute: m.ceil(max((minute - 45), 0) / 15) * 3

subscribers['cost_to_ride'] = subscribers['duration_min'].apply(cost_calc)

master_df = pd.concat(customers, subscribers)

master_df.to_csv(dir + '/clean_df.csv')