# AI_Project

(c) skip-thought model to be trained on UniM-Poem, for now we are using the pretrained model

Step 1: Download skipthoughts zip file

Step 2: Run following lines in terminal and save in the directory:

wget http://www.cs.toronto.edu/~rkiros/models/dictionary.txt
wget http://www.cs.toronto.edu/~rkiros/models/utable.npy
wget http://www.cs.toronto.edu/~rkiros/models/btable.npy
wget http://www.cs.toronto.edu/~rkiros/models/uni_skip.npz
wget http://www.cs.toronto.edu/~rkiros/models/uni_skip.npz.pkl
wget http://www.cs.toronto.edu/~rkiros/models/bi_skip.npz
wget http://www.cs.toronto.edu/~rkiros/models/bi_skip.npz.pkl

Step 3 : Add the PYTHONPATH of this repo/folder to your bashrc file.

Step 4 : (encoder takes in an Python list as an input)
run the file as python2.7 SkipThoughtModel.py
