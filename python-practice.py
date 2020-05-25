voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
{"county":"Denver", "registered_voters": 463353},
{"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    county = county_dict['county']
    for voters in county_dict:
        voters = county_dict['registered_voters']
    print(f'{county} county has {voters:,} registered voters.')
    