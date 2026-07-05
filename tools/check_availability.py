import json
def check_availability(date) : 
    with open("memory/calendar.json", "r") as file: 
        calendar_data = json.load(file)
    for day in calendar_data : 
        if day["date"] == date : 
            return day["slots"]
    return []