import pandas as pd
import snowflake.connector

# Snowflake connection details
conn = snowflake.connector.connect(
    user='MRAJAMANI',
    password='Muruga@20608',
    account='mg05545.eu-west-1'
)

query = "SELECT * FROM POC_CICD_PROD.SH_PROD.TEST_TBL;"
df = pd.read_sql(query, conn)

# Generate report
df.to_csv('report.csv', index=False)
print("Report generated: report.csv")

conn.close()
