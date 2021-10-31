import pprint
import string

""" 1. Harvest text from the Internet - IMBD Movie Reviews"""

def find_title_id(movie_title):
    """input movie title, output imbd's id of the movie"""
    from imdbpie import Imdb
    imdb = Imdb()
    info = imdb.search_for_title(movie_title)
    for dic in info:
        return dic['imdb_id']

def import_data(movie_title):
    """input movie title to get the raw data of the movie review"""
    from imdbpie import Imdb
    imdb = Imdb()
    reviews = imdb.get_title_user_reviews(find_title_id(movie_title))
    # print(reviews)
    # {@type: , base: , title , paginationKey, reviews:
    # [
    # {author:{displayName: , userId: }, authorRating: ,
    # helpfulnessScore: , id: , interestingVotes:{down: , up: }, languageCode: , reviewText: , reviewTitle: , spoiler: ,
    # submissionDate: , titleId: }, {}
    # ], 
    # totleReviews: }
    review_text = reviews['reviews']
    return review_text
# print(import_data("La La Land"))

""" 2. Analyzing the Text"""

""" 1) word frequencies count of all reviews"""
def get_review_text_in_list(movie_title): 
    """input movie title output a list in which the each item is a user's review"""
    review_text = import_data(movie_title)
    # # print(review_text)
    all_text = []
    for item in review_text:
        all_text.append(item['reviewText'])
    return all_text
# pprint.pprint(get_review_text_in_list("La La Land"))

def most_common_words_of_all_reviews(movie_title):
    """input movie title, output a list representing word frequency of all reviews
    in which each item is a tuple, key is the frequency of the word and value is the word
    the list is sorted in descending order"""
    all_text = get_review_text_in_list(movie_title)
    reviews_str = ",".join(all_text)
    # print(reviews_str)  
    word_freq = {}
    strippables = string.punctuation + string.whitespace
    # print(strippables)
    reviews_str = reviews_str.replace('-', '')
    reviews_str = reviews_str.replace('\n', ' ')
    reviews_str = reviews_str.replace('(', '')
    reviews_str = reviews_str.replace(')', '')
    reviews_str = reviews_str.replace('...', ' ')
    reviews_str = reviews_str.replace('....', ' ')
    reviews_str = reviews_str.replace('/', ' ')
    reviews_str = reviews_str.replace(';', ' ')
    reviews_str = reviews_str.replace(':', ' ')
    # print(reviews_str)
    all_reviews_list = reviews_str.split()
    # print(all_reviews_list)
    for word in all_reviews_list:
        word = word.strip(strippables)
        word = word.lower()
        word_freq[word] = word_freq.get(word, 0) + 1
    # print(word_freq)
    most_common = []
    for item in word_freq:
        most_common.append((word_freq[item], item))
    sorted_most_common = sorted(most_common, reverse=True)
    return sorted_most_common
# print(most_common_words_of_all_reviews("La La Land"))

""" 2) words in each review """
def raw_review_cleaning(movie_title):
    """input movie title, output a cleaned list in which each item is a user's review
    depriving of punctuations and other marks"""
    all_text_list = get_review_text_in_list(movie_title)
    # pprint.pprint(all_text_list)
    all_text_list = [all_text_list[i].replace('\n', ' ') for i in range(len(all_text_list))]
    all_text_list = [all_text_list[i].replace('-', '') for i in range(len(all_text_list))]
    all_text_list = [all_text_list[i].replace('(', '') for i in range(len(all_text_list))]
    all_text_list = [all_text_list[i].replace(')', '') for i in range(len(all_text_list))]
    all_text_list = [all_text_list[i].replace('...', ' ') for i in range(len(all_text_list))]
    all_text_list = [all_text_list[i].replace('....', ' ') for i in range(len(all_text_list))]
    all_text_list = [all_text_list[i].replace('/', '') for i in range(len(all_text_list))]
    all_text_list = [all_text_list[i].replace('.', '') for i in range(len(all_text_list))]
    all_text_list = [all_text_list[i].replace('*', '') for i in range(len(all_text_list))]
    all_text_list = [all_text_list[i].replace('?', '') for i in range(len(all_text_list))]
    all_text_list = [all_text_list[i].replace('\\', ' ') for i in range(len(all_text_list))]
    all_text_list = [all_text_list[i].replace('"', '') for i in range(len(all_text_list))]
    all_text_list = [all_text_list[i].replace(',', '') for i in range(len(all_text_list))]
    all_text_list = [all_text_list[i].replace(';', '') for i in range(len(all_text_list))]
    all_text_list = [all_text_list[i].replace(':', '') for i in range(len(all_text_list))]
    # pprint.pprint(all_text_list)
    return all_text_list  
