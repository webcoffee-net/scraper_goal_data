import lxml.html


class Box:
    def __init__(self, page_source, id_box):
        self.page_source = page_source
        self.id_box = id_box

        xpath_text_title_box = "//div[@class='main-content']//div[@class='competition-matches' and @data-competition-id='{}']//div[@class='competition-name']//text()".format(id_box)
        self.list_title_box = self.get_list_title_box_to_page(self.page_source, xpath_text_title_box)

        xpath_list_data_match_id = "//div[@class='main-content']//div[@class='competition-matches' and @data-competition-id='{}']//div[@class='match-row-list']//div[contains(@class, 'match-row')]//@data-match-id".format(id_box)
        self.dict_data_id_lines_by_id_box = self.get_dict_data_id_lines_by_id_box(self.id_box, self.page_source, xpath_list_data_match_id)

    def get_list_title_box_to_page(self, page_source, xpath):
        root_elemnt = lxml.html.fromstring(page_source)
        data = root_elemnt.xpath(xpath)
        return data

    def get_dict_data_id_lines_by_id_box(self, id_box, page_source, xpath):
        data_dict_id_box_and_id_lines = {}
        root_elemnt = lxml.html.fromstring(page_source)
        data = root_elemnt.xpath(xpath)
        dic = data_dict_id_box_and_id_lines[id_box] = data
        return dic
