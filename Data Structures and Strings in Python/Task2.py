original_list =[]
for i in range(1,11):
    original_list.append(i)
print("Original list: ", original_list)
Extracted_list = original_list[:5]
print("Extracted first five elements: ", Extracted_list)
revered_list = Extracted_list[::-1]
print("Reversed extracted elements: ",revered_list)

