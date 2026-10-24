import random 

#Task 1
def exact_probability(n, days=365):
    if n > days:
        return 1
        
    product = 1
    for i in range(n):
        product = product*(days-i)/days
        
    return 1 - product

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

#task4
print("----------------------------------------")
print(f"n\texact_probability\tsimulate")
print("----------------------------------------")
for n in [i * 10 for i in range(1, 6)]:
    print(f"{n}\t{exact_probability(n)}\t {simulate(n, 5000)}")
print("----------------------------------------")


#Task 5
n = 1

while True:
    minima  = exact_probability(n)
    if minima >= 0.5:
        print(f'The smallest n for exact_prob >= 0.5 is : {n}')
        break
    n += 1

#Task 5 For 100 days
m = 1
while True:
    minima  = exact_probability(m, days=100)
    if minima >= 0.5:
        print(f'The smallest n for exact_prob >= 0.5 and day = 100 is : {m}')
        break
    m += 1