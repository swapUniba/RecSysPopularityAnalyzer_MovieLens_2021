import csv

import pandas as pd
from enum import Enum


class Category(Enum):
    COLD = 1
    REGULAR = 2
    HOT = 3


################## EDIT HERE TO CHANGE CONFIGS ############################
RECS_FILE_NAME = 'doc2vec_descr'
RECS_PATH = '../recs/cb-word-embedding/doc2vec_descr.csv' # input recs file
OUTPUT_FOLDER = '../recs_user/recs_user_cb_word_embedding/'
OUTPUT_FILE_NAME = 'COLD'
TAG = True
COLD_USER_RANGE = 23
REGULAR_USER_MIN = 24
REGULAR_USER_MAX = 175
MODE = Category.COLD
###########################################################################

def pick_tag():
    if TAG:
        return '_'

'''
MOVIELENS
Dalla linea 37 al 43
Estrai i dati che mi interessano dal file indicato nel percorso.
Cambia percorso e separatore per file diversi.
Creo due liste con i rispettivi valori di interesse, in questo caso,
utente e valutazione e con l'uso del dizionario associo ad ogni utente la rispettiva valutazione.
'''
get_id_user_movie = lambda col: (line.split('::')[col - 1] for line in open('../datasets/ml-1m/users.dat'))
get_id_rating = lambda col: (line.split('::')[col - 1] for line in open('../datasets/ml-1m/ratings.dat'))


users_id = list(get_id_user_movie(1))
ratings_id = list(get_id_rating(1))
users_rating_match = {}

for index in users_id:
    users_rating_match[index] = ratings_id.count(index)


'''
Inizializzazione 3 dizionari, uno per ogni categoria di utenti.
Attraverso il for, in base al voto espresso dall'utente verrà inserito nell'apposito dizionario.
'''
user_cold_start = {}
user_regular = {}
user_hot_start = {}

for values in users_rating_match:
    #Memorizzo il valore in una variabile e il confronto con i valori di soglia.

    rating = int(users_rating_match[values])
    if rating <= COLD_USER_RANGE:
        user_cold_start[values] = rating
    elif REGULAR_USER_MIN <= rating <= REGULAR_USER_MAX:
        user_regular[values] = rating
    else:
        user_hot_start[values] = rating


if MODE == Category.COLD:
    category = user_cold_start
elif MODE == Category.REGULAR:
    category = user_regular
else:
    category = user_hot_start


#file output
output_path = OUTPUT_FOLDER + RECS_FILE_NAME + pick_tag() + OUTPUT_FILE_NAME

#file recs
recommender_file = pd.read_csv(RECS_PATH)
# select rows from a DataFrame on column values, as a query.
filtered_recommender = pd.DataFrame(recommender_file.loc[recommender_file['user'].isin(category.keys())])
filtered_recommender.to_csv(output_path, index=False)



