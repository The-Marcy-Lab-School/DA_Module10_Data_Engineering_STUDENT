# Cloud & Distributed Data Platforms Project

Start with `PROJECT_OVERVIEW.md` for what you're building and why. This
file (`README.md`) is where the step-by-step setup lives.

**Due:** 8 days, run as a sprint, plus a required share-out session
scheduled after. See `CHECKLIST_TIMELINE.md` for the
day-by-day pace and the full submission checklist.

This repo is a **GitHub template** — a starting point, not something you
edit directly on Marcy's copy of it.

## Getting started

### Step 1: Get your own copy

On this repo's GitHub page, click **"Use this template" → "Create a new
repository"** (not Fork). Name it something like
`cloud-distributed-data-platforms`, keep it **public**, and create it.

### Step 2: Clone your new repo locally

```bash
git clone <the URL of your own new repo>
cd <your-repo-name>
```

### Step 3: git setup — already done for you this time

Unlike Module 8, `.gitignore` and `LICENSE` are already here —
`git-version-control` is a real prerequisite for this module, not
something newly tested here. Commit as you go, same discipline as
every prior module.

### Step 4: Databricks Free Edition + your real dataset

See `GETTING_STARTED.md` — the real signup walkthrough, the real
`File > Import` step for the given notebook, and the real
quota-shutdown risk to plan around.

## What to do

- `starter/pyspark_job.py` is a **given, real, upload-ready Databricks
  notebook** — real structure (bronze/silver/gold cells), the actual
  logic left as `TODO`/`NotImplementedError`. Following it is the
  guided rep; your real, independent project needs more than filling
  in these TODOs — your instructor's shared checklist has the full
  required scope.
- Build the real pipeline as a real **3-layer medallion architecture**
  (bronze/silver/gold — Databricks' own current terminology): bronze
  holds your real raw data unmodified; silver applies real cleanup/
  validation; gold is your real, full-dataset aggregation (see
  `SCENARIOS.md` for your dataset). All three land in your real Unity
  Catalog Workspace catalog.
- Demonstrate a real Delta update and a real time-travel query on your
  **gold** table — not just a Delta write.
- Wire your notebook into a real **Databricks Workflow** and trigger a
  real run from there.
- Write a real explanation of your pipeline, your compute choices, and
  what would actually need to change (storage, scaling, security) if
  this ran in production on a real cloud — see
  `starter/required_components.md` Section 4.
- Fill in `starter/required_components.md` as you go.

`CHECKLIST_TIMELINE.md` has the suggested day-by-day pace and the full
sequenced checklist.

**Where's the exact bar for "done," and what are the optional stretch
goals?** This repo (your own copy) doesn't include `MVP.md` (your **M**inimum **V**iable **P**roduct —
the required baseline) or `ABOVE_AND_BEYOND.md` on purpose — they're not something to keep sitting
in your portfolio repo. Ask your instructor for the link to this
template's `project-scope` branch to read them, or check the checklist
your instructor shares through the classroom, which covers the same
ground.
