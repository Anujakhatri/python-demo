
#define a menu of restaurant
menu={
    'pizza':40,
    'pasta':50,
    'burger':60,
    'salad':70,
    'coffee':80,  
}
#Greet
print('Welcome to our restaurant')
print('pizza: Rs40\nPasta: Rs50\nburger:Rs60\nsalad: Rs70\ncoffe: Rs80\n')

order_total=0

item1= input("enter the name of item you want to order=")
if item1 in menu:
    order_total += menu[item1]
    print(f'your item {item1} has been added to your order')   

else:
    print(f"ordered item {item1} is not available yet")
    
another_order =input('Do you want another item to add?(Yes/No)')
if another_order == 'Yes':
    item2= input('Enter the name of second item=')
    
    if item2 in menu:
        order_total +=menu[item2]
        print= input(f'Your {item2} is successfully added')
    
    else:
        print(f"ordered item {item2} is not available yet")
 
print(f"The total amount of items is to pay {order_total} ")

 