# print(raw_review_cleaning("La La Land"))

def list_of_each_review_word_freq(movie_title):
    """input moive title, output a list of dictionaries;
    each dictionary represents word frequency of each review;
    key is word and value is frequency"""
    processed_reviews = raw_review_cleaning(movie_title)
    each_review_list = []
    for r in processed_reviews:
        r = r.split()
        each_review_list.append(r)
    # print(each_review_list)
    loop_dic = {}
    each_review_word_freq = []
    for each_r in each_review_list:
        for w in each_r:
            w = w.lower()
            loop_dic[w] = loop_dic.get(w, 0) + 1
        each_review_word_freq.append(loop_dic)
        loop_dic = {}
    return each_review_word_freq
# pprint.pprint(list_of_each_review_word_freq("La La Land"))

def list_of_sorted_each_review_word_freq(movie_title):
    """input movie title, output a list in which each item is a list of tuples;
    each item represents word frequency of each review in descending order;
    key of each tuple is frequency and value is word"""
    ori_list = list_of_each_review_word_freq(movie_title)
    sorted_each_review_word_freq = []
    loop_ = []
    for dic in ori_list:
        for key in dic:
            loop_.append((dic[key], key))
            loop_sort = sorted(loop_, reverse=True)
        sorted_each_review_word_freq.append(loop_sort)
        loop_ = []
    return sorted_each_review_word_freq
# print(list_of_sorted_each_review_word_freq("La La Land"))

def selected_freq_words_of_each_review(movie_title, n1, n2):
    """input movie title, output a list in which each item is a list of tuples;
    each item represents word frequency of each review in descending order;
    input n1 and n2 as the range of each item wanted"""
    sorted_each_review = list_of_sorted_each_review_word_freq(movie_title)
    each_review_words = []
    for each_list in sorted_each_review:
        each_list = each_list[n1:n2+1]
        each_review_words.append(each_list)
    return each_review_words
# print(selected_freq_words_of_each_review("La La Land", 20, 30))

""" 3) sentiment analysis"""
import nltk
nltk.download('vader_lexicon')
def sentiment_analysis_of_all_reviews(movie_title):
    """input movie title to get the sentiment analysis of the movie;
    the score shows what percent of all reviews contains negative, neutral, positive sentiment respectively"""
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    all_text = get_review_text_in_list(movie_title)
    reviews_str = ",".join(all_text)
    sentence = reviews_str
    score = SentimentIntensityAnalyzer().polarity_scores(sentence)
    return score
# print(sentiment_analysis_of_all_reviews("La La Land"))

def movie_sentiment_avg(*movie_title):
    """input as many movie titles as wanted;
    output the average sentiment analysis score of all movies input"""
    list_m = list(movie_title)
    sum_neg = 0
    sum_neu = 0
    sum_pos = 0
    for m in list_m:
        score = sentiment_analysis_of_all_reviews(m)
        sum_neg += score['neg']
        sum_neu += score['neu']
        sum_pos += score['pos']
        average_score = {'neg':sum_neg/(len(list_m)-1), 'neu':sum_neu/(len(list_m)-1), 'pos':sum_pos/(len(list_m)-1), 'compound':(sum_neg/(len(list_m)-1))+(sum_neu/(len(list_m)-1))+(sum_pos/(len(list_m)-1))}
    return average_score
# print(movie_sentiment_avg("Southside With You", "Maggie's Plan", "Sunset Song", "Bridget Jones's Baby"))

""" 3. Code Testing"""

def main():
    Movie = 'La La Land'
    find_title_id(Movie)
    import_data(Movie)
    get_review_text_in_list(Movie)
    print(most_common_words_of_all_reviews(Movie))
    raw_review_cleaning(Movie)
    list_of_each_review_word_freq(Movie)
    list_of_sorted_each_review_word_freq(Movie)
    print(selected_freq_words_of_each_review(Movie, 20, 30))
    print(sentiment_analysis_of_all_reviews(Movie))
    print(movie_sentiment_avg("Southside With You", "Maggie's Plan", "Sunset Song", "Bridget Jones's Baby"))

if __name__ == "__main__":
    main()