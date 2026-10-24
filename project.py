import random 
#Task 1
def exact_probability(n, days=365):
    if n > days:
        return 1
        
    product = 1
    for i in range(n):
        product = product*(days-i)/days
        
    return 1 - product
print(round(exact_probability(23),4))
print(exact_probability(1))
print(exact_probability(366))


#task2
def has_repeat(values):
    seen = []

    for value in values:
        if value not in seen:
            seen.append(value)
        else:
            return True

    return False

values = [3, 5, 7, 8]
print(has_repeat(values))





#task3
def simulate(n, trials, days=365):
    count=0 
    for i in range(trials):
        birthday=[random.randint(1,days) for i in range(n)]
        if has_repeat(birthday):
            count=count+1 
    return count/trials 



#Task 5 For 100 days
n = 1
while True:
    minima  = exact_probability(n, days=100)
    if minima >= 0.5:
        print(f'The smallest n for exact_prob >= 0.5 and day = 100 is : {n}')
        break
    n += 1