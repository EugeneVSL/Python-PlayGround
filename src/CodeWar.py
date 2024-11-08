def find_even_index(arr):

    index = 0
    found_index = 0

    while True:

        if index == 0:
            first_sum = 0 
        else:
            first_sum = sum(arr[:index])

        second_sum = sum(arr[index + 1:])

        if first_sum == second_sum:
            found_index = index 
            break
        else:
            index += 1

            if index == len(arr):
                found_index = -1
                break

    return found_index

my_list = [0,0,0,0,0]
print(find_even_index(my_list))



# test.assert_equals(find_even_index([1,2,3,4,3,2,1]),3)
# test.assert_equals(find_even_index([1,100,50,-51,1,1]),1)
# test.assert_equals(find_even_index([1,2,3,4,5,6]),-1)
# test.assert_equals(find_even_index([20,10,30,10,10,15,35]),3)
# test.assert_equals(find_even_index([20,10,-80,10,10,15,35]),0)
# test.assert_equals(find_even_index([10,-80,10,10,15,35,20]),6)
# test.assert_equals(find_even_index(list(range(1,100))),-1)

# test.assert_equals(find_even_index([0,0,0,0,0]),0,"Should pick the first index if more cases are valid")
# test.assert_equals(find_even_index([-1,-2,-3,-4,-3,-2,-1]),3)
# test.assert_equals(find_even_index(list(range(-100,-1))),-1)
# test.assert_equals(find_even_index([8,8]),-1)
# test.assert_equals(find_even_index([8,0]),0)
# test.assert_equals(find_even_index([0,8]),1)
# test.assert_equals(find_even_index([7,3,-3]),0)
# test.assert_equals(find_even_index([8]),0)
# test.assert_equals(find_even_index([10,-10]),-1)
# test.assert_equals(find_even_index([-3,2,1,0]),3)
# test.assert_equals(find_even_index([-15,5,11,17,19,-17,20,-6,17,-17,19,16,-15,-6,20,17]),8)
