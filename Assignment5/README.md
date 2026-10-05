# Task 1:

# Task 2:
- Question: "In your own words: how is a cell's wall stiffness reduced as a function of its chemical level?"

Answer: For normal plant cells, the pathogen chemical level is scaled as Chemical(0) / 0.5 and capped at 1.2. If this scaled level is above 0.1, wall stiffness is reduced according to stiffness = 3 - patho_chem_level. Therefore, more chemical causes lower wall stiffness. With the cap, stiffness can decrease from 3 to 1.8.

- Queston: "What does the pathogen do differently?"

Answer: The pathogen behaves differently because it is excluded from this wall softening rule, so its wall stiffness remains 3. Instead, the pathogen enlarges its target area and divides when it becomes large enough, allowing it to grow into the weakened tissue.

# Task 3:
- Question: "How is the diffusion coefficient defined? Explain the feedback loop this creates and sketch it: chemical lowers stiffness, lower stiffness raises diffusion, faster diffusion spreads the chemical."

Answer: The diffusion coefficient is inversely proportional to the average wall stiffness. For stiffness above 0.001, the model uses D = 0.00001 / stiffness. Therefore, softer walls have a larger diffusion coefficient and allow the pathogen chemical to spread faster between cells.

Sketch:
More pathogen chemical → Lower wall stiffness → Higher diffusion coefficient → Faster chemical spread → More chemical in neighbouring cells → further wall softening

- Question: "Is this positive or negative feedback?"

Answer: This is positive feedback because the initial increase in chemical promotes processes that cause the chemical to spread even faster.


# Task 4:

# Task 5:

# Task 6:

