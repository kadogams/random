"""
NLTK's TextCat with the possibility of identifying languages
between a set of specified languages, in order to narrow down
the search field.

For more info about TextCat please check the documentation at:
'https://www.nltk.org/api/nltk.classify.html#nltk.classify.textcat.TextCat'
"""


from nltk.classify.textcat import TextCat

try:
    TextCat()
except:
    import nltk
#     nltk.set_proxy()
    nltk.download('crubadan')
    nltk.download('punkt')


######################################################################
## TextCat with extra option
######################################################################


class TextCat_(TextCat):

    def __init__(self, languages=None):
        """ TextCat with the possibility of identifying languages between a set of specified languages.
        If not specified, all available language ngrams are loaded into cache.
        
        :param array-like languages: ISO 639-3 codes of the languages to choose between.
        """
        self._languages = languages
        
        TextCat.__init__(self)
        
        if self._languages:
            
            invalid_languages = set(self._languages) - set(self._corpus.langs())
            if invalid_languages:
                raise ValueError("Valid values for the `languages` param are '{}', "
                                 "these given field(s) are invalid: '{}'"
                                 .format("', '".join(self._corpus.langs()),
                                         "', '".join(invalid_languages))
                )
            
            # Load specified language ngrams into cache
            self._corpus._all_lang_freq = {}
            for lang in self._languages:
                self._corpus.lang_freq(lang)
            print(self._corpus._all_lang_freq.keys())
