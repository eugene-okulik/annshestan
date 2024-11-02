
my_dict = {'tuple': (1, True, 6, 'Text'), 'list': [3, 'list', 5], 'dict': {'1': 'one', '2': 'two'}, 'set': {1, 3, 5}}
ttuple = my_dict['tuple']
print(ttuple[-1])
llist = my_dict['list']
llist.append('hehe')
llist.pop(1)
print(llist)
ddict = my_dict['dict']
ddict[('i am tuple',)] = 'three'
ddict.pop('1')
print(ddict)
sset = my_dict['set']
sset.add('not hehe')
sset.pop()
print(sset)
print(my_dict)
