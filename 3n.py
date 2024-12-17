import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Initialize the matrix for counting pairs of least significant digits
heatmap = np.zeros((10, 10), dtype=int)
values_loop_4 = []
values_loop_6 = []
values_loop_8 = []
num = int(input("Enter a number: "))
loop_count = 0

previous_lsd = None
previous_num = None

start_loop_num = num
# Loop to generate the sequence
while True: 
    
    loop_count += 1
    
    # Get the least significant digit (LSD)
    lsd = num % 10
    
    # Count pairs of LSDs
    if previous_lsd is not None:
        heatmap[previous_lsd][lsd] += 1
        
        # Check for specific pairs to annotate
        if (previous_lsd, lsd) == (2, 6):
            values_loop_4.append((start_loop_num, num))  # Could mark start of loop 4
            start_loop_num = previous_num

        elif (previous_lsd, lsd) == (6, 8):
            values_loop_6.append((start_loop_num, num))  # Exit of loop 6
            start_loop_num = previous_num

        elif (previous_lsd, lsd) == (8, 4):
            values_loop_8.append((start_loop_num, num))  # Exit of loop 8
            start_loop_num = previous_num

    if num ==1:
        print(f"{num} (LSD: {lsd})")
        break
    
    print(f"{num} (LSD: {lsd})")

    # Update previous LSD
    previous_lsd = lsd
    previous_num = num

    if (num % 2) == 0:
        num = int(num / 2)
    else:
        num = 3 * num + 1
    
    
    
print("Step count =", loop_count)


# Print annotated loop information with highlights
yellow_text = "\033[93m"  # Yellow text
reset_text = "\033[0m"     # Reset to default color

# Annotate specific pairs on the heatmap
for value in values_loop_4:
    print(f"Loop 4 (entrance value of (8) at (8=>4) : exit value of (6) at (2=>6) ({yellow_text}{value[0]}{reset_text}, {yellow_text}{value[1]}{reset_text}))")

for value in values_loop_6:
    print(f"Loop 6 enterance value of (2) at (2=>6) : exit value of (6) at (6=>8)) ({yellow_text}{value[0]}{reset_text}, {yellow_text}{value[1]}{reset_text}))")

for value in values_loop_8:
    print(f"Loop 8 enterance value of (6) at (6=>8) : exit value of (4) at (8=>4)) ({yellow_text}{value[0]}{reset_text}, {yellow_text}{value[1]}{reset_text}))")



# Display transitions in the desired format
print("Transitions:")
for i in range(10):
    for j in range(10):
        count = heatmap[i][j]
        if count > 0:
            print(f"({i}, {j}) => {count}")


# Generate the heatmap
plt.imshow(heatmap, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.xticks(ticks=np.arange(10), labels=np.arange(10))
plt.yticks(ticks=np.arange(10), labels=np.arange(10))
plt.title("Heatmap of LSD Pairs")
plt.xlabel("Current LSD")
plt.ylabel("Previous LSD")
plt.autoscale(True)

plt.show()



# Create a DataFrame to display values as a table
loop_counts = {
    'Start Loop 4': len(values_loop_4),
    'Start Loop 6': len(values_loop_6),
    'Start Loop 8': len(values_loop_8)
}

# Convert to DataFrame
df = pd.DataFrame.from_dict(loop_counts, orient='index', columns=['Count'])
print(df)