#!/usr/bin/python

#consolidates parts in eagle .bom file by value, device, and package
#will fail if there are not at least 4 fields per line
def consolidate_bom(fnamein,fnameout):

  refdes = []
  value = []
  device = []
  package = []

  fin = open(fnamein,'r')
  #First four lines aren't parts
  for i in range(5):
    line = fin.readline()
  while not line == '': #EOF
    els = line.split() #does not include white space by default
    value_inds = [i for i, x in enumerate(value) if x == els[1]]
    duplicate_part = False
    for i in value_inds:
      if device[i]==els[2] and package[i]==els[3]:
        duplicate_part = True
        break
    if duplicate_part: #part is already in list
      refdes[i].append(els[0])
    else: #part not in list yet
      refdes.append([els[0]])
      value.append(els[1])
      device.append(els[2])
      package.append(els[3])
    line = fin.readline()

  fout = open(fnameout,'w')
  for i in range(len(refdes)):
    for k in range(len(refdes[i])):
      if k > 0:
        fout.write(',')
      fout.write(refdes[i][k])
    fout.write(' ' + str(value[i]) + ' ' + str(device[i]) + ' ' + str(package[i]) + '\n')
  fout.close()

if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', action='store', dest='infile', help='Input file')
  parser.add_argument('-o', action='store', dest='outfile', help='Ouput file')
  args = parser.parse_args()
  consolidate_bom(args.infile,args.outfile)
