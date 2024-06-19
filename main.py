grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] # This is a sample Python script.
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_2 = sorted({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
#print (students_2)
#print ('Aarons grades: ', grades [0])
a_0 = grades [0]
#print ('sum Aaron: ', sum (a_0))
b_0 = sum (a_0)
#print (len (grades[0]))
c_0 = len (grades [0])
d_0 = b_0/c_0
#print (d_0)

a_1 = grades [1]
#print ('sum Bilbo: ', sum (a_1))
b_1 = sum (a_1)
#print (len (grades[1]))
c_1 = len (grades [1])
d_1 = b_1/c_1
#print (d_1)

a_2 = grades [2]
#print ('sum Jonny: ', sum (a_2))
b_2 = sum (a_2)
#print (len (grades[2]))
c_2 = len (grades [2])
d_2 = (b_2/c_2)
#print (d_2)

a_3 = grades [3]
#print ('sum Khendrik: ', sum (a_3))
b_3 = sum (a_3)
#print (len (grades[3]))
c_3 = len (grades [3])
d_3 = (b_3/c_3)
#print (d_3)

a_4 = grades [4]
#print ('sum Steve: ', sum (a_4))
b_4 = sum (a_4)
#print (len (grades[4]))
c_4 = len (grades [4])
d_4 = (b_4/c_4)
#print (d_4)

students_grades = {'Aaron': d_0}
students_grades.update ({'Bilbo': d_1,
                          'Johnny': d_2,
                          'Khendrik': d_3,
                          'Steve': d_4})
print (students_grades)



# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
