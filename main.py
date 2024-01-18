import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

unique_numbers = set(lst)

robot = [1,0]
human = [0,1]

numbers = []
for i in lst:
    if i == 'robot':
        numbers.append(robot)
    else:
        numbers.append(human)

edata = pd.DataFrame(data=numbers,columns=['robot','human']).to_string(index=False)
print(edata)

