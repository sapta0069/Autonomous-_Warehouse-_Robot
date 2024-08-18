# Artificial Intelligence for Business
# Optimizing Warehouse Flows with Q-Learning
# Importing the libraries
import numpy as np
# Setting the parameters gamma and alpha for the Q-Learning
gamma = 0.75
alpha = 0.9

# PART 1 - DEFINING THE ENVIRONMENT
# Defining the states
location_to_state = { 'A': 0,'B': 1,'C': 2,'D': 3,'E': 4,'F': 5,'G': 6,'H': 7,'I': 8,'J': 9,'K': 10,'L': 11}

# Defining the actions
actions = [0,1,2,3,4,5,6,7,8,9,10,11]

# Defining the rewards
R = np.array([
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1000, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
])

# PART 2 - BUILDING THE AI SOLUTION WITH Q-LEARNING
# Initializing the Q-Values
Q = np.array(np.zeros([12,12]))

# Implementing the Q-Learning process with debugging information
for i in range(1000):  # Increased number of iterations
    current_state = np.random.randint(0, 12)  # Randomly select the current state
    playable_actions = []
    for j in range(12):
        if R[current_state,j]>0:
          playable_actions.append(j)

    # Choose next state randomly from playable actions
    next_state = np.random.choice(playable_actions)

    # Calculate Temporal Difference (TD)
    TD = R[current_state, next_state] + gamma *Q[next_state, np.argmax(Q[next_state,])] - Q[current_state, next_state]
    
    # Update the Q-value
    Q[current_state, next_state] =  alpha * TD + Q[current_state, next_state]

print("Q-Values:")
print(Q.astype(int))