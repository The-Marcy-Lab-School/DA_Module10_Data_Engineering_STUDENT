# Databricks notebook source
# GIVEN TEMPLATE. Real structure, real TODOs -- fill these in, but your
# actual independent project (see MVP.md) needs more than this.
#
# This is a real Databricks notebook in plain-text "source" format.
# In your workspace: Workspace -> Import -> upload this file directly.
# Each "# COMMAND ----------" line becomes its own real notebook cell.

# COMMAND ----------

# TODO: point this at your own real, chosen dataset. Bound it to a
# real window (see GETTING_STARTED.md) so a full run doesn't trip
# Databricks Free Edition's quota.
RAW_PATH = "/Volumes/workspace/default/raw/*.csv"  # TODO
CATALOG = "workspace"
SCHEMA = "default"
BRONZE_TABLE = "TODO_bronze_table_name"
SILVER_TABLE = "TODO_silver_table_name"
GOLD_TABLE = "TODO_gold_table_name"

# COMMAND ----------

# BRONZE: raw data, unmodified. No cleanup here -- that's silver's job.
raise NotImplementedError("TODO: read RAW_PATH, write unmodified to a real bronze Delta table")

# COMMAND ----------

# SILVER: real cleanup/validation, reading FROM bronze. Decide for real
# how to handle nulls (e.g. a cancelled flight has no arrival delay)
# and say why in required_components.md.
raise NotImplementedError("TODO: read from bronze, clean it for real, write a real silver Delta table")

# COMMAND ----------

# GOLD: a real aggregation across the FULL silver dataset, not a
# sample. Cross-check the result against a small local pandas
# hand-computation before trusting it.
raise NotImplementedError(
    f"TODO: read from silver, aggregate, write to '{CATALOG}.{SCHEMA}.{GOLD_TABLE}'"
)

# COMMAND ----------

# TODO (required): a real update on your gold table that changes a
# real value (not a no-op), and a real time-travel query back to the
# version before it. See required_components.md Section 2.

# COMMAND ----------

# TODO (required): wire this notebook into a real Databricks Workflow
# and trigger a real run from there. See required_components.md
# Section 3.
