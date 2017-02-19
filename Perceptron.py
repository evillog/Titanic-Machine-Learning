# coding=UTF-8
import csv

"""
感知机
'PassengerId', 'Survived', 'Pclass’‘Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked','Test'
"""


# 符号
def sign(v):
    if v > 0:
        return 1
    else:
        return -1


# 训练
def training(train_datas):
    weight = [0, 0]  # 权值
    bias = 0  # 偏置
    learning_rate = 0.05  # 学习率

    for each in train_datas:
        x1, x2, y = each
        result = sign(weight[0]*x1 + weight[1]*x2 + bias)
        if result*y < 0:
            weight[0], weight[1], bias = weight_result(weight[0], weight[1], x1, x2, y, learning_rate, bias)

    print("stop training: "),
    print(weight[0], weight[1], bias)

    return weight, bias


def weight_result(w1, w2, x1, x2, y, n, b):
    w1 = w1 + n*x1*y
    w2 = w2 + n*x2*y
    b = b + n*y
    print("update weight and bias: "),
    print(w1, w2, b)
    return w1, w2, b


# 测试
def test(sex, pclass):
    prediction = sign(weight[0]*sex + weight[1]*pclass + bias)
    if prediction == -1:
        prediction = 0
    return prediction


if __name__ == "__main__":
    train_datas = []
    with open('C:/evillog/Machine_Learning/Titanic/train.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)

    #     sex = [row['Sex'] for row in reader]
        for row in reader:
            train_data = []
            # train data
            train_data.append(1) if row['Sex'] == 'male' else train_data.append(0)
            train_data.append(float(row['Pclass']))
            if row['Survived'] == '1':
                train_data.append(1)
                train_datas.append(train_data)
            else:
                train_data.append(-1)
                train_datas.append(train_data)

        print train_datas
        weight, bias = training(train_datas)

    write_rows = []
    with open('C:/evillog/Machine_Learning/Titanic/test.csv', 'r') as testfile:
        reader = csv.DictReader(testfile)
        for row in reader:
            new_dict = {}
            sex = 0
            if row['Sex'] == 'male':
                sex = 1
            is_survived = test(sex, float(row['Pclass']))
            new_dict['PassengerId'] = row['PassengerId']
            new_dict['Survived'] = is_survived

            write_rows.append(new_dict)

    with open('C:/evillog/Machine_Learning/Titanic/test_pre.csv', 'ab+') as writefile:
        headers = ['PassengerId', 'Survived']

        writer = csv.DictWriter(writefile, headers)

        writer.writeheader()
        writer.writerows(write_rows)

    csvfile.close()
    testfile.close()
    writefile.close()
