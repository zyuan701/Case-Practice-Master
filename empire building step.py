import numpy as np
import matplotlib as plt

# Initialize all_walks
all_walks = []

# Simulate random walk 500 times
for i in range(500) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness in which case I was too clumsy to fall down of the building
        # This is a second independent random variable
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)
#convert all_walks to Numpy arrays
#transpose the column to rows
np_aw_t = np.transpose(np.array(all_walks))

#select last row from np_aw_t as ends
ends = np_aw_t[-1]

#plot histogram
plt.hist(ends)
plt.show()

#show the chances of reaching 60 steps or higher
print(np.mean(ends>=60))