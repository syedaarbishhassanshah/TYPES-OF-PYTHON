def square_set(number):
    return{a*a for a in number}
set1={1,2,3,4,5}
squared_number=square_set(set1)
print(squared_number)