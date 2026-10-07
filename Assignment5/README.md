# MSMBS Assignment 5 — VirtualLeaf Pathogen Infection Model


# Task 1: Run the infection model for 2h and describe spread & deformation

Simulations were run with the VirtualLeaf2021 cell-based tissue model using the `pathogen_infection` leaf file. In this model:
- Cell type 0 = xylem (green), type 1 = procambium / mesophyll (blue),
  type 2 = pathogenic fungus (red).
- The pathogen secretes a chemical, Chemical(0); plant cells degrade it.

## Method
The simulation was run from `data/leaves/pathogen_infection.xml`.
Simulated time advances by `rd_dt = 10 s` per timestep, so a full
run to maxt = 7200 s (2h) took 720 steps. VirtualLeaf writes a high-resolution PNG snapshot every step, where we used the initial state and half hour marks as report screenshots.

Screenshot frames taken at init and at half hour marks:

| Simulated time | Frame |
|---|---|
| Initial (t = 0) | `Assignment5/report_frames/task1/0h0m_t=000000.png` |
| +30 min (t = 1800 s) | `Assignment5/report_frames/task1/0h30m_t=001800.png` |
| +60 min (t = 3600 s) | `Assignment5/report_frames/task1/1h0m_t=003600.png` |
| +90 min (t = 5400 s) | `Assignment5/report_frames/task1/1h30m_t=005400.png` |
| +120 min / end (t = 7200 s) | `Assignment5/report_frames/task1/2h0m_t=007200.png` |

## Observations

### How the infected region spreads
The pathogenix fungus starts as a single red cell attached to the procambium layer of the plant tissue. Over the 2h it does not divide, but its secreted chemical diffuses into neighbouring plant cells. The number of cells containing the pathogen chemical and the region they cover grow steadily:

| Sim time | Cells containing pathogen chemical |
|---|---|
| 0 min | 0 |
| 30 min (1800 s) | 23 |
| 60 min (3600 s) | 29 |
| 90 min (5400 s) | 33 |
| 120 min (7200 s) | 37 |

The infected region spreads outward from the pathogen.
The single pathogen cell itself also grows, enlarging its area over the run and pushing into the softened tissue.

### How the tissue deforms
The infection weakens plant-cell walls (see Task 2/3). Specifically, plant cells
that contain pathogen chemical become smaller on average than healthy cells and
shrink further as the infection progresses.

Visually, the originally light blue cells become more purple around the pathogenic cell (red infection tint from chemical), and the blue plant-cell outlines become compressed in the process, likely losing their regular healthy cellular function from the pathogenic chemical.
The leaf boundary itself stays fixed (outer cells are `fixed=true`), so deformation is seen around the infected region.

---

# Task 2: How a cell's wall stiffness is reduced by its chemical level

- **Question:** "In your own words: how is a cell's wall stiffness reduced as a function of its chemical level?"

**Answer:** For normal plant cells, the pathogen chemical level is scaled as `Chemical(0) / 0.5` and capped at 1.2. If this scaled level is above 0.1, wall stiffness is reduced according to `stiffness = 3 - patho_chem_level`. Therefore, more chemical causes lower wall stiffness. With the cap, stiffness can decrease from 3 to 1.8.

- **Question:** "What does the pathogen do differently?"

**Answer:** The pathogen behaves differently because it is excluded from this wall softening rule, so its wall stiffness remains 3. Instead, the pathogen enlarges its target area and divides when it becomes large enough, allowing it to grow into the weakened tissue.

---

# Task 3: Diffusion coefficient & the feedback loop

- **Question:** "How is the diffusion coefficient defined? Explain the feedback loop this creates and sketch it."

**Answer:** The diffusion coefficient is inversely proportional to the average wall stiffness. For stiffness above 0.001, the model uses `D = 0.00001 / stiffness`. Therefore, softer walls have a larger diffusion coefficient and allow the pathogen chemical to spread faster between cells.

**Sketch:**
```
More pathogen chemical → Lower wall stiffness
      ↑                                        ↓
more chem in neighbours ← faster chemical spread ← Higher diffusion (softer)
```

