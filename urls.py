import pandas as pd

class Urls:
    url_result = "https://www.goal.com/en/results/"

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.list_urls = self.get_list_days()

    def get_list_days(self):
        days_list = [i.strftime("%Y-%m-%d") for i in pd.date_range(start=self.start_date, end=self.end_date, freq='D')]
        return days_list

    def get_list_full_urls_pages(self):
        list_full_urls = []
        for i in self.list_urls:
            list_full_urls.append(Urls.url_result + i)
        return list_full_urls
