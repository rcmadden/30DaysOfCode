# http://echorand.me/site/notes/articles/python_custom_class/article.html
'''
class Point:

    def __init__(self):
        #print('Self identifier:: ', id(self))

#if __name__ == '__main__':
    # create an instance of the class
#    p = Point()
#    print('Point object identifier {}'.format(id(p)))

#    p = Point()
#    print('Point object identifier', id(p))
'''

'''
class Point:

    def __init__(self, point):
        self.point = point
        #print('Self identifier:: ', id(self))
(
# returns the string representation of the point (str(self.point))
    def __str__(self):
        return 'Point: {0}'.format(str(self.point))

p1 = Point((1,2,3))
print(p1)

'''

class List:
    def __init__(self):
        list_id = id(self)
        title = "Todo"
        type = ('Todo', 'Shopping')
        members = ""
        items ="Add items to your list"
        print(list_id,title, type, members, items)

class Items:
    def __init__(self):
        item_id = id(self)
        status = ("Todo", "Done", "Asssigned", "Owner")


class Members:

    member_id = id(self)
    lists = # call list object
    items = "Get started"
    groups = "Self"
    privilages = "owner"

if __name__ == '__main__':
    DueToday = List()
    print(DueToday)


