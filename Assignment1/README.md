# Epidemiological Model Assignment — Parameter Exploration

**Course**: KEN3170 — Multi-scale modeling of biological systems
**Group number**: [14]

---

## 1. Repository overview
- `analysis.ipynb` — main notebook containing all required sections (Setup, Part 1–3, Conclusions)
- `requirements.txt` — Python dependencies (numpy, matplotlib, pandas, scipy, seaborn)
- `README.md` — this file

**How to run**: Run `pip install -r requirements.txt`, then open `analysis.ipynb` and execute all cells from top to bottom

---

## 2. Part 1 — Parameter analysis function
**Function**: `analyze_recovery_rates(beta, mu, N, I0, simulation_days)`

The SIRD model was simulated for five different recovery rates while keeping the transmission rate, mortality rate, population size, and initial number of infected individuals constant. For each recovery rate, the peak number of infections, peak day, total deaths, and R₀ value were calculated and compared.

Results:
   gamma   R0  peak_infected  peak_day  total_deaths
0   0.05  6.0            480        26           165
1   0.10  3.0            269        27            84
2   0.15  2.0            137        30            48
3   0.20  1.5             57        33            26
4   0.25  1.2             18        30            11

---

## 3. Part 2 — Scenario comparison
- Result tables for Scenario A (High Transmission) and Scenario B (Low Transmission)
- Which scenario is worse for public health, and why

---

## 4. Part 3 — Policy recommendations
- 4.1 Parameter impact analysis
- 4.2 Intervention analysis
- 4.3 Real-world application

---

## 5. Conclusions

Conclusions from Part 1: Higher recovery rates reduced the peak number of infections, lowered total deaths, and decreased R₀. This shows that faster recovery can significantly reduce epidemic severity by decreasing the number of people infected, the number of deaths, and the number of people requiring treatment at the same time. Interestingly, the epidemic peak generally occurred later as the recovery rate increased.

Conclusion from Part 3: Working towards reducing the recovery rate by effective and quick use of medicine is a great way to fight a pandemic. An increase in the recovery rate of on 50% could still result in a reductiion of deaths by half or even more as shown by our experiments.The amount of peak infections also decrease by about half, howver the recovery rate does not seem to have a signifficant effect on the lenght of the infection peak as long as R0 is larger than 1. However as soon as we get R0 <= 1, which can be done with a high recovery rate, the spread is no longer pandemic and the number of peak days becomes 0.
