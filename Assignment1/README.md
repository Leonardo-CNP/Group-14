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

How does increasing recovery rate affect peak infections, total deaths, and epidemic duration?

Looking at the first experiment an increase in the recovery rate reduces the peak number of infections greatly from 480 for gamma = 0,05 to 18 for gamma = 0,25. The total number of deaths also falls from 165 to 11, however the peak days sligthly increase (from 26 to 30), with the highest number of 33 days at gamma = 0,20.

- 4.2 Intervention analysis

If an intervention could increase recovery rate by 50%, what would be the expected impact on total deaths? Scenario A as baseline.

To examine a recovery rate increase of 50% we could look at the experiments and the change in deats from gamma = 0,10 and gamma = 0,15.

In the first experiment we see a fall in deaths from 84 to 48.
In Scenario A the fall in deaths is from 160 and 103.
In Scenario B the deaths change from 37 and 14.

Across all experiments we also see a significant drop in peak infections, however the length of the peak in days stays relatively the same. 

Looking deeper into Scenario A the fall in deaths from 160 to 103 represent a decrease of 35,6%. The peak infected fall from 340 to 213, decrease of 37,4%. The peak days go up very slightly from 22 to 24.

- 4.3 Real-world application

Name one real medical intervention that could increase recovery rates. Explain the mechanism and estimate realistic effectiveness.

Anti-viral treatments plus quick and redily available at home testing could double the recovery rate. This could help provide earlier more effective treatments and move people out of the infected category at twice the rate. Using Scenario A as a baseline we compare gamma = 0,05 and 0,10 the total number of deats decreases from 285 to 160 (a fall of 43,9%). In a real world scenario this is already a really great result in terms of saving lives.

---

## 5. Conclusions

Conclusions from Part 1: Higher recovery rates reduced the peak number of infections, lowered total deaths, and decreased R₀. This shows that faster recovery can significantly reduce epidemic severity by decreasing the number of people infected, the number of deaths, and the number of people requiring treatment at the same time. Interestingly, the epidemic peak generally occurred later as the recovery rate increased.
Conclusions from Part 2: In the low transmission scenario, we can see the epidemic disappear into a contained outbreak as the recovery rate grows. The high transmission scenario on the other hand consistently keeps the death toll high, no matter the recovery rate. When analyzing the peak of the epidemic wave in both scenarios compared by their recovery rates, we can see that the recovery rate delays the timing of the peak, or moves it to day 0 in the contained outbreak scenario mentioned above.
Conclusions from Part 3: The experiments show that recovery rate is a strong driver of epidemic outcomes. Raising γ from 0.05 to 0.25 cuts the infection peak from 480 to 18 and deaths from 165 to 11, while the timing of the peak changes only slightly. A 50% increase in recovery (γ = 0.10 to 0.15) reduces deaths in every setting: 84 to 48 in the first experiment, 160 to 103 in Scenario A (−35.6%), and 37 to 14 in Scenario B. Peak infections fall by a similar share (340 to 213, −37.4% in Scenario A), but the epidemic does not last much longer. Doubling recovery through antivirals and rapid at-home testing (Scenario A, γ = 0.05 to 0.10) lowers deaths from 285 to 160 (−43.9%).