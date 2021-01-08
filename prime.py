import plotly.express as px

elnum = int(input('Enter the number of elements:'))
print('Maximum value is ', 6*elnum+5)
x = [None]*elnum
y = [1]*elnum
z = [0]*elnum
cnt = 0
for i in range(elnum):
    x[i] = 6*i+5  # every number from Xn = 6*n + 5
    if y[i] and i+x[i] < elnum:
        for j in range(elnum):
            if i+(j+1)*x[i] < elnum:
                y[i+(j+1)*x[i]] = 0
    if y[i]:
        cnt = cnt + 1
        z[i] = cnt
    if (i % 1000) == 0:
        print(i)

# print(x)
# print(y)
x = [1, 3, 5]
y = [11, 12, 13]
a = [2, 4, 6]
b = [3, 24, 15]
print(x)
print(y)
print(x + a)
print(y + b)

fig = px.scatter(x=x+a, y=y+b)
print(fig)
fig.show()
