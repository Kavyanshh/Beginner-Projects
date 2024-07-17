import cv2
file_path=input("Enter the file path (with extension): ")
new_file_path=input("Enter the output path (with extension): ")

image=cv2.imread(f"C://Users//LENOVO//Pictures//{file_path}",cv2.IMREAD_UNCHANGED)


#Scales the height of the original image to the required height which is presented in the output 
scale_length=int(input("Enter the scale length: "))


#Calculation for the height and width
new_height= int(image.shape[0]*scale_length/100)
new_width= int(image.shape[1]*scale_length/100)


size=(new_width,new_height)

#Resizing the image
resized_image=cv2.resize(image,size)

#Saving the file
cv2.imwrite(f"C://Users//LENOVO//Pictures//{new_file_path}",resized_image)