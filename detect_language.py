"""
Modified version of the detect_language() function from:
http://blog.alejandronolla.com/2013/05/15/detecting-text-language-with-python-and-nltk/

Could not find it on his Github so I copy pasted it.

A function to detect languages locally.

Added param to detect language between a set of specified languages
to narrow down the search field.
"""


from nltk import wordpunct_tokenize

try:
    from nltk.corpus import stopwords
except:
    import nltk
#     nltk.set_proxy()
    nltk.download('stopwords')
    from nltk.corpus import stopwords


def _calculate_languages_ratios(text, languages):
    """
    Calculate probability of given text to be written in several languages and
    return a dictionary that looks like {'french': 2, 'spanish': 4, 'english': 0}
    
    :param str text: Text whose language want to be detected
    :param array-like languages: Set of languages to choose between
    :return: Dictionary with languages and unique stopwords seen in analyzed text
    :rtype: dict
    """

    languages_ratios = {}

    '''
    nltk.wordpunct_tokenize() splits all punctuations into separate tokens
    
    >>> wordpunct_tokenize("That's thirty minutes away. I'll be there in ten.")
    ['That', "'", 's', 'thirty', 'minutes', 'away', '.', 'I', "'", 'll', 'be', 'there', 'in', 'ten', '.']
    '''

    tokens = wordpunct_tokenize(text)
    words = [word.lower() for word in tokens]

    # Compute per specified language the number of unique stopwords appearing in analyzed text
    for language in languages:
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)

        languages_ratios[language] = len(common_elements) # language "score"

    return languages_ratios


def detect_language(text, languages=None):
    """
    Calculate probability of given text to be written in several languages and
    return the highest scored.
    
    It uses a stopwords based approach, counting how many unique stopwords
    are seen in analyzed text.
    
    :param str text: Text whose language want to be detected
    :param array-like languages: Set of languages to choose between
    :return: Most scored language guessed
    :rtype: str
    """
    
    if languages:

        invalid_languages = set(languages) - set(stopwords.fileids())
        if invalid_languages:
            raise ValueError("Valid values for the `languages` param are '{}', "
                             "these given field(s) are invalid: '{}'"
                             .format("', '".join(stopwords.fileids()),
                                     "', '".join(invalid_languages))
            )
    else:
        languages = stopwords.fileids()

    ratios = _calculate_languages_ratios(text, languages)
    most_rated_language = max(ratios, key=ratios.get)
    return most_rated_language


