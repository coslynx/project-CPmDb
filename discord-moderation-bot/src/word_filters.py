# word_filters.py (Python)

import re

class WordFilters:
    def __init__(self):
        self.filters = []

    def add_filter(self, word):
        self.filters.append(word)

    def remove_filter(self, word):
        if word in self.filters:
            self.filters.remove(word)

    def filter_message(self, message):
        for word in self.filters:
            message = re.sub(r"\b" + re.escape(word) + r"\b", "****", message, flags=re.IGNORECASE)
        return message

# End of word_filters.py