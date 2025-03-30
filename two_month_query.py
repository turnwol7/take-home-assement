import pandas as pd
from datetime import datetime, timedelta

delegators = pd.read_csv('delegators.csv')
rewards = pd.read_csv('rewards.csv')

rewards['date'] = pd.to_datetime(rewards['date'], format='%m-%d-%Y')

date_now = datetime.now()
two_months_date = date_now - timedelta(days=60)

two_month_summary = (
    rewards[rewards['date'] >= two_months_date]
    .groupby('address')['amount']
    .sum()
    .reset_index()
    .rename(columns={'amount': 'total_rewards'})
)

print(two_month_summary)
# this 2 month summary from the rewards table outputs the total 2 month SUM for each address
#   address                                         total_rewards
#0  axelar120zgt5384kj4qlrv5z7ag38efgelyfykr6xnjf    13728141183