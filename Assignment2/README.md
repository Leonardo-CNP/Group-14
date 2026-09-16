## How to run:
pip install -r Assignment2/requirements.txt
In Assignment2/metabolic_modeling_assignment.ipynb, click "Run All"

# Part 1:
a:
We explain the difference between mass balance and maximal reaction activities
b:
We explain the visualization of reactions that have no data associated with them and those with an activation capacity of 0, which are visualized in the same way on our ESCHER map.

# Part 2

The code checks wether every reaction has a value in expressions. If it is reversible the lower an upper bounds to the positive and negative of the values. For glucose exchange reaction we remove its pre-existing maximal absolute flux bound and use the high absolute default bound instead. For ATPM flux is left as is. These are the two exeptions that need to be handled. The code then prints every reaction with its upper and lower value.

# Part 3:
a:
Goal: maximise biomass under the **internal** enzyme-activity constraints (using 'model.optimize()') → maximal specific growth rate of≈ **0.873/h**.
b:
Goal: re-enforce an **external** glucose‑uptake limit of 5 mmol/gDW/h and explain how this
"environmental / substrate-supply" constraint differs from the internal expression-based ones.
c:
Goal: compare internal constraint cell vs. internal AND external constraint cell for maximal biomass, with the later dropping to less than half the maximal biomass.

# Part 4:
a: 
Plot the function of Growth Rate vs. Increasing Glucose Uptake, over the [1, 15] mmol/gDW/h bounds.
b:
Full answer in the notebook.
c:
EX_ac_e