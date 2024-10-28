class French:
    def __init__(self, lang):
        self.lang = lang

    def greeting(self):
        return 'Bonjour'


class English:
    def __init__(self, lang):
        self.lang = lang

    def greeting(self):
        return 'Hello'


class Korean:
    def __init__(self, lang):
        self.lang = lang

    def greeting(self):
        return '안녕하세요'


french = French(lang='French')
english = English(lang='English')
korean = Korean(lang='Korean')
print(french.greeting(), english.greeting(), korean.greeting())
