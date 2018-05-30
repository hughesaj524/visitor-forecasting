import pandas as pd
import matplotlib as plt
import numpy as np

air = {
    "reserve": pd.read_csv("../data/air/air_reserve.csv", parse_dates=["visit_datetime", "reserve_datetime"]),
    "store_info": pd.read_csv("../data/air/air_store_info.csv"),
    "visit_data": pd.read_csv("../data/air/air_visit_data.csv", parse_dates=["visit_date"])
}

hpg = {
    "reserve": pd.read_csv("../data/hpg/hpg_reserve.csv", parse_dates=["visit_datetime", "reserve_datetime"]),
    "store_info": pd.read_csv("../data/hpg/hpg_store_info.csv")
}

date_info = pd.read_csv("../data/date_info.csv", parse_dates=["calendar_date"])
store_id_relation = pd.read_csv("../data/store_id_relation.csv")

# FEATURES (+ natural - engineered)
# + whether the day is a holiday or not
# - what day of the week it is
# + restaurant type
# - FIXME: location of restaurant TODO: (relative density?)
# - prefecture (first word of area_name)
# - TODO: weather
# + reservations (note cancellations and walk-ins: relationship to holidays)

air["visit_data"]["day_of_week"] = air["visit_data"]["visit_date"].dt.dayofweek

corr_table = air["visit_data"]
corr_table = pd.merge(corr_table, air["store_info"]["air_genre_name"].to_frame(), on="air_store_id")
corr_table = pd.merge(corr_table, date_info["calendar_date", "holiday_flg"],
                      left_on="visit_date", right_on="calendar_date")
"""
if __name__ == "__main__":
    air["visit_data"].groupby('day_of_week')['visitors'].mean().plot(kind="bar")

    visits_by_holiday = date_info["calendar_date", "holiday_flg"]
    visits_by_holiday["day_of_week"] = visits_by_holiday["calendar_date"].dt.dayofweek
    visits_by_holiday["visitors"] = air["visit_data"]["visitors"]

    holiday_weekday = pd.DataFrame(columns=["Holiday", "Workday"],
                                   index=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    visits_by_holiday.groupby("week_holiday")["visitors"].mean().plot(kind="bar")

    plt.pyplot.show()
"""