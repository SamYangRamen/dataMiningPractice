rfp = open("population_in_Seoul_test.csv", "r", encoding="utf-8")
wfp = open("population_in_Seoul.txt", "w")

#d = rfp.read().replace(',', '')
d = rfp.read()

count = 0

for line in d.split('\n'):
    print(line)
    for word in line.split( ):
        if(count != 0):
            wfp.write(',')
        count += 1
        if(word.count(',')):
            wfp.write("\"" + word + "\"")
        else:
            wfp.write(word)
    wfp.write('\n')
    count = 0

rfp.close()
wfp.close()
