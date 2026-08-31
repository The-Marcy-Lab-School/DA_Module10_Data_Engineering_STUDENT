# Project Overview: Cloud & Distributed Data Platforms

## The objective

Build a real, end-to-end **PySpark job on Databricks** that reads a
large real dataset (millions of real rows), writes it into a real
**3-layer bronze/silver/gold Delta Lake pipeline in your real Unity
Catalog**, performs a real aggregation across the **full** dataset (not
a sample), and runs as a real **Databricks Workflow** — plus a real,
written explanation of your pipeline, your compute choices, and what
would actually change if this ran in production on a real cloud.

## Why it matters

Every project so far has run on a single machine. This is the first
time "the data is too big for one computer" is real, not hypothetical —
Spark's whole design exists because a single-threaded script genuinely
can't process this at scale. **Module 15's capstone** reuses
`databricks` directly.

## Deliverables at a glance

- A real PySpark job, run on **Databricks Free Edition** (Databricks'
  real current free tier — the name changed from "Community Edition,"
  which was retired in 2025; see `GETTING_STARTED.md`), reading your
  real dataset end to end, not a truncated sample.
- A real **3-layer medallion architecture** (bronze/silver/gold —
  Databricks' own current terminology) in your real Unity Catalog
  workspace catalog — a real update applied to your gold table, a real
  prior version queried via time-travel.
- Your real PySpark notebook wired into and run as a real **Databricks
  Workflow** (Job).
- A real, written explanation of your pipeline/compute and how it
  would actually run in production on a real cloud, including a real
  security consideration.
- A real, written 10x-data-growth bottleneck analysis.

## Skills you'll practice

- **Databricks / Apache Spark / PySpark** — a real distributed job,
  not a single-machine script.
- **Distributed Systems / Scalability** — why partitioning enables
  parallelism, and where your own architecture would break first at
  10x scale.
- **Delta Lake / Data Lake** — real ACID guarantees and time-travel,
  demonstrated, not just described.
- **Cloud Architecture** — describing/evaluating a real
  storage/compute architecture under real growth pressure, and
  reasoning about what a real cloud deployment would need.

## Timeline

8 days, plus a required share-out session scheduled after. See
`CHECKLIST_TIMELINE.md` for the day-by-day sprint pace and the full
submission checklist.

## Where to start

Go to `README.md`, then `GETTING_STARTED.md` — a real JDK check if
you're doing any local development, the real Databricks Free Edition
signup, and the real quota-shutdown risk this module's `SCENARIOS.md`
data choices are already designed around.
