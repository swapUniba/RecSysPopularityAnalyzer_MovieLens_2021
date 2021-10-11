from lenskit.datasets import ML1M

import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

################## EDIT HERE TO CHANGE CONFIGS ########################################
MIN_POSITIVE_RATING = 4  # minimum rating to consider an item as liked
NUM_OF_RECS = 10  # num of recs for each user
OUTPUT_FOLDER = '../recs/pagerank/'  # output folder
OUTPUT_FILE_NAME = 'pagerank'  # output filename (NO NEED TO ADD .csv)
PROPERTY = False  # add properties
#######################################################################################


df = ML1M('../datasets/ml-1m').ratings

# data processing
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

# Create graph
G = nx.DiGraph()

# Creating User set of nodes
G.add_nodes_from(user)

# Creating Item set of nodes
G.add_nodes_from(item1)

# Adding Edge among nodes
i = 0
while i < len(user):
    if ratings[i] >= MIN_POSITIVE_RATING:
        G.add_edge(user[i], item1[i])
    i = i + 1


# Show graph
def show_graph(Graph):
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()

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
    add_pro = 't'
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

# Pagerank calculation
PR = []
PR = nx.pagerank(G)

# Ordered pagerank
sen_rank = sorted(PR.items(), key=lambda x: x[1], reverse=True)
# print(sen_rank)
list = []
for nodes in sen_rank:
    if ('p' in str(nodes[:1])):
        list.append(str(nodes[:1]))

# Data processing
# print(list1)
aux = []
for i in list:
    x = i.replace('(', '')
    x = x.replace("'", '')
    x = x.replace(",", '')
    x = x.replace(")", '')
    # print(x)
    aux.append(x)
# print(aux)

# Output path of file

output_path = OUTPUT_FOLDER + OUTPUT_FILE_NAME + '.csv'

# write csv doc header
f = open(output_path, 'w')
f.write('user,item,score\n')
f.close()

for u in user_set:
    print(u)
    list = []
    list = G[u]
    print('------------------')
    c = 0
    for i in aux:
        if c < NUM_OF_RECS:
            ax = []
            ax = PR[i]
            x = i.replace('p', '')
            f = open(output_path, 'a')
            f.write('{},{},{}\n'.format(u, x, PR[i]))
            f.close()
            # print(x)
            c = c + 1