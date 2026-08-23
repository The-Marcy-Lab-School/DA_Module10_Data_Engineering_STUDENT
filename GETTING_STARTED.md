# Getting Started

## "Use this template" vs. Fork vs. Clone

Same rule as every project: **"Use this template"** on this repo's GitHub
page (not Fork) creates your own independent copy. Clone *that* copy, not
this template directly.

## Step 1: Sign up for Databricks Free Edition

Databricks' free tier is now called **Free Edition** — it replaced the
older "Community Edition" (retired in 2025; if you see "Community
Edition" anywhere, including in some of this curriculum's own generated
text, that's the old name — Free Edition is the real, current thing to
sign up for). Sign up at
[databricks.com/learn/free-edition](https://www.databricks.com/learn/free-edition)
— no credit card confirmed required in Databricks' own current docs.

**Real, confirmed limitations to plan around** (from Databricks' own
current docs):
- Serverless compute only — you can't configure custom clusters.
- Max 5 concurrent job tasks per account — plenty for one pipeline.
- **If you exceed your quota, your whole workspace shuts down for the
  rest of the day** (or, in extreme cases, the rest of the month). This
  is the real reason `SCENARIOS.md` has you bound your dataset to a
  real, specific window rather than pulling everything available.

## Step 2: Unity Catalog — already there, no setup needed

Every Databricks workspace created after November 2023 has Unity
Catalog on by default, and every new workspace gets a real, automatic
**"Workspace catalog"** every user already has access to — no admin
privileges needed. Your real Delta table should land in
`workspace.default.<your_table_name>` (or a schema of your own choosing
under `workspace`), not a bare, catalog-less Delta path.

## Step 3: Import the given notebook

`starter/pyspark_job.py` is a **real Databricks notebook**, written in
Databricks' own plain-text "source" format — the file already starts
with the exact line `# Databricks notebook source`, which is what makes
Databricks recognize it as a notebook, not a plain script.

In your Databricks workspace: **Workspace → your folder → Import** →
upload `starter/pyspark_job.py` directly. It opens as a real notebook,
with each `# COMMAND ----------` line already split into its own cell.

## Step 4 (optional): developing locally before uploading

If you want to write and test your real transform logic locally before
pasting it into Databricks, PySpark and Delta Lake are both real,
free, open-source packages you can run on your own machine — this is
genuinely how many real data engineers develop Spark code before
deploying it. You'll need:

- **A real JDK** (PySpark needs a JVM — check with `java -version`
  first; if you don't have one, install a real JDK, e.g. Temurin 17).
- `pip install pyspark delta-spark` in a dedicated venv (same "don't
  use a big shared environment" discipline as Module 7's own dbt
  finding).

This is optional — Databricks' own notebook environment already has
Spark and Delta Lake ready to go with nothing to install.

## Step 5: your real dataset

See `SCENARIOS.md` for the two real, verified options — pick one and
bound it to a real window (not the entire available history) before
you start building real transform logic.

## Step 6: the real Databricks Workflow

Once your notebook runs cleanly end to end in a normal notebook run:
**Workflows (left sidebar) → Create Job** → add your notebook as a real
task → **Run now**. A real, successful Workflow run — not just cells
executed in order in the notebook editor — is part of the real MVP bar.

## What's next

Once Databricks Free Edition is set up and your notebook is imported,
go back to `README.md`'s "What to do" section and start with picking
your real dataset.
