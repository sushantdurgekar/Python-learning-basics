import random
import my_module

random_integer=random.randint(1,10)
print(random_integer)
print(my_module.my_fav_number)

random_0_to_1_float=random.random()
print(random_0_to_1_float)
print(random_0_to_1_float*10)

random_a_to_b_float=random.uniform(0,10)
print(random_a_to_b_float)

random_heads_or_tails=random.randint(0,1)
if random_heads_or_tails==0:
    print("Heads!!!")
else:
    print("Tails!!!")

if(random_0_to_1_float>=0.5):
    print("Heads!!!")
else:
    print("Tails!!!")
