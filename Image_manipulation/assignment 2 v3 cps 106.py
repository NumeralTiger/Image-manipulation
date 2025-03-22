from PIL import Image

# Open images
image = Image.open("IMG_6718.jpeg")  
img = Image.open("IMG_6719.jpeg")    

# Get pixel maps of the images
map1 = image.load()  
map2 = img.load()   

# Get image dimensions
w1, h1 = image.size

# Create a blank canvas with the same size as the images (or a desired size)
mars = Image.open("mars_1.jpg")  # Black background

def add_colors(colors):
    r_sum = g_sum = b_sum = 0
    for color in colors:
        r_sum += color[0]
        g_sum += color[1]
        b_sum += color[2]
    return (r_sum, g_sum, b_sum)

def multiply_color(color, factor):
    r, g, b = color
    return (int(r * factor), int(g * factor), int(b * factor))

map_mars = mars.load()
w, h = mars.size

def pasting():
    for x in range(w1):  
        for y in range(h1):  
            r1, g1, b1 = map1[x, y]
            r2, g2, b2 = map2[x, y]
            # Check if the color difference exceeds the threshold
            if abs(r2 - r1) > 30 or abs(g2 - g1) > 30 or abs(b2 - b1) > 30:
                # Update the canvas with the pixel from map1
                map_mars[x, y] = map1[x, y]

def blur(image):
    w, h = mars.size
    map = image.load()
    
    # Iterate over each pixel
    for x in range(w):
        for y in range(h):
            # Do not change the edges
            if x == 0 or x == w-1 or y == 0 or y == h-1:
                continue  # Skip edge pixels
            else:  # Blur a non-edge pixel
                surrounding_pixels = [map_mars[x, y], map_mars[x-1, y], map_mars[x+1, y], map_mars[x, y-1], map_mars[x, y+1]]
                summed_color = add_colors(surrounding_pixels)
                avgcolor = multiply_color(summed_color, 0.2)
                map_mars[x, y] = avgcolor
# Call the pasting function
pasting()
# Call the blur function
blur(mars)


# Print status and show the canvas
print("The canvas has been updated with the object.")
mars.show()