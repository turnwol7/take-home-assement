import pandas as pd
import os

def create_sql_file(rewards_path='rewards.csv', delegators_path='delegators.csv', output_file='create_tables.sql'):
    rewards = pd.read_csv(rewards_path)
    delegators = pd.read_csv(delegators_path)

    with open(output_file, 'w') as f:
        f.write("""CREATE TABLE rewards (
        protocol VARCHAR(3),
        address VARCHAR(50),
        amount NUMERIC,
        date DATE
    );\n\n""")

        f.write("""CREATE TABLE delegators (
        protocol VARCHAR(3),
        address VARCHAR(50),
        total_figment_staked NUMERIC,
        total_staked NUMERIC
    );\n\n""")

        for _, row in rewards.iterrows():
            f.write(f"INSERT INTO rewards VALUES ('{row.protocol}', '{row.address}', {row.amount}, '{row.date}');\n")

        for _, row in delegators.iterrows():
            # this could be improved. Maybe the manual way of entering numbers with commas can be standardized
            figment = row.total_figment_staked.replace(',', '')
            staked = row.total_staked.replace(',', '')
            f.write(f"INSERT INTO delegators VALUES ('{row.protocol}', '{row.address}', {figment}, {staked});\n")

def test_create_sql_file():
    #simple test to make sure the 2 table statements and 2 insert statements were created in SQL file
    create_sql_file()
    
    assert os.path.exists('create_tables.sql'), "SQL file was not created"
    
    with open('create_tables.sql', 'r') as f:
        content = f.read()
        assert 'CREATE TABLE rewards' in content, "Rewards table creation missing"
        assert 'CREATE TABLE delegators' in content, "Delegators table creation missing"
        assert 'INSERT INTO rewards' in content, "Rewards inserts missing"
        assert 'INSERT INTO delegators' in content, "Delegators inserts missing"

if __name__ == "__main__":
    create_sql_file()
    test_create_sql_file()
    print("tests passed ✅")