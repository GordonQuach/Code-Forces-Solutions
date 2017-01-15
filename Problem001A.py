### This solution is extremely inefficient... improvement coming soon.

import math

m = int(input())
n = int(input())
stone_Size = int(input())

# Creating variable for storage.
loop_Stone_Size = stone_Size

# Amt of stones for n.
n_Stone = 1
# Amt of stones for m.
m_Stone = 1
# You would start with one stone.
count_Stone = 1

if (loop_Stone_Size < m):
	m_Stone += 1
	count_Stone += 1
	loop_Stone_Size = loop_Stone_Size*count_Stone
else:
	print(str(n_Stone * m_Stone))

# Resets variables for next loop.
count_Stone = 1
loop_Stone_Size = stone_Size

if (loop_Stone_Size < n):
	n_Stone += 1
	count_Stone += 1
	loop_Stone_Size = loop_Stone_Size*count_Stone
else:
	print(str(n_Stone * m_Stone))

print(str(n_Stone*m_Stone))
