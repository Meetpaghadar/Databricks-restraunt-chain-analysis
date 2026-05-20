🍽️  Databricks Restaurant Analytics Platform 
An end-to-end Databricks Lakehouse Project built for a large Indian restaurant chain operating in the UAE, designed to simulate a real-world enterprise analytics platform with both batch and real-time streaming pipelines.

🚀 Project Overview
The platform processes restaurant operational data, customer reviews, and live order streams to generate real-time business insights and AI-powered analytics.

Data Ingestion Architecture
The project uses two ingestion patterns:

Azure SQL Database
Used for ingesting customers, menus, historical orders, and reviews using LakeFlow Connect with CDC (Change Data Capture) for incremental updates.
Azure Event Hub
Simulates a live POS system streaming order events every few seconds using Spark Declarative Pipelines (SDP) and Structured Streaming.

🏗️ Medallion Architecture

Implemented a complete Bronze → Silver → Gold architecture using Delta Lake.

Bronze Layer
Raw batch + streaming ingestion
CDC handling
Incremental updates
Immutable source storage
Silver Layer

Transformed raw data into a scalable Star Schema model.

Fact Tables
fact_orders
fact_order_items
fact_reviews
Dimension Tables
dim_customers
dim_restaurants
dim_menu_items

Additional transformations included:

Exploding nested order arrays
Data cleansing
Deduplication
Data quality expectations
Invalid record handling
Gold Layer

Created production-ready Materialized Views for:

Daily Sales KPIs
Customer 360 Analytics
Restaurant Performance Metrics
Peak Hour Analytics
Review & Sentiment Insights
🧠 AI-Powered Analytics with Mosaic AI

Integrated Mosaic AI directly into SQL workflows using AI_QUERY() for automated customer review analysis.

Features
Sentiment Classification
Positive
Neutral
Negative
Service Issue Detection
Delivery Delays
Food Quality Issues
Staff Complaints
Pricing Concerns

This demonstrates practical usage of LLMs inside enterprise ETL pipelines for AI-enriched analytics.

🔐 Governance & Orchestration
Unity Catalog

Used for:

Centralized governance
RBAC
Secure table management
Catalog.Schema.Table organization
Databricks Workflows

Orchestrated:

CDC ingestion
Streaming jobs
Silver/Gold transformations
Dashboard refresh pipelines
📊 AI/BI Dashboards
Chain Performance Dashboard
Revenue Trends
Order Volume
Peak Order Hours
Restaurant Performance
Category Analytics
Review Insight Dashboard
Customer Sentiment Trends
AI-classified Service Issues
Rating Analytics
Review Drilldowns
⚙️ Tech Stack

Databricks Apache Spark Delta Lake Unity Catalog LakeFlow Connect CDC Spark Declarative Pipelines (SDP) Structured Streaming Mosaic AI Databricks SQL AI/BI Dashboards Azure Event Hub Azure SQL Database