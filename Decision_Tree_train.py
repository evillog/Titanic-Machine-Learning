# coding=UTF-8
import csv
from math import log

"""
决策树---计算选择特征
'PassengerId', 'Survived', 'Pclass Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked','Test'
"""


# 人
class PersonInfo(object):
    def __init__(self):
        self.sex = 0  # Sex: male--1 female--0
        self.age = 200
        self.survive = 0  # Survived: alive--1 dead--0


# 计算经验熵
def entropy_process(data_list):
    num = 0
    for each in data_list:
        num += each

    entropy = 0
    for each in data_list:
        if each == 0:
            entropy -= 0
        else:
            prob = float(each) / num
            entropy -= prob * log(prob, 2)
    return entropy


# 计算信息增益
def info_gain(data_list, data_sum, entropy):
    sum_num = data_sum
    gain = 0
    for each in data_list:
        current_entropy = entropy_process(each)
        num = 0
        for x in each:
            num += x
        gain += float(num) / sum_num * current_entropy
    return entropy-gain


# 训练
def training(train_datas):
    # 总数统计
    alive_account, dead_account = 0, 0  # 用于计算总的经验熵
    male_alive, male_dead, female_alive, female_dead = 0, 0, 0, 0       # 用于计算信息增益
    baby_alive, baby_dead, older_alive, older_dead, other_alive, other_dead = 0, 0, 0, 0, 0, 0   # 用于计算信息增益
    for each_person in train_data:
        if each_person.survive == 0:
            dead_account += 1
            # Sex
            if each_person.sex == 0:
                male_dead += 1
            else:
                female_dead += 1
            # Age
            if each_person.age <= 1:
                baby_dead += 1
            elif each_person.age > 40:
                older_dead += 1
            else:
                other_dead += 1
        else:
            alive_account += 1
            # Sex
            if each_person.sex == 0:
                male_alive += 1
            else:
                female_alive += 1
            # Age
            if each_person.age <= 1:
                baby_alive += 1
            elif each_person.age > 40:
                older_alive += 1
            else:
                other_alive += 1

    # 计算总的经验熵
    entropy_list = [dead_account, alive_account]
    print "死：活", entropy_list
    entropy = entropy_process(entropy_list)
    print entropy

    # 计算两个属性的信息增益
    # 性别
    sex_list = [[male_alive, male_dead], [female_alive, female_dead]]
    sex_gain = info_gain(sex_list, len(train_data), entropy)
    print "性别的信息增益：", sex_gain

    # 年龄
    age_list = [[baby_alive, baby_dead], [older_alive, older_dead], [other_alive, other_dead]]
    print age_list
    age_gain = info_gain(age_list, len(train_data), entropy)
    print "年龄的信息增益：", age_gain


if __name__ == "__main__":
    with open('C:/evillog/Machine_Learning/Titanic/train.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        # 确认参与训练的属性
        feature_name = ['Sex', 'Age']
        train_data = []  # [PersonInfo]

        # 添加训练数据
        for row in reader:
            new_person = PersonInfo()
            # Sex: male--1 female - 0
            if row['Sex'] == 'male':
                new_person.sex = 1
            if row['Age'] != "":
                new_person.age = float(row['Age'])
            if row['Survived'] == '1':
                new_person.survive = 1
            train_data.append(new_person)

        # 传输数据以生成决策树
        training(train_data)

    csvfile.close()
