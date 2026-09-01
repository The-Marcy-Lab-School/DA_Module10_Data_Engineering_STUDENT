# Your Real Dataset

Unlike Modules 3/4/6/7/8/9 (the SQL-through-Data-Engineering run of
projects that all reuse your own established domain), this project
doesn't reuse your own domain — you're picking a new, large, real
public dataset. Pick one.

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

## Option 2: CMS Medicare Physician & Other Practitioners data

Real, live, U.S. Government Work public-domain data — **Medicare
Physician & Other Practitioners by Provider and Service**, confirmed
live and downloaded for real this session:

```
https://data.cms.gov/sites/default/files/2026-05/b5ebab5a-f490-418a-9bce-4b9f31419356/PHY_R26_P05_V10_D24_Prov_Svc.csv
```

(the 2024 file — CMS publishes one file per year back to 2013; check
`https://data.cms.gov/data.json` for the current year's exact URL, since
these filenames include a version hash that changes on republish).

**Real, confirmed size: ~9.78 million rows, ~3.0GB, for a single year.**
This is already the same order of magnitude as Option 1's full 3-year
bound — **use exactly one year, not multiple.** Pulling several years
of this file is a real, fast way to hit Databricks Free Edition's
quota, faster than Option 1's per-month sizing would suggest.

Real columns worth knowing before you design your aggregation:
`Rndrng_NPI` (provider ID), `Rndrng_Prvdr_Last_Org_Name`,
`Rndrng_Prvdr_State_Abrvtn`, `Rndrng_Prvdr_Type` (specialty), `HCPCS_Cd`/
`HCPCS_Desc` (the billed service), `Place_Of_Srvc`, `Tot_Benes`,
`Tot_Srvcs`, `Avg_Sbmtd_Chrg`, `Avg_Mdcr_Alowd_Amt`, `Avg_Mdcr_Pymt_Amt`.
A real, meaningful business question this supports: which provider
specialties or services have the highest average Medicare payment
nationally, and how much do submitted charges diverge from what
Medicare actually pays?

**If you'd rather browse the current catalog yourself** for a different
CMS dataset instead of this one, that's fine too — `data.cms.gov`'s real
catalog changes over time (a normal part of working with public data,
not a sign you're doing something wrong), but confirm your alternative's
real row count and file size **before** committing to it, the same way
this option's numbers above were confirmed, not assumed.

## Either way

- Bound your real dataset to a real, specific, sized-for-the-task
  window — "the whole thing" isn't the assignment, and on Databricks
  Free Edition it's a real quota risk.
- Your aggregation needs to run against the **full** bounded dataset,
  not a sample — that's the actual point of this module.
