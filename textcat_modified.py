"""
NLTK's TextCat with the possibility of identifying languages
between a set of specified languages, in order to narrow down
the search field.


About TextCat:

A module for language identification using the TextCat algorithm.
An implementation of the text categorization algorithm
presented in Cavnar, W. B. and J. M. Trenkle,
"N-Gram-Based Text Categorization".

The algorithm takes advantage of Zipf's law and uses
n-gram frequencies to profile languages and text-yet to
be identified-then compares using a distance measure.

Language n-grams are provided by the "An Crubadan"
project. A corpus reader was created separately to read
those files.

For details regarding the algorithm, see:
http://www.let.rug.nl/~vannoord/TextCat/textcat.pdf

For details about An Crubadan, see:
http://borel.slu.edu/crubadan/index.html
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
        """ Add the possibility of identifying languages between a set of specified languages.
        If not specified, all available language ngrams are loaded into cache.

        For more info please check the documentation at:
        'https://www.nltk.org/api/nltk.classify.html#nltk.classify.textcat.TextCat'

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
