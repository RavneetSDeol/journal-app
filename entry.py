class Journal_Entry():
    def __init__(self, date, title, body):
        self.date = date
        self.title = title
        self.body = body

    def to_dict(self):
        return {
            'date': self.date,
            'title': self.title,
            'body': self.body
        }

    @staticmethod
    def from_dict(journal_entry_dict):
        return Journal_Entry(
            date=journal_entry_dict['date'],
            title=journal_entry_dict['title'],
            body=journal_entry_dict['body']
        )