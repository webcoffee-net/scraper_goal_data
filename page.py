from requests_html import HTMLSession
import lxml.html


class Page:

    def __init__(self, url):
        self.url = url
        self.page_source = self.get_page_source_from_one_page()
        xpath_text_title_page = "//div[@class='page-header']//div[@class='page-header__title']//text()"
        self.title_page = self.get_title_page_by_xpath(self.page_source, xpath_text_title_page)[0]
        xpath_list_attr_id_boxes = "//div[@class='main-content']//div[@class='competition-matches']//@data-competition-id"
        self.list_id = self.get_list_id_box_to_page(self.page_source, xpath_list_attr_id_boxes)
        self.list_id_clean = self.list_filterd_id_to_box()


    def get_page_source_from_one_page(self):
        sess = HTMLSession()
        source_html = sess.get(self.url)
        return source_html.text

    def get_title_page_by_xpath(self, page_source, xpath):
        root_elemnt = lxml.html.fromstring(page_source)
        data = root_elemnt.xpath(xpath)
        return data

    def get_list_id_box_to_page(self, page_source, xpath):
        root_elemnt = lxml.html.fromstring(page_source)
        data = root_elemnt.xpath(xpath)
        return data

    def box_is_not_empty(self, page_source, xpath):
        root_elemnt = lxml.html.fromstring(page_source)
        data = root_elemnt.xpath(xpath)
        if len(data) > 1:
            return True
        elif len(data) <= 1:
            return False

    def set_xpath_from_id_to_check_full_box_from_page(self, id_box):
        xpath_box_is_empty_by_id = "//div[@class='main-content']//div[@class='competition-matches' and @data-competition-id='{}']//div[@class='match-row-list']//div[contains(@class,'match-main-data')]".format(
            id_box)
        return xpath_box_is_empty_by_id

    def check_count_box_is_full(self):
        list_id_box = self.list_id
        count_box_is_full = 0
        for i in list_id_box:
            if self.box_is_not_empty(self.page_source, self.set_xpath_from_id_to_check_full_box_from_page(i)):
                count_box_is_full += 1
        return count_box_is_full

    def list_filterd_id_to_box(self):
        list_id = []
        for i in self.list_id:
            if self.box_is_not_empty(self.page_source, self.set_xpath_from_id_to_check_full_box_from_page(i)):
                list_id.append(i)
        return list_id