- **Question:** "Is this positive or negative feedback?"

**Answer:** This is **positive feedback**: the initial increase in chemical promotes processes that cause the chemical to spread even faster.

---

# Task 4: Effect of rel_cell_div_threshold on pathogen expansion

## Method
`rel_cell_div_threshold` controls when a cell divides. The fungus enlarges its target area and then calls
`Divide()` once `Area() > rel_cell_div_threshold * BaseArea()`. 
A lower threshold therefore allows the pathogen to divide sooner (at a smaller size); a higher threshold requires it to grow larger before dividing.

Two runs were documented, both for 2h simulated time, identical except for this
parameter. Frames:

**Low threshold (rel_cell_div_threshold = 1.0):**
- `Assignment5/report_frames/task4/low_thr1.0_0h0m_t=000000.png`
- `Assignment5/report_frames/task4/low_thr1.0_0h30m_t=001800.png`
- `Assignment5/report_frames/task4/low_thr1.0_1h0m_t=003600.png`
- `Assignment5/report_frames/task4/low_thr1.0_DIVISION_t=4190s(69min50s).png`(division, t = 70 min)
- `Assignment5/report_frames/task4/low_thr1.0_1h30m_t=005400.png`
- `Assignment5/report_frames/task4/low_thr1.0_2h0m_t=007200.png`

**High threshold (rel_cell_div_threshold = 6.0):**
- `Assignment5/report_frames/task4/high_thr6.0_0h0m_t=000000.png`
- `Assignment5/report_frames/task4/high_thr6.0_0h30m_t=001800.png`
- `Assignment5/report_frames/task4/high_thr6.0_1h0m_t=003600.png`
- `Assignment5/report_frames/task4/high_thr6.0_1h30m_t=005400.png`
- `Assignment5/report_frames/task4/high_thr6.0_2h0m_t=007200.png`

**First division time of the pathogen:**
- Low threshold (1.0): At ~70 min the single fungus divides into two daughter
  cells, doubling their output of the pathogenic chemical.
- High threshold (6.0): never divides within 2h.

## Interpretation

Lowering `rel_cell_div_threshold` makes the pathogen population expand much faster:
with a threshold of 1.0 it divides once by ~70 min, giving two producing cells,
which doubles its chemical output and accelerates spread. Raising the threshold prevents division within the same window because the fungus cannot grow large enough in time, meaning the population stays at 1 cell. So a smaller `rel_cell_div_threshold` speeds up pathogen population expansion (and the chemical spread), whereas a larger one delays or prevents it.

---

# Task 5:

In the previous models the diffusion coefficient for the exchange of chemicals between neighbour cells' walls was fixed, and coupling was also fixed. In our model coupling is dynamic and depends on the mechanical state of both cells. Our model takes the shared wall of both cells and calculates a lenght-weighted average stiffness. This gives us a diffusion coefficeint of 0.00001/stiffness. As cells become infected their stiffness goes down and they become better conected with their neighbours. 

# Task 6:

In CellHouseKeeping we put the new code after line 108 (stiffness_inf = 3 - (patho_chem_level);)

patho_chem_level = min(Chemical(0) / 0.5 ; 1.2)
stiffness_inf = 3

if patho_chem_level > 0.1 and CellType() != 2:
  SetCellVeto(false)
  stiffness_inf = 3 - patho_chem_level

  % the new defensive response
  if Chemical(0) > defence_threshold
    stiffness_inf = stiffness_inf + k_defence * (Chemical(0) - defence_threshold)
    stiffness_inf = min(stiffness_inf, max_stiffness)

  for every wall element of c
    setStiffness(stiffness_inf)
  
  else
    for every wall element
      setStiffness(3)
    SetCellVeto(true)

We introduce the new parameters defence_threshold - the level above which the walls start to stiffen; k_stiffness - how strongly the wall stiffens by unit of chemical above treshold; max_stiffness - the maximum the walls can stiffen.

We have given the plant negative feedback as the initial increase in the chemical will only slow the spread of it. Above the treshhold the walls stiffen and we get a lower diffusion coefficient which slows the spread the chemichal. 