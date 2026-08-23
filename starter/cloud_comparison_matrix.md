# Cloud Comparison Matrix

**Given as a real, partially-filled starting point** (objective 3's own
"provided comparison matrix"). The first row is filled in for you, real
and verified against each provider's own current docs as of this
writing — fill in the rest for real, checking each provider's own
current docs yourself (per `exemplar_guidance`: ground every claim in
the provider's own current documentation page, not memory or an
unverified AI summary — service names do change, see this module's own
`instructor/overview.md` for a real example).

| Capability | AWS | Azure | GCP |
|---|---|---|---|
| Object storage | Amazon S3 | Azure Blob Storage / ADLS Gen2 | Google Cloud Storage |
| Managed Spark | TODO | TODO | TODO |
| Managed data warehouse / lakehouse | TODO | TODO | TODO |
| Identity & access management | TODO | TODO | TODO |
| Workflow orchestration | TODO | TODO | TODO |

## Your one-page written comparison

Fill this in for real — this is graded, not the table above alone (the
table is a reference; the real deliverable is the written analysis the
module's own deliverable text asks for):

**How would the same architecture (your real Databricks/Spark/Delta
pipeline) be deployed on each of AWS, Azure, and GCP?** Name the real,
current, specific services you'd actually use on each — not generic
category names.

**At least one real, non-obvious difference between the three
providers**, specific to this workload (not just "they have different
names for the same thing" — what would actually change about how you'd
build this?):

**At least one real, specific security consideration** for deploying
this architecture on a real cloud provider (tie it to something real
from the Dockerfile/S3-policy review below if it fits):
