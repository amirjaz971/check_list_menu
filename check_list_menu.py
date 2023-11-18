class Check:
    def __init__(self,lst):
        self.lst=lst

    def add(self,item):
        self.lst.append(item)
    def remove(self,item):
        self.lst.remove(item)

    def display(self):

        return f'list={self.lst}'



c1=Check([])


while True:
    print('1.add')
    print('2.remove')
    print('3.display')
    print('4.exit')
    choose=input('choose the option(1/2/3/4): ')

    if choose=='1':
        num=int(input('how many items do you want to add?: '))
        for i in range(num):
            item=input(f'enter the item {i+1}: ')
            c1.add(item)
        print('The items have been added to the list')
    elif choose=='2':
        if len(c1.lst)!=0:
            num=int(input('how many items do you want to remove from the list?: '))
            if num<=len(c1.lst):
               while num>0:
                
                
                
                   item=input('enter the item that you want to remove from the list: ')
                   if item in c1.lst:
                    
                       c1.remove(item)
                       num-=1
                   else:
                       print(f'there is no {item} in the list to remove from the list!')
                       
                       
               print('Items have been removed from the list')    
            else:
                print("The number of the items can't be more than the lenght of the list!")
        else:
            print('There is no items in the list to remove!')
    elif choose=='3':
        print(c1.display())
    elif choose=='4':
        print('Have a nice day')
        break
    else:
        print('wrong command!')
