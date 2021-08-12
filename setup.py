import psycopg2
import yaml


# Initiating connection to postgres db with given dsn
def connect(dsn):
    conn = None
    try:
        print("Connecting to Database...")
        conn = psycopg2.connect(**dsn)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        exit(1)
    print("Database connection successful.")
    return conn


# Reading the project's yaml file for database connection info
def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)
