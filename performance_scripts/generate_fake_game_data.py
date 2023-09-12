from faker import Faker

fake = Faker("it_IT")

max_num = 100000000

for _ in range(max_num):
    home_team = fake.first_name()
    visitor_team = fake.first_name()
    if home_team != visitor_team:
        home_score = fake.pyint(min_value=0, max_value=10)
    visitor_score = fake.pyint(min_value=0, max_value=10)
    print(f"{home_team} F.C. {home_score} , {visitor_team} F.C. {visitor_score}")
