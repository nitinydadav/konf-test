import requests
from fuzzywuzzy import fuzz
from fuzzywuzzy import process



def make_request():
    url = "https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences"
    response = requests.get(url)
    return response.json()


data =  make_request()
paid = data["paid"]
conf_info = "Hi, amazing {conf_name} is happening at {venue}, {city} from {start_date} to {end_date}. It's {type} ,please check {link} for more detials."

def task_1():
    for item in paid :
        message=conf_info.format(conf_name=item["confName"], venue=item["venue"],city=item["city"],start_date=item["confStartDate"],end_date=item["confStartDate"], type=item["entryType"], link=item["confUrl"])
        print(message)


def task_2():
    item1 = []
    for item in paid:
        conf_name = item["confName"]
        if conf_name not in item1:
            item1.append(conf_name)
        else:
            print("conf {conf_name} is duplicate".format(conf_name=conf_name))

def task_3():
    for dic_1 in paid:
        name_1 = dic_1['confName']
        for dic_2 in paid:
            name_2 = dic_2['confName']
            match_ratio = fuzz.ratio(name_1, name_2)
            if match_ratio >= 55 and match_ratio!= 100:
                print("approx match found: ", (name_1, name_2))


task_1()
task_2()
task_3()






