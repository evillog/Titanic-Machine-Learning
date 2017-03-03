# coding=UTF-8
import csv
from math import log

"""
决策树
'PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked','Test'
"""


# 树
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 创建决策树
def create_tree():
    decision_tree = TreeNode('Sex')
    sex_left = TreeNode('Age')
    sex_right = TreeNode('Survived')
    male_left = TreeNode('Died')
    male_right = TreeNode('SibSp')
    sibsp_left = TreeNode('Died')
    sibsp_right = TreeNode('Survived')

    male_right.left = sibsp_left
    male_right.right = sibsp_right
    sex_left.left = male_left
    sex_left.right = male_right
    decision_tree.left = sex_left
    decision_tree.right = sex_right
    return decision_tree


# 判断性别是否为男
def is_male(sex):
    if sex == 1:
        return 1
    else:
        return 0


# 判断年龄是否大于等于9.5岁
def is_baby(age):
    if age >= 9.5:
        return 1
    else:
        return 0


# 判断Sibsp是否大于等于3
def is_sibsp(sibsp):
    if sibsp >= 3:
        return 1
    else:
        return 0


# def test():
#     decision_tree = create_tree()
#     is_survived(1, 0.5, decision_tree)


def is_survived(sex, age, sibsp, decision_tree):
    r = DFS_tree(decision_tree, 0, sex, age, sibsp)
    return r


def DFS_tree(node, deep, sex, age, sibsp):
    r = 0
    if node.val == 'Survived':
        r = 1
        return r
    elif node.val == 'Died':
        return r
    elif node.val == 'Sex':
        result = is_male(sex)
        if result:
            r =DFS_tree(node.left, (deep + 1), sex, age, sibsp)
        else:
            r =DFS_tree(node.right, (deep + 1), sex, age, sibsp)
    elif node.val == 'Age':
        result = is_baby(age)
        if result:
            r = DFS_tree(node.left, (deep + 1), sex, age, sibsp)
        else:
            r = DFS_tree(node.right, (deep + 1), sex, age, sibsp)
    elif node.val == 'SibSp':
        result = is_sibsp(sibsp)
        if result:
            r = DFS_tree(node.left, (deep + 1), sex, age, sibsp)
        else:
            r = DFS_tree(node.right, (deep + 1), sex, age, sibsp)

    return r


if __name__ == "__main__":
    decision_tree = create_tree()

    write_rows = []
    with open('C:/evillog/Machine_Learning/Titanic/test.csv', 'r') as testfile:
        reader = csv.DictReader(testfile)
        for row in reader:
            new_dict = {}
            sex = 0
            if row['Sex'] == 'male':
                sex = 1
            if row['Age'] == "":
                age = 200
            else:
                age = float(row['Age'])
            result = is_survived(sex, age, int(row['SibSp']), decision_tree)
            new_dict['PassengerId'] = row['PassengerId']
            new_dict['Survived'] = result

            write_rows.append(new_dict)

    with open('C:/evillog/Machine_Learning/Titanic/test_pre.csv', 'ab+') as writefile:
        headers = ['PassengerId', 'Survived']

        writer = csv.DictWriter(writefile, headers)

        writer.writeheader()
        writer.writerows(write_rows)

    testfile.close()
    writefile.close()
