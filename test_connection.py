from database import engine

try:
    connection = engine.connect()
    print("Database Connection Successful")
    connection.close()
except Exception as e:
    print(f"Error: {e}")