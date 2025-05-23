item=input("Enter the item name: ")
price=input("Enter the price of the item: ")
final = item.ljust(25-(len(price)),'.')+price
print(final)
