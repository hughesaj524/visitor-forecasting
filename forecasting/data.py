import pandas as pd

air = {
    "reserve": pd.read_csv("../data/air/air_reserve.csv", converters={"visit_datetime": pd.to_datetime,
                                                                      "reserve_datetime": pd.to_datetime}),
    "store_info": pd.read_csv("../data/air/air_store_info.csv"),
    "visit_data": pd.read_csv("../data/air/air_visit_data.csv", converters={"visit_date": pd.to_datetime})
}

hpg = {
    "reserve": pd.read_csv("../data/hpg/hpg_reserve.csv", converters={"visit_datetime": pd.to_datetime,
                                                                      "reserve_datetime": pd.to_datetime}),
    "store_info": pd.read_csv("../data/hpg/hpg_store_info.csv")
}

date_info = pd.read_csv("../data/date_info.csv", converters={"calendar_date": pd.to_datetime,
                                                             "holiday_flg": bool})
store_id_relation = pd.read_csv("../data/store_id_relation.csv")

if __name__ == "__main__":
    print(date_info.dtypes)
