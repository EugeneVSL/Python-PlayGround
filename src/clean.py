import pandas as pd
import numpy as np
from datetime import datetime
from time import strptime

data_df = pd.read_csv("bank_marketing.csv")

# create the client_df
client = data_df[['client_id', 'age', 'job', 'marital', 'education', 'credit_default', 'mortgage']]

client['job'] = client['job'].str.replace('.', '_')
client['education'] = client['education'].str.replace('.', '_')
client['education'] = client['education'].str.replace('unknown', str(np.NaN))

client['credit_default'] = client['credit_default'].map({'yes': 1,'unknown': 0, 'no': 0})
client['credit_default'] = client['credit_default'].astype(bool)

client['mortgage'] = client['mortgage'].map({'yes':1,'unknown': 0, 'no': 0})
client['mortgage'] = client['mortgage'].astype(bool)

client.to_csv('client.csv', index=False)

#  create the campaign datafame
campaign = data_df[['client_id', 'number_contacts', 'contact_duration', 'previous_campaign_contacts', 'previous_outcome', 'campaign_outcome']]

campaign['previous_outcome'] = campaign['previous_outcome'].map({'success': 1,'failure': 0, 'nonexistent': 0})
campaign['previous_outcome'] = campaign['previous_outcome'].astype(bool)

campaign['campaign_outcome'] = campaign['campaign_outcome'].map({'yes': 1,'unknown': 0, 'no': 0})
campaign['campaign_outcome'] = campaign['campaign_outcome'].astype(bool)

last_contact_date = []
date_format = '%Y-%m-%d'

for row in data_df.itertuples():
    new_date = f"2022-{strptime(row[8],'%b').tm_mon}-{row[9]}"
    new_val = datetime.strptime(new_date, date_format)
    last_contact_date.append(new_val.strftime('%Y-%m-%d'))

campaign['last_contact_date'] = last_contact_date
campaign.to_csv('campaign.csv', index=False)


# create economics df
economics = data_df[['client_id', 'cons_price_idx', 'euribor_three_months']]
economics.to_csv('economics.csv', index=False)