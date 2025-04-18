# BODSI_TOOLKIT

The **Bi-Objective Dynamic Systems Identification (BODSI_TOOLKIT)** is a Python toolkit designed to identify dynamic systems based on Polynomial NARX models using a bi-objective optimization approach. It balances two core objectives:

1. **Dynamic Error Minimization**
2. **Static Curve Fitting**

This results in a **Pareto-Optimal Set of Candidate Models**, leveraging the *p-lambda* technique:
> J(Parameters) = λ * Ed + (1 - λ) * Ee

Where:
- `Ed` = dynamic error  
- `Ee` = static error  
- `λ` = user-defined weight between objectives

If the identified polynomial structure suits both the dynamic and static aspects of the system, the bi-objective estimator will generate unbiased parameters [[1]](#reference).

---

## 📦 Installation

### 🔹 Option 1 – via `pip`

```bash
pip install bodsi-toolkit
```

> Ensure you have Python ≥ 3.8 installed and `pip` is up to date.

---

### 🔹 Option 2 – via `conda` (recommended for scientific environments)

```bash
conda create -n bodsi-env python=3.8
conda activate bodsi-env
pip install bodsi-toolkit
```

---

### 🔹 Option 3 – Manual installation (from source)

```bash
git clone https://github.com/your-org/bodsi-toolkit.git
cd bodsi-toolkit
pip install .
```

---

## 🚀 Features

The `BODSI_TOOLKIT` class offers 23 methods to support bi-objective dynamic system identification:

| #  | Method Name                   | Description |
|----|-------------------------------|-------------|
| 1  | `generateCandidateTerms`     | Generate candidate terms for a polynomial NARX model. |
| 2  | `sortByERR`                  | Sort terms by Error Reduction Ratio (ERR). |
| 3  | `AkaikeInformationCriterion` | Use AIC to help select model terms. |
| 4  | `getClusters`                | Cluster terms and output cluster matrix. |
| 5  | `buildRegressorMatrix`       | Build regressor matrix for dynamic modeling. |
| 6  | `buildStaticMatrix`          | Construct static matrix under equilibrium assumption. |
| 7  | `buildMapping`               | Map estimated parameters to cluster coefficients. |
| 8  | `generateParetoSet`          | Generate Pareto-optimal models using p-lambda. |
| 9  | `correlationDecisionMaker`   | Validate model by correlation with dynamic error. |
| 10 | `getInfo(model)`             | Get model details and metadata. |
| 11 | `simulateModel`              | Simulate model behavior given inputs. |
| 12 | `buildStaticModel`           | Build full static model matrix. |
| 13 | `displayStaticModel`         | Simulate and display static model result (limited cases). |
| 14 | `displayModel`               | Print model structure with delays and parameters. |
| 15 | `rmse`                       | Compute Root Mean Square Error (RMSE). |
| 16 | `correla`                    | Calculate cross-correlation between two signals. |
| 17 | `combinationWithRepetition`  | Generate combinations of terms with repetition. |
| 18 | `delay`                      | Apply time delay to a signal. |
| 19 | `removeClusters`             | Remove spurious clusters from model. |
| 20 | `checkSubarrayForGNLY`       | Check for nonlinearity in `y`. |
| 21 | `correlationFunction`        | Compute correlation function of a signal/vector. |
| 22 | `buildStaticResponse`        | Build static matrix when nonlinearity in `y` ≥ 2. |
| 23 | `buildStaticModelAgroup`     | Build static model under high `y` nonlinearity. |

> Example usage:
```python
from bodsi_toolkit import BODSI_TOOLKIT

model = BODSI_TOOLKIT()
help(model.getInfo)
```

---

## 📚 Reference

<a name="reference"></a>

Barroso, M.F.S., Takahashi, R.H.C., & Aguirre, L.A. (2007).  
*Multi-objective parameter estimation via minimal correlation criterion*.  
Journal of Process Control, 17(4), 321–332.  
[https://doi.org/10.1016/j.jprocont.2006.10.005](https://doi.org/10.1016/j.jprocont.2006.10.005)

---

## 👥 Authors

- **Márcio F. S. Barroso** – Universidade Federal de São João del-Rei (UFSJ)  
- **Eduardo M. A. M. Mendes** – Universidade Federal de Minas Gerais (UFMG)  
- **Jim Jones S. Marciano** – Computer Scientist

📅 March 2025

---

## 📬 Contact & Contributions

Feel free to open issues or pull requests!  
GitHub Repo: [https://github.com/your-org/bodsi-toolkit](https://github.com/your-org/bodsi-toolkit)

---

## 📄 License

MIT License (or insert your license here)
