import shelve

class LinkShortener:
    def __init__(self,db_name="short_links_db"):
        self.db_name = db_name

    def save_link(self, short_link, full_link):
        with shelve.open(self.db_name) as db:
            db[short_link] = full_link

    def get_link(self, link):
        with shelve.open(self.db_name) as db:
            return db[link]