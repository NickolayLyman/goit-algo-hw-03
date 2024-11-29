from datetime import datetime

def get_days_from_today(date):
    try:
        now = datetime.now()
        normalized_string = date.replace(date[4],".")
        normalized_date = datetime.strptime(normalized_string, "%Y.%m.%d") 
        days_differense =  normalized_date-now
        return days_differense.days  + 1

    except ValueError:
        return "Please enter the correct date format, for example 2020-02-12"

    
    
print(get_days_from_today("2024-11-29"))