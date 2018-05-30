import pandas as pd

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

if __name__ == "__main__":
    print(date_info.dtypes)
