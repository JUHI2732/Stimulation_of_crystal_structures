import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Take the lattice parameter as input from the user
a = float(input("Enter the lattice parameter: "))

# Take the crystal structure as input from the user
crystal_structure = input("Enter the crystal structure (bcc/fcc/hcp): ")

if crystal_structure == 'bcc':
    x = [0, 0, a, a, 0, 0, a, a, a/2]
    y = [0, a, 0, a, 0, a, 0, a, a/2]
    z = [0, 0, 0, 0, a, a, a, a, a/2]
elif crystal_structure == 'fcc':
    x = [0, 0, a, a, a/2, a/2, 0, 0, a, a, a/2, a/2]
    y = [0, a, 0, a, 0, a, a/2, a/2, a/2, a/2, 0, a]
    z = [0, 0, 0, 0, a/2, a/2, 0, a, a/2, a/2, a, a]
elif crystal_structure == 'hcp':
    x = [0, a, a/2, a/2, 0, a, a/2, a/2]
    y = [0, 0, np.sqrt(3)*a/2, np.sqrt(3)*a/2, 0, 0, np.sqrt(3)*a/2, np.sqrt(3)*a/2]
    z = [0, 0, 0, 0, a*np.sqrt(2/3), a*np.sqrt(2/3), a*np.sqrt(2/3), a*np.sqrt(2/3)]
else:
    print("Invalid crystal structure. Please enter bcc, fcc, or hcp.")
    exit()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.scatter(x, y, z)

# Plot the lines connecting the points
for i in range(len(x)):
    for j in range(i+1, len(x)):
        ax.plot([x[i], x[j]], [y[i], y[j]], [z[i], z[j]], color='b')

# Set the limits of the plot
ax.set_xlim([0, a])
ax.set_ylim([0, a])
ax.set_zlim([0, a])

# Set the labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
