# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
su = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    line = line.strip()
    count = count+1
    start = line.find(':')
    su = su+float(line[start+1:])
print(su/count)


