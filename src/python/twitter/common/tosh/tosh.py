import sqlparse

print("Hello")
def hello():
    print("Hello")

hello()
print sqlparse.split('select * from foo; select * from bar;')

