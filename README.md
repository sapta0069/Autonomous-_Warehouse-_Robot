# Autonomous-_Warehouse-_Robot
The warehouse belongs to an online retail company that sells products to a variety of customers. Inside this
warehouse, the products are stored in 12 different locations, labeled by the following letters from A to L:
The 12 locations are all connected to a computer system, which is ranking in real time the priorities of
product collection for these 12 locations. For example, at a specific time t, it will return the following
ranking :
| Priority Rank | Location |
| ------------- | -------- |
| 1             | G        |
| 2             | K        |
| 3             | L        |
| 4             | J        |
| 5             | A        |
| 6             | I        |
| 7             | H        |
| 8             | C        |
| 9             | B        |
| 10            | D        |
| 11            | F        |
| 12            | E        |

Our mission is to build an AI that will always take the shortest route to the top
priority location, whatever the location it starts from, and having the option to go by an intermediary
location which is in the top 3 priorities.

We have utilised the Q-learning model top solve this problem statement which one can infer by loking at the code

