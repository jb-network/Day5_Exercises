# # Course Total Python: Become an Advance Python Developer
# Day 5 Exercise 3

def duplicate_in_row(*args):

    for index_number, element in enumerate(args):
        if index_number != 0 and args[index_number-1] == element:
            return True
        else:
            continue
    return False


# TEST DATA
#Should be True
#number_list1 = duplicate_in_row(5,6,1,0,0,9,9,3)
#print(f"number list 1: {number_list1}")

#Should be False
#number_list2 = duplicate_in_row(6,0,5,1,0,3,0,1)
#print(f"number list 2: {number_list2}")
