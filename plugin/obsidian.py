# this is a comment PATH = "literature/piece de stockage.md"

from flox import Flox

class Obsidian(Flox):

    def query(self, query):
        word_count = self.count_words(query)
        self.add_item(
            title=query,
            subtitle=f"Word count: {word_count}"
        )

    def context_menu(self, data):
        pass 

    def count_words(self, query):
        words = query.split()
        return len(words)