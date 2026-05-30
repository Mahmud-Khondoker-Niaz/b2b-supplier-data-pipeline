# 🏠 Home Assignment

## 📁 Project Structure

```text
Home Assignment/
├── 📂 Assignment-1-product-supplier-insights/
│   ├── 💻 analysis.py (or Notebook)      # EDA, Data Cleaning, and Analytical Tasks
│   └── 📄 Assignment-1-Report.pdf        # Insights, Methodology, and Recommendations
│
├── 📂 Assignment-2-supplier-harmonisation/
│   ├── 🛠️ pipeline.py                    # API Data Extraction and Harmonization Script
│   └── 📄 Assignment-2-Report.pdf        # Unified Schema Details and Architecture Report
│
└── 📝 README.md                          # Project Overview
```

---

# 📊 Project Overview

This repository contains solutions for two data-focused assignments:

1. **Product & Supplier Insights Analysis**
2. **Supplier Data Harmonisation Pipeline**

Both assignments demonstrate data engineering, data analysis, data quality assessment, and business intelligence capabilities.

---

# 🔹 Assignment 1: Product & Supplier Insights

## Objective

Analyze the provided database tables to assess data quality and generate actionable business insights.

### Data Sources

* Products
* SupplierProductPriceLists
* SupplierProductVariants
* SupplierProductStocks

---

## Key Tasks Completed

### ✅ Data Quality Assessment

Performed a comprehensive data quality review, including:

* Identification of missing and null values
* Detection of duplicate records
* Outlier analysis
* Logical consistency checks

  * Example: Cost Price > Selling Price
  * Invalid stock values
  * Incorrect timestamps

---

### ✅ Feature Engineering

Created additional analytical features to improve business insights:

* **Product Age** (derived from `created_at`)
* **Supplier Product Count**
* **Category-Level Aggregations**
* Product and supplier performance metrics

---

### ✅ Exploratory Data Analysis (EDA)

Conducted exploratory analysis to understand:

* Supplier product distribution
* Product category distribution
* Price variation across categories
* Stock availability patterns
* Supplier contribution and coverage

Visualizations were generated to support findings and recommendations.

---

### ✅ Analytical Deep Dive

Implemented advanced analysis including:

#### Supplier Segmentation

Suppliers were grouped based on:

* Product volume
* Pricing behavior
* Margin characteristics

#### Anomaly Detection

Flagged unusual records such as:

* Negative margins
* Extreme price outliers
* Suspicious inventory values

---

# 🔹 Assignment 2: Supplier Data Harmonisation Pipeline

## Objective

Build a robust ingestion and transformation pipeline capable of collecting, cleaning, and harmonizing supplier data from multiple external sources into a unified catalog.

---

## Key Tasks Completed

### ✅ Data Extraction

Integrated supplier feeds from:

* Midocean
* PF Concept
* Clipper Interall
* XD Connects
* DATA NatuRe

The pipeline programmatically fetches supplier data through the European Sourcing Sandbox API.

---

### ✅ Data Standardization

Resolved inconsistencies across supplier datasets by:

* Normalizing attribute names

  * `clr`, `Colour`, `colour` → `color`
* Standardizing formats
* Converting dimensions to metric units
* Harmonizing currencies and values where required

---

### ✅ Taxonomy Mapping

Created a centralized category mapping system to unify supplier-specific classifications.

Example:

| Supplier Categories | Unified Category |
| ------------------- | ---------------- |
| Mug                 | Drinkware        |
| Bottle              | Drinkware        |
| Flask               | Drinkware        |

A reusable JSON taxonomy map was implemented to support scalable categorization.

---

### ✅ Inventory Modeling

Designed a relational product structure that links:

* Abstract products
* Supplier SKUs
* Product variants
* Tier-based pricing (MOQ)
* Real-time stock availability

---

# 🎯 Unified Target Schema

The harmonisation pipeline transforms heterogeneous supplier data into a consistent, queryable structure.

```json
{
  "product_id": "uuid",
  "name": "string",
  "category": "string",
  "variants": [
    {
      "sku": "string",
      "supplier": "string",
      "color": "string",
      "size": "string",
      "price": 10.50,
      "currency": "EUR",
      "stock": 120
    }
  ]
}
```

---

# 🏗️ Technical Approach

### Data Analysis Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

### Data Engineering Stack

* Python
* Requests
* JSON Processing
* ETL Principles
* Data Transformation Pipelines

---

# 🔒 Security & Data Privacy

> **Important:** To ensure compliance with security best practices and prevent accidental credential exposure, all production connection details have been excluded from this repository.

The following sensitive configurations are managed locally through environment variables:

* Database Host
* Port
* Username
* Password
* API Credentials

Configuration values should be stored in a local `.env` file and must never be committed to version control.

---

# 🚀 How to Run

Detailed setup instructions, dependency installation steps, environment configuration, and execution guidelines are available in the **instruction.txt** file included in the project folder.

Please follow the instructions provided there to run the analysis and pipeline locally.

---

# 📌 Deliverables

| Assignment            | Deliverables                                        |
| --------------------- | --------------------------------------------------- |
| Assignment 1          | `analysis.py` / Notebook, `Assignment-1-Report.pdf` |
| Assignment 2          | `pipeline.py`, `Assignment-2-Report.pdf`            |
| Project Documentation | `README.md`                                         |

---

# 👨‍💻 Author

**Khondoker Niaz Mahmud**

M.Sc. Artificial Intelligence
Brandenburg University of Technology (BTU), Germany
