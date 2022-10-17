#This image prints alternating blue and green lines, contingent on an even amount of lines the user inputs.

import numpy as np #This helps create the array
import matplotlib.pyplot as plt #This helps create a graph we can manipulate

lines_image_size = int(input("Enter the size: "))
file_output_name = input("Enter the output file name: ")

line_pic = np.zeros((lines_image_size, lines_image_size, 3)) #This defines the size of the image

#These set the column, row, and color values for the lines. Each green stripe must start when each blue stripe ends
line_pic[:, :, 0] = 0 #Defines red
line_pic[:,:,2] = 1 #Defines Blue
line_pic[:,1::2, 1] = 1 #Defines Green, starting from one step and moving to two before stopping
line_pic[:,1::2,2] = 0 #Blue set to 0

plt.imshow(line_pic)
plt.show()
plt.imsave(file_output_name,line_pic)