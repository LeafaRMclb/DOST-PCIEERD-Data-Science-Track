import re
##with open("regex_sum_42.txt") as txtfile:
    #matches = re.findall("[0-9]+", txtfile.read())
    #print(sum(int(i) for i in matches))
#txtfile.close()


with open("regex_sum_83240.txt") as txtfile:
    #matches = re.findall("[0-9]+", txtfile.read())
    print(sum([int(i) for i in re.findall("[0-9]+", txtfile.read())]))
txtfile.close()



    #print(sum([numbers for ]))

    
#X = "Why should you learn to write programs? 7746 12 1929 8827 Writing programs (or programming) is a very creative 7 and rewarding activity.\
 #You can write programs for many reasons, ranging from making your living to solving 8837 a difficult data analysis problem to having fun\
  #to helping 128 someone else solve a problem. This book assumes that everyone needs to know how to program ..."
#matches = re.findall("[0-9]+",X)
#to_int = []
##for i in matches:
    #i = int(i)
    #to_int.append(i)
#rint(sum(to_int))

        
    #print(matches)
    #print(sum([number for numbers in re.findall("[0-9]+", reader)]))
    