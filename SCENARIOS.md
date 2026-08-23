# Your Real Dataset

Unlike Module 3-8, this project doesn't reuse your own domain — you're
picking a new, large, real public dataset. Pick one.

## Option 1: BTS On-Time Performance data (recommended default)

Real flight-level on-time performance data from the U.S. Bureau of
Transportation Statistics — U.S. Government Work, genuinely public
domain. **Use the real, direct download mechanism** (the
`bts.gov/airline-data-downloads` landing page blocks automated/bot
traffic, but the actual data portal doesn't):

```
https://transtats.bts.gov/PREZIP/On_Time_Reporting_Carrier_On_Time_Performance_1987_present_<YEAR>_<MONTH>.zip
```

e.g. `..._2024_1.zip` for January 2024. Confirmed live and real —
**about 27MB and ~550,000 real rows per month**.

**Bound your real window to 3 real years (36 months)** — genuinely
tens of millions of real rows, large enough that a full-dataset
aggregation actually needs real distributed processing, without
risking Databricks Free Edition's quota shutdown from pulling the
entire multi-decade archive.

Real columns worth knowing before you design your aggregation:
`Reporting_Airline`, `Year`, `Month`, `Origin`, `Dest`,
`DepDelayMinutes`, `ArrDelayMinutes`, `Cancelled`, `Distance`. A real,
meaningful business question this supports: which airlines have the
worst on-time performance, and is it improving or getting worse over
time?

## Option 2: CMS data

Real, live, U.S. Government Work public-domain data at
[data.cms.gov](https://data.cms.gov/) — but the specific
synthetic/de-identified claims dataset this curriculum originally
pointed at no longer resolves. You'll need to browse the current
catalog yourself for a suitable current dataset — a real, normal part
of working with public data (sources change), not a sign you're doing
something wrong.

## Either way

- Bound your real dataset to a real, specific, sized-for-the-task
  window — "the whole thing" isn't the assignment, and on Databricks
  Free Edition it's a real quota risk.
- Your aggregation needs to run against the **full** bounded dataset,
  not a sample — that's the actual point of this module.
