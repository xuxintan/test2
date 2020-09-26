def merge_Sort(List): #define the merge sort function
    if len(List)<=1:
        return List 
    half = len(List)//2
    left=merge_Sort(List[:half])
    right=merge_Sort(List[half:])
    return reduce(left,right)

def reduce(left,right): #define the reduce function to merge two sorted lists into one list
    result=[]
    left_index=0
    right_index=0
    while True:
        if left[left_index]<right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index+= 1
        if left_index ==len(left):
            result.extend(right[right_index:])
            break
        if right_index== len(right):
            result.extend(left[left_index:])
            break
    return result