# Checklist & Timeline

**8 days, run as a sprint.** This module has the most tested skills of
any project so far — real setup cost (a real cloud signup, a real new
compute engine) on Day 1 is expected, not falling behind.

## Day 1 — Databricks signup, Unity Catalog, dataset choice

- [ ] Real Databricks Free Edition account created.
- [ ] Confirmed your real Workspace catalog exists (no admin setup
      needed).
- [ ] `starter/pyspark_job.py` imported into your workspace as a real
      notebook.
- [ ] Picked your real dataset and real bounded window (`SCENARIOS.md`).

## Day 2-3 — The real pipeline (bronze / silver / gold)

- [ ] Bronze, silver, and gold implemented for real (replacing the
      given template's TODOs).
- [ ] A real full-dataset aggregation run (gold), its result
      cross-checked against a real small local pandas hand-computation.
- [ ] All three real Delta tables written into your real Unity Catalog
      Workspace catalog.

## Day 4 — Delta Lake, for real

- [ ] A real update applied to your Delta table.
- [ ] A real time-travel query, back to the version before the update —
      confirmed it returns the real pre-update data.

## Day 5 — The real Databricks Workflow

- [ ] Your notebook wired into a real Job/Workflow.
- [ ] A real, successful Workflow run triggered and confirmed — not just
      cells run in order in the notebook editor.

## Day 6-7 — Pipeline/compute/cloud writeup, architecture analysis

- [ ] `required_components.md` Section 4: a real, written explanation
      of your pipeline and compute choices, and what would actually
      need to change (storage, scaling, security) running this in
      production on a real cloud.
- [ ] The real 10x-growth bottleneck analysis written.

## Day 8 — Finish, submit

- [ ] `starter/required_components.md` fully filled in with real
      evidence.
- [ ] Commit and push.

**Heads-up**: a real share-out session runs after this project is due —
you'll walk a small group through your actual running Workflow. Nothing
to prepare in advance beyond the real project itself.

## Submission checklist

- [ ] A real PySpark job, run on Databricks Free Edition against the
      **full** bounded dataset, not a sample.
- [ ] A real bronze/silver/gold pipeline in your real Unity Catalog, a
      real update on gold, a real time-travel query.
- [ ] A real, successful Databricks Workflow run.
- [ ] A real, written pipeline/compute/cloud-deployment explanation,
      with a real, specific security consideration.
- [ ] A real, written 10x-growth bottleneck analysis.
- [ ] **Delete `PROJECT_OVERVIEW.md` and `SCENARIOS.md`** — they explain
      the assignment, not your project; a real portfolio repo shouldn't
      have "here's what you were asked to build" sitting in it.
- [ ] **Replace `README.md`'s content with your own real project README**
      — write it for someone who's never seen this assignment:
  - **Business Problem** — what your pipeline processes, and why.
  - **Medallion Architecture Overview** — your real bronze/silver/gold
    design.
  - **Key Findings** — what your gold-layer data actually shows.
  - **Cloud & Compute Reflection** — your real deployment/security/
    scaling write-up.
