import lxml.html


class Lines:

    def __init__(self, page_source, id_box, data_match_id):

        self.page_source = page_source

        self.id_box = id_box
        self.data_match_id = data_match_id

        self.xpath_title_box_by_id = "//div[@class='main-content']//div[@class='competition-matches' and @data-competition-id='{}']//div[@class='competition-name']//text()".format(id_box)
        self.xpath_list_name_team_home_by_id = "//div[@class='main-content']//div[@class='competition-matches' and @data-competition-id='{}']//div[@class='match-row-list']//div[contains(@data-match-id, '{}')]//div[@class='match-main-data']//div[@class='match-data']//div[contains(@itemprop,'homeTeam')]//span[@class='team-name']//text()".format(id_box, data_match_id)
        self.xpath_list_name_team_away_by_id = "//div[@class='main-content']//div[@class='competition-matches' and @data-competition-id='{}']//div[@class='match-row-list']//div[contains(@data-match-id, '{}')]//div[@class='match-main-data']//div[@class='match-data']//div[contains(@itemprop,'awayTeam')]//span[@class='team-name']//text()".format(id_box, data_match_id)
        self.xpath_list_score_team_home_by_id = "//div[@class='main-content']//div[@class='competition-matches' and @data-competition-id='{}']//div[@class='match-row-list']//div[contains(@data-match-id, '{}')]//div[@class='match-main-data']//div[@class='match-data']//div[contains(@itemprop,'homeTeam')]//span[@class='goals']//text()".format(id_box, data_match_id)
        self.xpath_list_score_team_away_by_id = "//div[@class='main-content']//div[@class='competition-matches' and @data-competition-id='{}']//div[@class='match-row-list']//div[contains(@data-match-id, '{}')]//div[@class='match-main-data']//div[@class='match-data']//div[contains(@itemprop,'awayTeam')]//span[@class='goals']//text()".format(id_box, data_match_id)
        self.xpath_list_datetime_line_by_id = "//div[@class='main-content']//div[@class='competition-matches' and @data-competition-id='{}']//div[@class='match-row-list']//div[contains(@data-match-id, '{}')]//div[@class='match-main-data']//div[@class='match-status']//time//@datetime".format(id_box, data_match_id)
        self.xpath_list_state_line_by_id = "//div[@class='main-content']//div[@class='competition-matches' and @data-competition-id='{}']//div[@class='match-row-list']//div[contains(@data-match-id, '{}')]//div[@class='match-main-data']//div[@class='match-status']//span[@data-bind='state']//text()".format(id_box, data_match_id)

        self.title = self.get_list_title(self.page_source, self.xpath_title_box_by_id)[0]
        self.list_name_home = self.get_list_name_home(self.page_source, self.xpath_list_name_team_home_by_id)
        self.list_name_away = self.get_list_name_away(self.page_source, self.xpath_list_name_team_away_by_id)
        self.list_score_home = self.get_list_scour_home(self.page_source, self.xpath_list_score_team_home_by_id)
        self.list_score_away = self.get_list_scour_away(self.page_source, self.xpath_list_score_team_away_by_id)
        self.list_datetime = self.get_list_datetime(self.page_source, self.xpath_list_datetime_line_by_id)
        self.list_state = self.get_list_state(self.page_source, self.xpath_list_state_line_by_id)

    def get_list_title(self, page_source, xpath):
        root_elemnt = lxml.html.fromstring(page_source)
        data = root_elemnt.xpath(xpath)
        return data

    def get_list_name_home(self, page_source, xpath):
        root_elemnt = lxml.html.fromstring(page_source)
        data = root_elemnt.xpath(xpath)
        return data

    def get_list_name_away(self, page_source, xpath):
        root_elemnt = lxml.html.fromstring(page_source)
        data = root_elemnt.xpath(xpath)
        return data

    def get_list_scour_home(self, page_source, xpath):
        root_elemnt = lxml.html.fromstring(page_source)
        data = root_elemnt.xpath(xpath)
        return data

    def get_list_scour_away(self, page_source, xpath):
        root_elemnt = lxml.html.fromstring(page_source)
        data = root_elemnt.xpath(xpath)
        return data

    def get_list_datetime(self, page_source, xpath):
        root_elemnt = lxml.html.fromstring(page_source)
        data = root_elemnt.xpath(xpath)
        return data

    def get_list_state(self, page_source, xpath):
        root_elemnt = lxml.html.fromstring(page_source)
        data = root_elemnt.xpath(xpath)
        return data

    def set_data_from_dict(self):
        lines_data_from_one_box = {"title": self.title,
                                    "id_box": self.id_box,
                                   "data_match_id" : self.data_match_id,
                                    "name_home": self.list_name_home,
                                    "name_away": self.list_name_away,
                                    "score_home": self.list_score_home,
                                    "score_away": self.list_score_away,
                                    "datetime": self.list_datetime,
                                    "state": self.list_state}
        return lines_data_from_one_box
