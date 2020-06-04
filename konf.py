import requests

url = "https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences"
response = requests.get(url)
data = response.json()


print(data.keys())

#print(data["paid"])


paid = data["paid"]


conf_info = "Hi, amazing {conf_name} is happening at {venue}, {city} from {start_date} to {end_date}. It's {type} ,please check {link} for more detials."

for item in paid :
    message=conf_info.format(conf_name=item["confName"], venue=item["venue"],city=item["city"],start_date=item["confStartDate"],end_date=item["confStartDate"], type=item["entryType"], link=item["confUrl"])
    print(message)
