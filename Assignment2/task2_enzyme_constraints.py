import csv
import cobra
from cobra.io import load_model

model = load_model('textbook')  # unexpected errors when loading e_coli_core.json so this is fix

filename = 'e_coli_core_expression.csv'
activity_data = {}

with open(filename, mode='r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        if not row or row[0].startswith('#'):
            continue
        reaction_id = row[0].strip()
        value = float(row[1])
        activity_data[reaction_id] = value

for reaction in model.reactions:

    if reaction.id in activity_data:
        value = activity_data[reaction.id]

        if reaction.reversibility:
            reaction.lower_bound = -value
            reaction.upper_bound = value
        else:
            reaction.lower_bound = 0
            reaction.upper_bound = value

# for glucose exchange reaction we remove its pre-existing maximal absolute flux bound and use the high absolute default bound instead
glc_exchange = model.reactions.get_by_id('EX_glc__D_e')
glc_exchange.lower_bound = -1000.0   # highest absolute default bound
glc_exchange.upper_bound = 1000.0

#ATPM flux is left as is
atpm = model.reactions.get_by_id('ATPM')
atpm.lower_bound = atpm.lower_bound

print(f"{'Reaction ID':<15}{'Lower bound':>15}{'Upper bound':>15}")
for reaction in model.reactions:
    print(f"{reaction.id:<15}{reaction.lower_bound:>15.4g}{reaction.upper_bound:>15.4g}")
