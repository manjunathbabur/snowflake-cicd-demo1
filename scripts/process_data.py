import snowflake.connector

# Snowflake connection details
conn = snowflake.connector.connect(
     user='MRAJAMANI',
    password='Muruga@20608',
    account='mg05545.eu-west-1'
)

cursor = conn.cursor()

try:
    # Example query execution
    cursor.execute("SELECT CURRENT_TIMESTAMP();")
    for row in cursor:
        print(f"Current Timestamp: {row[0]}")
finally:
    cursor.close()
    conn.close()
