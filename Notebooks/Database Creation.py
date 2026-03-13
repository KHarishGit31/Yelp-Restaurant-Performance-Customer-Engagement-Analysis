import pandas as pd
import json
from sqlalchemy import create_engine
from pathlib import Path

DATASET_PATH = Path('yelp_dataset')
DB_PATH = 'sqlite:///yelp.db'
CHUNK_SIZE = 50000

## Engine creation
engine = create_engine(DB_PATH)
print('Database connected successfully')

def stream_json_to_sql(file_path, table_name, drop_cols=None):
    chunk = []
    total = 0

    print(f"Loading {file_path.name} → table `{table_name}`")

    with open(file_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            chunk.append(json.loads(line))

            if i % CHUNK_SIZE == 0:
                df = pd.DataFrame(chunk)

                if drop_cols:
                    df.drop(columns=drop_cols, inplace=True, errors='ignore')

                df.to_sql(table_name, engine, if_exists='append', index=False)

                total += len(df)
                chunk.clear()
                print(f"Inserted {total} rows")

        if chunk:
            df = pd.DataFrame(chunk)

            if drop_cols:
                df.drop(columns=drop_cols, inplace=True, errors='ignore')

            df.to_sql(table_name, engine, if_exists='append', index=False)
            total += len(df)

    print(f"Finished {table_name}: {total} rows\n")
#Load Business table
stream_json_to_sql(
    DATASET_PATH / 'yelp_academic_dataset_business.json',
    'business',
    drop_cols=['attributes','hours']
)

#load review table
stream_json_to_sql(
    DATASET_PATH / 'yelp_academic_dataset_review.json',
    'review'
)

#Load User Table
stream_json_to_sql(
    DATASET_PATH / 'yelp_academic_dataset_user.json',
    'user'
)

#Load Tip Table
stream_json_to_sql(
    DATASET_PATH / 'yelp_academic_dataset_tip.json',
    'tip'
)

#Load Checkin Table
stream_json_to_sql(
    DATASET_PATH / 'yelp_academic_dataset_checkin.json',
    'checkin'
)

#verifying tables
from sqlalchemy import text

with engine.connect() as conn:
    tables = conn.execute(
        text("SELECT name FROM sqlite_master WHERE type='table';")
    ).fetchall()

print('Tables created:')
for t in tables:
    print('-', t[0])


    
    