# Import packages
from sqlalchemy import create_engine, text
import pandas as pd

chinook_db = 'sqlite:///C:\\Users\\eugen\\AppData\\Roaming\\DBeaverData\\workspace6\\.metadata\\sample-database-sqlite-1\\Chinook.db'
nothwind_db = 'sqlite:///data/sqlite/northwind.db'

# Create engine: engine
engine = create_engine(chinook_db)

# Open engine connection
con = engine.connect()

# Perform query: rs
rs = con.execute(text("SELECT * FROM Album"))

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())