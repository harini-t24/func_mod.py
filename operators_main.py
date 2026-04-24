import operators_module
a=set()
b=set()
n1=int(input("Enter the number of elements of setA:"))
for i in range(n1):
    a.add(int(input()))
n2=int(input("Enter the number of elements of setB:"))
for i in range(n2):
    b.add(int(input()))
print("Set A:",a)
print("Set B:",b)
print("Union:",operators_module.union_set(a,b))
print("Intersection:",operators_module.intersection_set(a,b))
print("Difference:",operators_module.difference_set(a,b))
print("Symmetric:",operators_module.symmetric_set(a,b))
