from statistics import mean
c1 = [1, 2, 100, 3, 4]
c2 = [1,4,4,4,5,6,9]

# maths
def centeredavg(list):
    print(list)
    return (sum(list) - min(list) - max(list)) / (len(list) -2)
    

def centeredavg2(list2):
    list2.sort()
    return mean(list2[1:-1])
    


print(centeredavg2(c1))