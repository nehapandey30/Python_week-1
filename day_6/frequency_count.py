dict={
    "apple banana sev apple mirchi jackfruit "
}
d={}
for i in dict:
    for j in i.split():
        if j in d:
            d[j]+=1
        else:
            d[j]=1
print(d)