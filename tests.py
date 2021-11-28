monday={"my home" : 'is here'}
tuesday={'is here' : 'all my life'}
wednesday = {}
thursday = {}
friday = {}
saturday = {}
sunday = {}

print(monday)
print(monday == '' or tuesday == '')

def test():
    global monday, tuesday, wednesday, thursday, friday, saturday, sunday
    if monday=='' or tuesday=='' or wednesday=='' or thursday=='' or friday=='' or saturday=='' or sunday=='':
        print('they are empty!')
    else:
        print('they are not empty!')

test()


def dict_add():
    global monday
    g = input('hello: ')
    h = input('world: ')
    monday[g] = h

    print(monday)

dict_add()