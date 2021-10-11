from lenskit.datasets import ML1M

import operator
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


################## EDIT HERE TO CHANGE CONFIGS ########################################
MIN_POSITIVE_RATING = 4  # minimum rating to consider an item as liked
NUM_OF_RECS = 10  # num of recs for each user
OUTPUT_FOLDER = '../recs/personalized_pagerank/'  # output folder
OUTPUT_FILE_NAME = 'personalized_pagerank'  # output filename (NO NEED TO ADD .csv)
PROPERTY = False  # add properties
#######################################################################################


df = ML1M('../datasets/ml-1m').ratings

#data processing
user_set = set(df['user'])

i = 0

user = []
user = df['user']
item = []
item = df['item']
ratings = []
ratings = df['rating']

user1 = []
item1 = []

for t in user:
    user1.append(t)
add = 'p'
Test = ''

for i in item:
    Test = add + str(i)
    item1.append(Test)
    Test = ''

item_set = set(item1)

#Create graph
G = nx.DiGraph()

#Creating User set of nodes
G.add_nodes_from(user)

#Creating Item set of nodes
G.add_nodes_from(item1)

#Adding Edge among nodes
i = 0
while i < len(user):
        if ratings[i] >= MIN_POSITIVE_RATING:
                G.add_edge(user[i], item1[i])
        i = i + 1


#Show graph
def show_graph(Graph):
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()

#Articles not rated by the user
def not_rated_item(user):
    cont = 0
    it = []
    for x in user1:
        item1[cont]
        if x != user:
            it.append(item1[cont])
        cont = cont + 1
    return it

#Articles rated by the user
def rated_item(user):
    cont = 0
    it1 = []
    for x in user1:
        item1[cont]
        if x == user:
            it1.append(item1[cont])
        cont = cont + 1
    return it1

######################## PROPERTY #######################

if PROPERTY:

    dt = pd.read_csv('../datasets/movies-tags.csv')
    it = []
    it = dt['item']
    prop = []
    prop = dt['tags']

    it1 = []
    add_t = 'p'
    Test_t = ''

    for i in it:
        Test_t = add_t + str(i)
        it1.append(Test_t)

    prop1 = []
    add_pro = 'v'
    Test_pro = ''

    for pro in prop:
        Test_pro = add_pro + str(pro)
        prop1.append(Test_pro)

    # Creating property set of nodes
    G.add_nodes_from(prop1)

    cont = 0
    for p in item_set:
        cont = 0
        for c in it1:
            if p == c:
                G.add_edge(p, prop1[cont])
            cont = cont + 1
########################################################

#Output path of file

output_path = OUTPUT_FOLDER + OUTPUT_FILE_NAME + '.csv'

############################### PPR #############################################

# write csv doc header
f = open(output_path, 'w')
f.write('user,item,score\n')
f.close()

for u in user_set:
    print(u)
    # Dictionary creation for pagerank customization for user u
    customized = {}
    tot = 0
    supp = []
    list1 = G[u]
    y = not_rated_item(u)
    for e in y:
        if e not in list1:
            supp.append(e)
    try:
        value = 0.8 / len(list1)
        remainder = 0.2 / len(supp)

        for ele in list1:
            customized[ele] = value
            tot = tot + value
        x = rated_item(u)
        for el in x:
            if el not in list1:
                customized[el] = 0
        for s in supp:
            customized[s] = remainder
            tot = tot + remainder
        # Personalized Pagerank calculation
        ppr = nx.pagerank(G, personalization=customized)
        sen_rank = sorted(ppr.items(), key=operator.itemgetter(1), reverse=True)

        # Ordered pagerank
        ord = []
        for nodes in sen_rank:
            if ('p' in str(nodes[:1])):
                ord.append(str(nodes[:1]))

        # Data processing
        aux = []
        for i in ord:
            x = i.replace('(', '')
            x = x.replace("'", '')
            x = x.replace(",", '')
            x = x.replace(")", '')
            aux.append(x)

        c = 0
        for i in aux:
            if c < NUM_OF_RECS:
                if (i not in list1) and (i in y):
                    x = i.replace('p', '')
                    f = open(output_path, 'a')
                    f.write('{},{},{}\n'.format(u, x, ppr[i]))
                    f.close()
                    c = c + 1
    except ZeroDivisionError:
        print('Skipping user ' + str(u))