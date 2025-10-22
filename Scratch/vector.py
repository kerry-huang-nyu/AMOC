import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import matplotlib.colors as mcolors

# Define the grid
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)


#Romeo Loves Juliet as much as she loves him back 
# P = Y
# Q = X


#Beast loves Bell as much as she loves him, 
# but Belle has stockholm syndrome and loves beast only if he doesn't like her back
# P = Y
# Q = -X


#Romeo loves juliet but 
#Define the vector field F(x, y) = (P, Q)

#a is factor of cautiousness. they both try to control themselves 
#b is the factor of responsiveness. both of them are excited by eachother's advances
a = 0
b = 0
P = a*X + b*Y               # Example: rotation field
Q = b*X + a*Y








# # Plot the vector field
# plt.figure(figsize=(6,6))
# plt.quiver(X, Y, P, Q, color='blue')

# # Optional: make arrows have consistent length
# plt.quiver(X, Y, P, Q, color='blue', angles='xy', scale_units='xy', scale=1)

# plt.title(r"Vector Field $\vec{F}(x, y) = (-y, x)$")
# plt.xlabel('x')
# plt.ylabel('y')
# plt.axis('equal')
# plt.show()



# Streamplot with variable linewidth and colormap
fig, ax = plt.subplots(figsize=(6,6))
strm = ax.streamplot(
    X, Y, P, Q,
    color=np.sqrt(P**2 + Q**2),
    cmap='viridis',
    linewidth=2*np.sqrt(np.sqrt(P**2 + Q**2)),
    density=0.7
)



# === Single trajectory using streamplot seeds (no manual integration) ===
x0, y0 = 2, -1.99
seed = np.array([[x0, y0]])

# use the same scalar field you used for the background coloring
speed_field = np.hypot(P, Q)

# reuse the exact cmap from the existing streamplot so colors match
cmap = strm.lines.get_cmap()
norm = mcolors.Normalize(vmin=np.min(speed_field), vmax=np.max(speed_field))

# draw only the seeded streamline: set density tiny but > 0 to avoid auto seeds
strm_traj = ax.streamplot(
    X, Y, P, Q,
    start_points=seed,
    color=speed_field,            # colors vary along the path
    cmap=cmap, norm=norm,         # match the background map
    linewidth=2.0,
    arrowsize=1.1,
    integration_direction='both',   # or 'both'
    maxlength=8.0,                     # tune path length
    minlength=0.00,
    broken_streamlines=False
)

# optional: highlight the seed
ax.scatter(x0, y0, s=30, zorder=5, color=cmap(norm(speed_field[np.argmin(np.abs(y - y0)), np.argmin(np.abs(x - x0))])))



# Add transparency
strm.lines.set_alpha(0.2)

for patch in ax.patches:
    if isinstance(patch, FancyArrowPatch):
        patch.set_alpha(0.5)


# Labels and layout
ax.set_title(r"Streamplot of $\vec{F}(x, y) = (-y, x)$", fontsize=14)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.axis('equal')
plt.show()


# plt.figure(figsize=(7,7))
# speed = np.sqrt(P**2 + Q**2)
# strm = plt.streamplot(
#     X, Y, P, Q,
#     color=speed,
#     cmap='viridis',
#     density=0.7,
#     linewidth=1.2,
#     arrowsize=1.0
# )
# plt.title(r"Elegant Vector Field: $\vec{F}(x, y) = (-y, x)$", fontsize=14, pad=10)
# plt.axis('equal')
# plt.axis('off')  # removes axes for a clean aesthetic
# plt.tight_layout()
# plt.show()