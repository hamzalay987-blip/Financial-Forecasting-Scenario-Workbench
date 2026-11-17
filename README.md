# Financial Forecasting Scenario Workbench

Generates baseline, optimistic, and conservative forecasts from historical monthly revenue.  
Reports rolling trend assumptions and a simple backtest error metric before extending the horizon.

## Problem

Planning teams need an interpretable forecast baseline before attempting complex prediction models.

## Solution and design

Use average month-over-month change with scenario multipliers and a basic holdout error estimate.

**Stack:** Python, time series, scenario planning, FP&A

## Quick start

Requires Python 3.11+ (standard library only for the local demo).

```bash
python main.py
python -m unittest discover -s tests -v
```

A GitHub Actions workflow runs the same tests on pushes and pull requests.

## Project layout

- `main.py`: core processing and a small command-line demonstration
- `data/`, `seeds/`, `models/`, `sql/`, `infra/`, `dags/` or `powerbi/`: included only where relevant
- `tests/`: fixture-based expected-value and repeatability checks

## Engineering decisions

- Narrow scope, realistic field names, and synthetic reproducible inputs
- No credentials, customer records, patient data, API tokens, or paid cloud resources
- Visible business logic and deterministic fixtures rather than screenshots of unverifiable dashboards

## Limits and next iteration

Simple trend baseline for demonstration; not a statistical prediction interval or validated production forecasting model.

A production hardening path would add larger-scale fixtures, alerting, operational runbooks, robust error handling, and integration tests against the real deployment target.

## Portfolio integrity

This is an independently reproducible **portfolio demonstration**, not a claim that these files are employer code or that a cloud workload has been deployed. The fixture data is synthetic.
