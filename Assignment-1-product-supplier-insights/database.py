import pandas as pd
from sqlalchemy import create_engine
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS

def get_engine():
    """Create and return database connection"""
    connection_url = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(connection_url)
    return engine

def fetch_all_data():
        """Fetch all tables from the database and return as dataframes"""

        try:
              engine = get_engine()
              print("Database connection succesfull")

              #Fecth all 4 tables
              products = pd.read_sql('SELECT * FROM "Products"', engine)
              print(f"Products loaded: {len(products)} rows")

              price_lists = pd.read_sql('SELECT * FROM "SupplierProductPriceLists"', engine)
              print(f"Price lists loaded: {len(price_lists)} rows")

              variants = pd.read_sql('SELECT * FROM "SupplierProductVariants"', engine)
              print(f"Variants loaded: {len(variants)} rows")

              stocks = pd.read_sql('SELECT * FROM "SupplierProductStocks"', engine)
              print(f"Stocks loaded: {len(stocks)} rows")

              # Return all tables as a dictionary
              return {
               "products": products,
               "price_lists": price_lists,
               "variants": variants,
               "stocks": stocks
              }

        except Exception as e:
         print("Database connection failed")
         print(f"Reason: {e}")
         return None

