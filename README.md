# 🍽️ Databricks Restaurant Analytics Platform

An end-to-end **Databricks Lakehouse Project** built for a large Indian restaurant chain operating in the UAE, designed to simulate a real-world enterprise analytics platform with both **batch** and **real-time streaming pipelines**.
---
# 🚀 Project Overview
The platform processes restaurant operational data, customer reviews, and live order streams to generate real-time business insights and AI-powered analytics.
---
# 📥 Data Ingestion Architecture
Data Ingestion Architecture
The project uses two ingestion patterns:

**Azure SQL Database**
Used for ingesting customers, menus, historical orders, and reviews using **LakeFlow Connect with CDC (Change Data Capture)** for incremental updates.
**Azure Event Hub**
Simulates a live POS system streaming order events every few seconds using **Spark Declarative Pipelines (SDP) and Structured Streaming.**

---
# 🏗️ Medallion Architecture

Implemented a complete **Bronze → Silver → Gold** architecture using **Delta Lake**.

### 🥉 Bronze Layer
Handled raw batch and streaming ingestion with **CDC handling**, **incremental updates**, and immutable source storage.

### 🥈 Silver Layer
Transformed raw data into a scalable **Star Schema** model consisting of fact tables such as `fact_orders`, `fact_order_items`, and `fact_reviews`, along with dimension tables including `dim_customers`, `dim_restaurants`, and `dim_menu_items`.

Additional transformations included **exploding nested order arrays**, **data cleansing**, **deduplication**, **data quality expectations**, and **invalid record handling**.

### 🥇 Gold Layer
Built production-ready **Materialized Views** for **Daily Sales KPIs**, **Customer 360 Analytics**, **Restaurant Performance Metrics**, **Peak Hour Analytics**, and **Review & Sentiment Insights**.

---

# 🧠 AI-Powered Analytics with Mosaic AI

Integrated **Mosaic AI** directly into SQL workflows using `AI_QUERY()` for automated customer review analysis and AI-enriched analytics.

The platform performs **Sentiment Classification** (**Positive**, **Neutral**, **Negative**) along with **Service Issue Detection** for **delivery delays**, **food quality issues**, **staff complaints**, and **pricing concerns**. This demonstrates practical usage of **LLMs inside enterprise ETL pipelines**.

---

# 🔐 Governance & Orchestration

### 🛡️ Unity Catalog
Used for **centralized governance**, **RBAC**, **secure table management**, and standardized `Catalog.Schema.Table` organization.

### ⚙️ Databricks Workflows
Orchestrated **CDC ingestion**, **streaming jobs**, **Silver/Gold transformations**, and **dashboard refresh pipelines**.

---

# 📊 AI/BI Dashboards

Developed interactive dashboards for **Chain Performance Analytics**, **Revenue Trends**, **Peak Order Hours**, **Restaurant Performance**, **Category Analytics**, **Customer Sentiment Trends**, **AI-classified Service Issues**, **Rating Analytics**, and detailed **Review Drilldowns**.

---

# ⚙️ Tech Stack

**Databricks • Apache Spark • Delta Lake • Unity Catalog • LakeFlow Connect CDC • Spark Declarative Pipelines (SDP) • Structured Streaming • Mosaic AI • Databricks SQL • AI/BI Dashboards • Azure Event Hub • Azure SQL Database**
