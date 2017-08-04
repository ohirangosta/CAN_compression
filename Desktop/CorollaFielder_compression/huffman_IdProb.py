# -*- coding:cp932 -*-

filename = r'CorollaFielder_freq.txt'

freq = dict()
for line in open(filename, 'rb'):
  l1l2 = line[:-1].split(' ')
  freq.setdefault(l1l2[0], 0)
  freq[l1l2[0]] = int(l1l2[1]);
  print l1l2

wtree = [i for i in freq.iteritems()]
print "-----------------------------------"
while len(wtree) > 1:

  wtree.sort(lambda a,b: cmp(b[1], a[1]))
  b2, b1 = (wtree.pop(), wtree.pop())
  wtree.append(((b1[0], b2[0]), b1[1] + b2[1]))
  
  print b2, b1
print "-----------------------------------"
tree = wtree[0][0]
print "frequency tree:"
print tree
orig_bits = wtree[0][1] * 11
print orig_bits

def collapse_tree(t, leaf, prefix):
  if type(leaf) == tuple:
    c = 0
    for i in leaf:
      collapse_tree(t, i, prefix + (c,))
      c += 1
  else:
    t.append((leaf, prefix))

e_table = []
collapse_tree(e_table, tree, ())


compressed_bits = 0
print "encoding table:"
for i in e_table:
  print freq[i[0]], "".join([str(j) for j in i[1]]), (i[0], freq[i[0]])
  compressed_bits += freq[i[0]] * len(i[1])

print "data can be compressed from %d bits into %d bits (%f%%)" % \
  (orig_bits, compressed_bits, float(compressed_bits) / orig_bits * 100)