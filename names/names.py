import time

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if self.left is not None:
            if self.value > target:
                if self.left == target:
                    return True
                else:  
                    return self.left.contains(target)
        if self.right is not None:
            if self.value < target:
                if self.right == target:
                    return True
                else:  
                    return self.right.contains(target)
        else:
            return False

        # if target is self.value:
        #     return True
        # else:
        #     if target < self.value:
        #         if not self.left:
        #             return False
        #         else:
        #             return self.left.contains(target)
        #     else:
        #         if not self.right:
        #             return False
        #         else:
        #             return self.right.contains(target)
            

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)



start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


bst = BSTNode('name_dups') # create a new binary search tree 

for name_1 in names_1:  # iterate through the first list of name
    bst.insert(name_1) # insert names into newly created tree
for name_2 in names_2: # iterate throught the second list of names
    if bst.contains(name_2) == True: # if name equals name is first list
        duplicates.append(name_2) # append it to the list

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


# First Run:

# 64 duplicates:

# Hallie Vazquez, Peyton Lloyd, Daphne Hamilton, Jaden Hawkins, Dulce Hines, Piper Hamilton, Marisol Morris, Josie Dawson, Giancarlo Warren, Amiah Hobbs, Jaydin Sawyer, Franklin Cooper, Diego Chaney, Carley Gallegos, Ahmad Watts, Malcolm Nelson, Malcolm Tucker, Grace Bridges, Luciana Ford, Davion Arias, Pablo Berg, Jadyn Mays, Marley Rivers, Abel Newman, Sanai Harrison, Cloe Norris, Clay Wilkinson, Salma Meza, Addison Clarke, Nelson Acevedo, Devyn Aguirre, Winston Austin, Carsen Tyler, Hayley Morgan, Aleah Valentine, Camryn Doyle, Josie Cole, Nathalie Little, Leia Foley, Jordin Schneider, Justine Soto, Lennon Hunt, Zara Suarez, Kale Sawyer, William Maldonado, Irvin Krause, Maliyah Serrano, Selah Hansen, Kameron Osborne, Alvaro Robbins, Leon Cochran, Andre Carrillo, Dashawn Green, Eden Howe, Logan Morrow, Ralph Roth, Trace Gates, Megan Porter, Aydan Calderon, Raven Christensen, Ashlee Randall, Victoria Roach, River Johnson, Ali Collier


# runtime: 4.272704601287842 seconds



# Second Run: (no code changes)

# 64 duplicates:

# Hallie Vazquez, Peyton Lloyd, Daphne Hamilton, Jaden Hawkins, Dulce Hines, Piper Hamilton, Marisol Morris, Josie Dawson, Giancarlo Warren, Amiah Hobbs, Jaydin Sawyer, Franklin Cooper, Diego Chaney, Carley Gallegos, Ahmad Watts, Malcolm Nelson, Malcolm Tucker, Grace Bridges, Luciana Ford, Davion Arias, Pablo Berg, Jadyn Mays, Marley Rivers, Abel Newman, Sanai Harrison, Cloe Norris, Clay Wilkinson, Salma Meza, Addison Clarke, Nelson Acevedo, Devyn Aguirre, Winston Austin, Carsen Tyler, Hayley Morgan, Aleah Valentine, Camryn Doyle, Josie Cole, Nathalie Little, Leia Foley, Jordin Schneider, Justine Soto, Lennon Hunt, Zara Suarez, Kale Sawyer, William Maldonado, Irvin Krause, Maliyah Serrano, Selah Hansen, Kameron Osborne, Alvaro Robbins, Leon Cochran, Andre Carrillo, Dashawn Green, Eden Howe, Logan Morrow, Ralph Roth, Trace Gates, Megan Porter, Aydan Calderon, Raven Christensen, Ashlee Randall, Victoria Roach, River Johnson, Ali Collier


# runtime: 4.8471386432647705 seconds

#BST code run:

# 64 duplicates:

# Ahmad Watts, Franklin Cooper, Jaydin Sawyer, Sanai Harrison, Jaden Hawkins, Cloe Norris, Pablo Berg, Giancarlo Warren, Camryn Doyle, Aleah Valentine, Grace Bridges, Daphne Hamilton, Irvin Krause, Justine Soto, Josie Cole, Winston Austin, Ashlee Randall, Leon Cochran, Kale Sawyer, Alvaro Robbins, Malcolm Tucker, Jadyn Mays, Josie Dawson, Clay Wilkinson, Logan Morrow, Salma Meza, Trace Gates, Hayley Morgan, Dulce Hines, Abel Newman, Nathalie Little, Zara Suarez, Leia Foley, William Maldonado, Marley Rivers, Addison Clarke, Kameron Osborne, Aydan Calderon, Ali Collier, Marisol Morris, Peyton Lloyd, Eden Howe, Victoria Roach, Dashawn Green, Carley Gallegos, Selah Hansen, Hallie Vazquez, Piper Hamilton, Lennon Hunt, Andre Carrillo, Devyn Aguirre, River Johnson, Maliyah Serrano, Diego Chaney, Davion Arias, Nelson 
# Acevedo, Malcolm Nelson, Raven Christensen, Luciana Ford, Amiah Hobbs, Megan Porter, Carsen Tyler, Jordin Schneider, 
# Ralph Roth


# runtime: 0.08296680450439453 seconds


#BST code run 2:

# 64 duplicates:

# Ahmad Watts, Franklin Cooper, Jaydin Sawyer, Sanai Harrison, Jaden Hawkins, Cloe Norris, Pablo Berg, Giancarlo Warren, Camryn Doyle, Aleah Valentine, Grace Bridges, Daphne Hamilton, Irvin Krause, Justine Soto, Josie Cole, Winston Austin, Ashlee Randall, Leon Cochran, Kale Sawyer, Alvaro Robbins, Malcolm Tucker, Jadyn Mays, Josie Dawson, Clay Wilkinson, Logan Morrow, Salma Meza, Trace Gates, Hayley Morgan, Dulce Hines, Abel Newman, Nathalie Little, Zara Suarez, Leia Foley, William Maldonado, Marley Rivers, Addison Clarke, Kameron Osborne, Aydan Calderon, Ali Collier, Marisol Morris, Peyton Lloyd, Eden Howe, Victoria Roach, Dashawn Green, Carley Gallegos, Selah Hansen, Hallie Vazquez, Piper Hamilton, Lennon Hunt, Andre Carrillo, Devyn Aguirre, River Johnson, Maliyah Serrano, Diego Chaney, Davion Arias, Nelson 
# Acevedo, Malcolm Nelson, Raven Christensen, Luciana Ford, Amiah Hobbs, Megan Porter, Carsen Tyler, Jordin Schneider, 
# Ralph Roth


# runtime: 0.08003449440002441 seconds
