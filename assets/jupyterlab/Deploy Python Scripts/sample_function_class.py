def detect_country(text:str) -> str:
    import langdetect
    import pycountry
    langcode = langdetect.detect(text)
    country = pycountry.countries.get(alpha_2=langcode).name
    return country

class Employee:

    def __init__(self, first, last, gender):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.gender = gender

    def fullname(self):
        return '{} {}'.format(self.first, self.last)