
import matplotlib.image as mpimg, matplotlib.pyplot as plt

def read(image):
    img = mpimg.imread(image)
    return img  
 
def gray1(image):#Method 1 - Averaging (aka “quick and dirty”)
    Red   = image[:,:,0]*(0.33)#multiplying the red   index with 1/3 for getting the index of gray
    Green = image[:,:,1]*(0.33)#multiplying the green index with 1/3 for getting the index of gray
    Blue  = image[:,:,2]*(0.33)#multiplying the blue  index with 1/3 for getting the index of gray
    Gray  = (Red+Green+Blue)#adding all index's to one index that is gray
    for i in range(3):
         image[:,:,i] = Gray#defining the indexes in the gray 
    return image

def gray2(image):
    #Method 2 - Type1 - Correcting for the human eye (sometimes called “luma” or “luminance”)
    Red   = image[:,:,0]*(0.3) #multiplying the red   index with 0.3  for getting the index of gray
    Green = image[:,:,1]*(0.59)#multiplying the green index with 0.59 for getting the index of gray
    Blue  = image[:,:,2]*(0.11)#multiplying the blue  index with 0.11 for getting the index of gray
    Gray  = (Red+Green+Blue)
    for i in range(3):
         image[:,:,i] = Gray#defining the indexes in the gray 
    return image

def gray3(image):
    #Method 2 - Type2 - Correcting for the human eye (sometimes called “luma” or “luminance”)
    Red   = image[:,:,0]*(0.299)#multiplying the red   index with 0.299 for getting the index of gray
    Green = image[:,:,1]*(0.587)#multiplying the green index with 0.587 for getting the index of gray
    Blue  = image[:,:,2]*(0.114)#multiplying the blue  index with 0.114 for getting the index of gray
    Gray  = (Red+Green+Blue)
    for i in range(3):
         image[:,:,i] = Gray#defining the indexes in the gray 
    return image

def gray4(image):
    #Method 2 - Type3 - Correcting for the human eye (sometimes called “luma” or “luminance”)
    Red   = image[:,:,0]*(0.2126)#multiplying the red   index with 0.2126 for getting the index of gray
    Green = image[:,:,1]*(0.7152)#multiplying the green index with 0.7152 for getting the index of gray
    Blue  = image[:,:,2]*(0.0722)#multiplying the blue  index with 0.0722 for getting the index of gray
    Gray  = (Red+Green+Blue)
    for i in range(3):
         image[:,:,i] = Gray#defining the indexes in the gray 
    return image

def plotRGB(RGB):
    plt.imshow(img2)#plotting the rgb image(original)
    plt.title('RGB')
    return plt.show()

def plotGray(Gray):
    plt.imshow(img)#plotting the gray image(changed)
    plt.title('Gray')
    return plt.show()

img ,img2= read("pp.png"),read("pp.png")
gray1(img)#Method 1 - Averaging (aka “quick and dirty”)
#gray2(img)#Method 2 - Type1 - Correcting for the human eye (sometimes called “luma” or “luminance,”
#gray3(img)#Method 2 - Type2 - Correcting for the human eye (sometimes called “luma” or “luminance,”
#gray4(img)#Method 2 - Type3 - Correcting for the human eye (sometimes called “luma” or “luminance,”
plotRGB(img2)
plotGray(img)