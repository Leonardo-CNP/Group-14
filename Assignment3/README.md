# Assignment 3 — Boolean-Network Mutation Analysis

## The three assignment questions (Q1–Q3)

### Q1 — Which mutation is most dangerous, and why?

**Mutations A (p53 knockout), B (MYC amplification) and C (MDM2 over-expression)
are the most dangerous — and in this model they are exactly equally so.** Each one
raises the fraction of initial cell states that end up in a cancer-like attractor from
~3 % to 50.0 %, while mutations D (p21 knockout) stays at 3.12 %.

| Genotype | # attractors | max period | cancer-% |
|---|:---:|:---:|---:|
| normal      | 3 (fixed points)         | 1 | 3.12 % |
| A – p53 KO  | 2 (fixed points)         | 1 | 50.00 % |
| B – MYC amp | 2 (fixed points)         | 1 | 50.00 % |
| C – MDM2 OE | 2 (fixed points)         | 1 | 50.00 % |
| D – p21 KO  | 5 (incl. two 3-cycles)   | 3 | 3.12 % |

TIn the Stressed (repairable damage) scenario a normal
cell dies, but under A/B/C it now grows instead:

| Genotype | Healthy | Stressed (damage) |
|---|:---:|:---:|
| normal      | G=1 D=0 p53=0 | G=0 D=1 p53=1 (dies) |
| A – p53 KO  | G=1 D=0 p53=0 | G=1 D=0 p53=0 (grows) |
| B – MYC amp | G=1 D=0 p53=0 | G=1 D=0 p53=0 (grows) |
| C – MDM2 OE | G=1 D=0 p53=0 | G=1 D=0 p53=0 (grows) |
| D – p21 KO  | G=1 D=0 p53=0 | G=0 D=1 p53=1 (dies) |

All three dangerous mutations converge on the same target: they make
`p53 = DNA_damage AND NOT MDM2` permanently false. In A it is forced off directly; in B,
MYC always ON keeps `MDM2 = MYC` ON so p53 can never turn on; in C, MDM2 is forced ON.
With p53 dead, any cell that ever has DNA damage divides. Because exactly half of all 256 initial states
start with `DNA_damage = 1`, each dangerous genotype is 50 %.


### Q2 — Role of feedback loops (e.g., MYC → MDM2 → p53)

The model has two such loops, and both are
positive-feedback (double-negative) toggles:

```
MYC ->+ MDM2 --| p53 --| MYC        product (+)(−)(−) = +1   positive loop
MDM2 --| p53 ->+ p21 --| MYC ->+ MDM2  product (−)(+)(−)(+) = +1  positive loop
```

The named example `MYC → MDM2 → p53` is double-negative:
MYC turns on MDM2, MDM2 suppresses p53, and p53 represses MYC. The sign of a
loop is the product of its edge signs, so three inhibitory-style interactions give
(+)(−)(−)= +1 — a positive feedback loop, not a negative one.

What that means: A single mutation changes *basins of
attraction* rather than just flipping one state — the toggle can be in either one. It also
explains Q1: forcing either of `MYC–MDM2–p53` into the "checkpoint-off" versions (A, B or C) tips the whole positive loop for every DNA-damaged cell, collapsing 3 attractors down to 2 and doubling cancer-% from ~3 % to 50 %.


### Q3 — Three limitations of this Boolean network model

1. Binary states ignore dose, thresholds and kinetics: Every gene is only 0 or 1 there are
   no concentrations, half-lives or activation thresholds. Consequences in this model: a mutation
   (e.g. MYC amp) is an all-or-nothing ON, so partialeffects cannot be represented,
   and the sharp `50 %` vs `3.12 %` jump does not loook realistic.

2. Synchronous updating is an idealisation: All nodes update simultaneously every tick; real
   cells have different delays, so node update timing matters.
   The presence of period-3 limit cycles in mutation D shows the dynamics are genuinely sensitive to
   timing — a random/asynchronous scheme could land on different attractors and change
   basin sizes.

3. Fixed topology, single-hit mutations only: The network is static and one node is mutated at a
   time. This does not really happen in real life. Generally the model is only testing a small subset of what is possible 
