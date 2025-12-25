#7-8. Deli:
print('\n**Creating out a list of sandwich')
sandwich_orders = ['cream','pear','mayonaise','butter','chocolate']
print(sandwich_orders)
finished_sandwiches = []
print('\n**writing a line individually using the while loop saying I "made your "___" sandwich')
while sandwich_orders:
    order = sandwich_orders.pop(0)
    print(f"I made your {order} sandwich")
    finished_sandwiches.append(order)
print("\nSandwiches made:", ' , '.join(finished_sandwiches))

#7-9. No pastrimi:
sandwich_orders = ['cream','pastrimi','pear','pastrimi','mayonaise','pastrimi','butter','chocolate']
finished_sandwiches = []
print('\n7-9. No pastrimi:')
print('\n**pastrimi is finished')
print('sorry, Deli has run out of Pastrimi')
#removing pastrimi from the list
while 'pastrimi' in sandwich_orders:
    sandwich_orders.remove('pastrimi')
while sandwich_orders:
    order = sandwich_orders.pop(0)
    print(f"I made your {order} sandwich")
    finished_sandwiches.append(order)
print("\nSandwiches made:", ' , '.join(finished_sandwiches))
