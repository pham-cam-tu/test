from pandas import DataFrame
from sklearn import linear_model

formulas = DataFrame([
    [0,0],
    [0,1],
    [0,2],
    [1,0],
    [1,1],
    [1,2],
    [2,0],
    [2,1],
    [2,2],
])

answer = DataFrame([0,1,2,1,2,3,2,3,4])

model = linear_model.LinearRegression()
model.fit(formulas,answer)

while True:
    print('> ', end='')
    x, y = list(map(lambda x: int(x), input().split(' ')))

    predected_answer = model.predict([x,y])
    print("{0}+{1}={2}".format(x,y,int(predected_answer[0][0])))