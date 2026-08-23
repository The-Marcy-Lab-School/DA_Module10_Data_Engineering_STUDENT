# MVP — the real bar for "done"

This is what actually gets graded as Meets/Approaching/Below per skill.
See instructor `rubric.md` for the full rubric if your instructor has
shared it — this is the same bar in checklist form.

## The pipeline

- [ ] A real PySpark job, run on Databricks Free Edition, that reads
      your real, chosen, bounded dataset — every real row processed,
      not a sample (`common_project_mistakes` #1: the most common way
      to fail this module).
- [ ] The real full-dataset aggregate result (your **gold** layer,
      below) **cross-checked against a real small local pandas
      hand-computation** for at least one real slice — matching
      exactly.
- [ ] Correctly explains (in `required_components.md`) why this
      workload needs Spark's distributed, partition-based execution —
      not just "it's big data" as an unexamined buzzword.

## A real 3-layer medallion architecture (bronze/silver/gold)

Databricks' own current terminology for a real multi-hop pipeline —
not just one Delta table, three, each a real, distinct step:

- [ ] **Bronze**: your real raw data, written unmodified into a real
      Delta table — preserves original fidelity, no cleanup yet.
- [ ] **Silver**: a real, cleaned/validated Delta table, built from
      bronze — real deduplication/type-enforcement/null-handling
      decisions, made and explained (not silently defaulted).
- [ ] **Gold**: your real, business-ready aggregation across the
      **full** dataset (not a sample), built from silver — the layer a
      real stakeholder would actually query.
- [ ] All three tables written into your real Unity Catalog
      **Workspace catalog** (`workspace.default.<table>` or your own
      schema) — not bare, catalog-less Delta paths.
- [ ] A real update applied to your **gold** table, changing a real
      value (not a no-op — pick something that's genuinely different
      before vs. after), and a real time-travel query that successfully
      returns the real pre-update version — an unexercised "I used
      Delta Lake" claim with no real ACID/versioning feature shown is
      `common_project_mistakes` #2.

## The real Databricks Workflow

- [ ] Your real notebook wired into a real Job/Workflow, and a real,
      successful run triggered from there — not just cells run in order
      in the notebook editor.

## Security review — both real issues found and fixed

- [ ] The real issue(s) in the given `Dockerfile` correctly identified
      (not invented) and a real, concrete fix proposed for each.
- [ ] The real over-permissive setting in the given
      `sample_s3_policy.json` correctly identified and a real, corrected
      policy proposed.

## The cloud comparison — real, current, specific

- [ ] `cloud_comparison_matrix.md` filled in for real; ≥3 services
      correctly mapped across all three providers for your stated
      workload, checked against each provider's **current** docs — not
      memory or an unverified AI summary (`common_project_mistakes` #3).
- [ ] ≥1 real, non-obvious difference between the three providers named,
      specific to this workload.
- [ ] ≥1 real, specific security consideration identified for deploying
      this architecture on a real cloud provider.

## Architecture at scale

- [ ] A real, written 10x-data-growth bottleneck analysis: the specific
      component that would break first, and why.

## What "Below" looks like, concretely

- The "big data" job only ever tested on a tiny sample, never actually
  run against the full dataset.
- Delta Lake used, but no real ACID/time-travel feature ever
  demonstrated.
- The cloud comparison uses outdated or invented service names instead
  of checking current documentation.
- A Dockerfile left running as root, or with secrets hardcoded in, with
  neither issue identified.
