# Databricks notebook source
# GIVEN TEMPLATE -- real structure, real TODOs. This mirrors objective 1's
# own "following a template notebook" guided rep -- the independent
# project itself asks you to build this without a template (see
# ../MVP.md), so don't just fill in these TODOs and call the project
# done.
#
# Real, verified pattern (this exact shape -- read CSV(s), aggregate at
# scale, write Delta into your Workspace catalog -- was built and run
# for real against 3 real years of BTS On-Time Performance data before
# this template was written; see ../../../instructor/solution/ if
# you're the instructor reading this).
#
# HOW TO USE THIS FILE: this is a real Databricks notebook in its
# plain-text "source" format (the "# Databricks notebook source" line
# above is not a comment for you to delete -- it's what makes Databricks
# recognize this as a notebook). In your Databricks workspace:
# Workspace -> Import -> upload this file directly. Each
# "# COMMAND ----------" line below becomes its own real notebook cell.

# COMMAND ----------

# TODO: pick your own real data window -- 3 real years is enough to
# need real distributed processing without tripping Databricks Free
# Edition's quota (see ../GETTING_STARTED.md). Point this at wherever
# you've staged your own real, chosen dataset.
RAW_PATH = "/Volumes/workspace/default/raw/*.csv"  # TODO: your real path
CATALOG = "workspace"      # Free Edition's real default catalog
SCHEMA = "default"         # TODO: consider a real schema of your own
TABLE_NAME = "TODO_your_table_name"

# COMMAND ----------

# EXTRACT: TODO -- read your real raw data for real.
# Real gotcha, confirmed while building this: inferSchema is fine at
# this scale, but check a few columns after reading -- BTS's own delay
# columns are real, genuine floats with real nulls (a cancelled flight
# has no arrival delay), not something to silently coerce to 0 without
# deciding whether that's actually the right call for your aggregation.
raise NotImplementedError("TODO: implement extract -- read RAW_PATH for real")

# COMMAND ----------

# TRANSFORM: TODO -- a real aggregation across the FULL dataset, not a
# sample (common_project_mistakes' #1 real trap). Before you trust the
# Spark result: compute the same real number by hand against a small
# local pandas slice first (exemplar_guidance's own instruction), then
# confirm your Spark aggregate matches it exactly for that slice.
raise NotImplementedError("TODO: implement transform -- a real groupBy/agg at full scale")

# COMMAND ----------

# LOAD: TODO -- write into your real Unity Catalog table, not a bare
# Delta path. Free Edition gives every workspace a real "workspace"
# catalog with a "default" schema you already have access to, no admin
# needed -- confirm this is real for your own account before assuming
# it (Databricks' own docs, checked live while building this template,
# confirm it's automatic for any workspace created after Nov 2023).
raise NotImplementedError(
    f"TODO: implement load -- df.write.format('delta').saveAsTable('{CATALOG}.{SCHEMA}.{TABLE_NAME}')"
)

# COMMAND ----------

# TODO (required, not optional): demonstrate a real Delta update AND a
# real time-travel query back to the version before it -- an
# unexercised "Delta Lake" claim with no real ACID/versioning feature
# shown is common_project_mistakes' #2 real trap. See
# required_components.md Section 2.

# COMMAND ----------

# TODO (required): once this notebook runs cleanly end to end, wire it
# into a real Databricks Workflow (Workflows -> Create Job -> add this
# notebook as a real task) and trigger a real run from there -- not
# just "I ran the cells in order once." See required_components.md
# Section 3.
