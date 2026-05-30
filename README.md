# b2b-supplier-data-pipeline
## 📂 Repository Structure

```text
🏠 Home Assignment/
├── 📂 Assignment-1-product-supplier-insights/
│   ├── 💻 analysis.py (or Notebook)  # EDA, Data Cleaning, and Analytical Tasks
│   └── 📄 Assignment-1-Report.pdf     # Insights, methodology, and recommendations
├── 📂 Assignment-2-supplier-harmonisation/
│   ├── 🛠️ pipeline.py                  # API Data extraction and harmonization script
│   └── 📄 Assignment-2-Report.pdf     # Unified schema details and architecture report
└── 📝 README.md                       # Project overview (This file)
📊 Project Overview & Tasks

🔹 Part 1: Product & Supplier InsightsGoal: Analyze database tables (Products, SupplierProductPriceLists, SupplierProductVariants, SupplierProductStocks) to evaluate data quality and extract business intelligence.  Data Quality Assessment: Identified and documented missing/null values, duplicate records, outliers, and logical field inconsistencies (e.g., Cost > Price).  Feature Engineering: Engineered meaningful features including Product Age (via created_at), Supplier Product Count, and Category-level aggregates.  Exploratory Data Analysis (EDA): Evaluated supplier product distributions and price spread across different categories using clean visualizations.  Analytical Deep Dive: Implemented analytical profiling to perform Supplier Segmentation (by volume, margin, and price distribution) or Anomaly Detection (flagging negative margins and price outliers).

🔹 Part 2: Supplier Data Harmonisation PipelineGoal: Build a robust data ingestion pipeline to fetch messy, multi-source supplier data via the European Sourcing Sandbox API and unify it into a shop-ready catalog.  Extraction: Programmatically connected to multi-supplier data streams including Midocean, PF Concept, Clipper Interall, XD Connects, and DATA NatuRe.  Standardization: Normalized mismatched fields (e.g., mapping clr, Colour ➔ color) and converted dimensional units to the metric system.  Taxonomy Mapping: Resolved cross-supplier category conflicts by creating a centralized JSON taxonomy map (e.g., grouping mugs, bottles, flasks under Drinkware).  Inventory Modeling: Structured a multi-variant relational format linking abstract items with supplier SKUs, tier-based pricing (MOQ), and current stock levels.  🎯 Unified Target Schema ExampleThe pipeline unifies and standardizes unstructured data into the following queryable JSON structure:  JSON{
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
🔒 Security & Data Privacy Notice⚠️ Important: To ensure strict compliance with database infrastructure rules and prevent credential leaks, all live production database connections (Host, Port, User, Password) have been explicitly omitted from this public repository.Configurations are handled locally via environment variables (.env).🛠️ How to Run the ProjectDetailed, step-by-step instructions on how to install dependencies, set up the environment, and run the code/pipeline are provided inside the instruction.txt file within the project folder. Please refer to that file to execute the scripts locally.
