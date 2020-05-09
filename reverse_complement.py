#!/usr/bin/env python
# coding: utf-8

# In[6]:


# import sys

#Generate reverse complement by replacing all A>1, C>2, G>3, T>4. then replace back with 1>T, 2>G, 3>C, 4>A.
def reverse(seq):
    """Returns a reversed string"""
    return seq[::-1]


def complement(seq):
    """Returns a complement DNA sequence"""
    complement_dict = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    seq_list = list(seq)
    
    try:
        seq_list = [complement_dict[base] for base in seq_list]
    except:
        return "Invalid Sequence"
    # second complicated lambda
    # seq_list = list(map(lambda base: complement_dict[base], seq_list))
    # third easy for loop
    # for i in range(len(seq_list)):
    #    seq_list[i] = complement_dict[seq_list[i]]
    return ''.join(seq_list)


def reverse_complement(seq):
    """"Returns a reverse complement DNA sequence"""
    seq = reverse(seq)
    seq = complement(seq)
    return seq

if __name__ == '__reverse_complement__':
    # test1.py executed as script
    # do something
#     reverse_complement(sys.seq[1])
    reverse_complement(seq)


# In[ ]:




