# Project Overview: Cloud & Distributed Data Platforms

## The objective

Build a real, end-to-end **PySpark job on Databricks** that reads a
large real dataset (millions of real rows), writes it into a **Delta
Lake table in your real Unity Catalog**, performs a real aggregation
across the **full** dataset (not a sample), and runs as a real
**Databricks Workflow** — plus a real, one-page written comparison of
how the same architecture would deploy on AWS, Azure, and GCP,
including a real, specific security consideration.

## Why it matters

Every project so far has run on a single machine. This is the first
time "the data is too big for one computer" is real, not hypothetical —
Spark's whole design exists because a single-threaded script genuinely
can't process this at scale. It's also your first real exposure to how
the same architecture looks across the three major cloud providers, and
your first real container/storage **security review** — a Dockerfile
and an S3 policy that look fine at a glance, with real issues underneath.
**Module 15's capstone** reuses `databricks` directly.

## Deliverables at a glance

- A real PySpark job, run on **Databricks Free Edition** (Databricks'
  real current free tier — the name changed from "Community Edition,"
  which was retired in 2025; see `GETTING_STARTED.md`), reading your
  real dataset end to end, not a truncated sample.
- A real Delta Lake table in your real Unity Catalog workspace catalog
  — a real update applied, a real prior version queried via time-travel.
- Your real PySpark notebook wired into and run as a real **Databricks
  Workflow** (Job).
- A real, current, one-page cloud-comparison writeup — every service
  name checked against that provider's own current docs.
- The given `Dockerfile`'s real security issue(s) found and fixed; the
  given `sample_s3_policy.json`'s real over-permissive setting found
  and fixed.
- A real, written 10x-data-growth bottleneck analysis.

## Skills you'll practice

- **Databricks / Apache Spark / PySpark** — a real distributed job,
  not a single-machine script.
- **Distributed Systems / Scalability** — why partitioning enables
  parallelism, and where your own architecture would break first at
  10x scale.
- **Delta Lake / Data Lake** — real ACID guarantees and time-travel,
  demonstrated, not just described.
- **AWS / Azure / GCP** — real, current service-name literacy across
  all three, at a comparative depth (not deep mastery of any one).
- **Docker / Cybersecurity / S3** — a real container and real
  storage-policy security review, each with a real fix.
- **Cloud Architecture** — describing/evaluating a real
  storage/compute architecture under real growth pressure.

## Timeline

8 days. See `CHECKLIST_TIMELINE.md` for the day-by-day sprint pace and
the full submission checklist.

## Where to start

Go to `README.md`, then `GETTING_STARTED.md` — a real JDK check if
you're doing any local development, the real Databricks Free Edition
signup, and the real quota-shutdown risk this module's `SCENARIOS.md`
data choices are already designed around.
