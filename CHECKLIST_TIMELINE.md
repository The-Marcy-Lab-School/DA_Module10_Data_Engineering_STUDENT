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

## Day 2-3 — The real pipeline

- [ ] `extract`/`transform`/`load` implemented for real (replacing the
      given template's TODOs).
- [ ] A real full-dataset aggregation run, its result cross-checked
      against a real small local pandas hand-computation.
- [ ] Real Delta table written into your real Unity Catalog Workspace
      catalog.

## Day 4 — Delta Lake, for real

- [ ] A real update applied to your Delta table.
- [ ] A real time-travel query, back to the version before the update —
      confirmed it returns the real pre-update data.

## Day 5 — The real Databricks Workflow

- [ ] Your notebook wired into a real Job/Workflow.
- [ ] A real, successful Workflow run triggered and confirmed — not just
      cells run in order in the notebook editor.

## Day 6 — Security review

- [ ] The real issue(s) in `starter/Dockerfile` found and fixed.
- [ ] The real over-permissive setting in `starter/sample_s3_policy.json`
      found and fixed.

## Day 7 — Cloud comparison, architecture analysis

- [ ] `starter/cloud_comparison_matrix.md` filled in for real, every
      service name checked against that provider's current docs.
- [ ] The one-page written comparison, with a real non-obvious
      difference and a real, specific security consideration.
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
- [ ] A real Delta table in your real Unity Catalog, a real update, a
      real time-travel query.
- [ ] A real, successful Databricks Workflow run.
- [ ] The given Dockerfile's real issue(s) and the given S3 policy's
      real issue, both fixed.
- [ ] A real, current, one-page cloud-comparison writeup.
- [ ] A real, written 10x-growth bottleneck analysis.
