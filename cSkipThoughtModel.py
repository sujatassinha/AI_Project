from __future__ import absolute_import 
from __future__ import division
from __future__ import print_function
import skipthoughts
import numpy as np
import json

#Dealing with the captions. For each image there are 5 captions.
with open('data/unim_poem.json','r') as f:
    captions = f.read().splitlines()
file_list=[]

captions_list=[]
for line in captions:
    file_list.append(line.split('#')[0])
    sentence = line.split('#')[1].split('\t')[1]
    captions_list.append(sentence)
#Load the SkipThoughts model and create an encoder
model = skipthoughts.load_model()
encoder = skipthoughts.Encoder(model)

#Pass the entire list into the encoder for encoding it
vectors = encoder.encode(captions_list)
np.save('data/unim_poem_sentence_skipthoughts.npy', vectors)
