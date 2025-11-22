# guest_list
guest_list=['Mbappe' , 'Vinicius' , 'Bellingham' , 'Rodrygo']
print(guest_list)
print("     writing to each person in the list to invite them")
print(guest_list[0], "I am inviting you for dinner")
print(guest_list[1], "I am inviting you for dinner")
print(guest_list[2], "I am inviting you for dinner")
print(guest_list[3], "I am inviting you for dinner")

#changing guest_list
print(guest_list[3]," can't make it for dinner")
guest_list[3]='Arda guller'
print("     writing again to each person in the list to invite them since the list has been modified")
print(guest_list[0], "I am inviting you for dinner")
print(guest_list[1], "I am inviting you for dinner")
print(guest_list[2], "I am inviting you for dinner")
print(guest_list[3], "I am inviting you for dinner")

#more guest
print("good news boys we found a bigger table ")
print("     inviting 3 more persons since a bigger table has been found and writing seperately to everyone to invite them")
guest_list.insert(0,'Coutois')
guest_list.insert(2,'Valverde')
guest_list.append('Trent')
print(guest_list[0], "I am inviting you for dinner")
print(guest_list[1], "I am inviting you for dinner")
print(guest_list[2], "I am inviting you for dinner")
print(guest_list[3], "I am inviting you for dinner")
print(guest_list[4], "I am inviting you for dinner")
print(guest_list[5], "I am inviting you for dinner")
print(guest_list[6], "I am inviting you for dinner")
