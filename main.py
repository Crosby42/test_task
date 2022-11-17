import collections

dict = {}
symb_count = 0

f = open('test.txt', 'r')
for symb in f.read():
    if symb.isalpha():
        symb_count += 1
        if (symb.lower() not in dict):
            dict[symb.lower()] = 1
        else:
            dict[symb.lower()] += 1
f.close()

ordered_dict = collections.OrderedDict(sorted(dict.items()))

for symb in ordered_dict:
    print('%(1)s: %(2)s' % {'1': symb, '2': "{:.{}f}".format(ordered_dict[symb]/symb_count*100,3)},'%',sep='')

