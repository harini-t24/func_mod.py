n=int(input("Enter the number of elements:"))
items=[]
def get_items(n):
    for i in range(n):
        name=input("Enter Product Name:")
        quantity=int(input("Enter quantity:"))
        price=int(input("Enter price:"))
        items.append((name,quantity,price))
    return items
sub_tot=[]
def sub_total(items,n):
    for i in range(len(items)):
            sub=items[i][1]*items[i][2]
            sub_tot.append(sub)
    return sub_tot
r=get_items(n)
print(r)
S=sub_total(r,n)
print("sub_total:",S)
total=0
for i in range(0,len(S)):
    total=total+S[i]
print("Total:",total)
if total>3000:
    dis=total*10/100
else:
    dis=0
total=total-dis
print("Total(Discount)t:",total)
gst=total*5/100
print("Gst:",gst)
total=total+gst
print("Total with GST:",total)
