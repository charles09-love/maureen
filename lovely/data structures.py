#list

employees = ['John','Smith','Andrew','Jane']
print(employees[1:3] )
employees[3] = 'Reuben'
print(employees)
employees.append('stephen')
print(employees)
employees.remove('stephen')
print(employees)
employees.insert(2,'Juliana')
print(employees)
employees.extend(['paul','Erick','Allan'])
print(employees)
print(employees)
# tuple
products =('apple','banana','orange','cherry' )
print(products)
print(products[2])
print(products[0:2])
# products[0] = 'mango'
print(products)
print(products)
#set
students = {'peter','Esther','Ann','Oduor'}
students.add('Dennis')
print(students)
students.update(['Kimani'])
print(students)
students.remove('Ann')
print(students)
# #dictionary
book = {
    'title':'Python Programming',
    'author':'charles',
    'publisher':'The University of Chicago'
    }
print(book)
book[' year published'] = 1919
print(book)
print(book['author'])
print(book['title'])

if 'author' in book:
    print('author is in the book')
else:
    print('author is not present')

book = {
     'title':'Haris Kingdom',
     'author':'charles',
     'publisher':'The University of Chicago'
}
print(book)
book[' year published'] = 2000
print(book)
print(book['author'])
print(book['title'])
#
if 'title' in book:
     print('title is in the book')
else:
     print('title is not present')



