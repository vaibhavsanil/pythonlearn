#e the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
add1 = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1 
    #line = line.rstrip()
    atpos = line.find('0')
    addvar = float(line[atpos:])
    add1 = add1 + addvar
    
     
avg = add1/count
avg = float(avg)

    
print "Average spam confidence : %12f " %avg

