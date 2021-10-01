# 使用年龄、票价、性别三个特征
import csv
import pandas as pd

mean_age = 0
mean_fare = 0
# 数据清洗
def data_clean(input_file, out_file):
    data_frame = pd.read_csv(input_file)
    data_frame['Age'] = data_frame['Age'].fillna(data_frame['Age'].mean())
    data_frame.to_csv(out_file, index=False)

# 计算需要的概率
def compute_probability(input_file):
    global mean_age, mean_fare
    number_of_unSurvived = 0
    number_of_female_unSurvived = 0
    number_of_old_unSurvived = 0
    number_of_rich_unSurvived = 0
    number_of_female_Survived = 0
    number_of_old_Survived = 0
    number_of_rich_Survived = 0
    count = 0
    data_frame = pd.read_csv(input_file)
    mean_age = data_frame['Age'].mean()
    mean_fare = data_frame['Fare'].mean()
    with open(r'D:\post_graduate_class\pattern_recognition\train_data_clean.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            count += 1
            if row['Survived'] == str(0):
                number_of_unSurvived += 1
                if row['Sex'] == 'female':
                    number_of_female_unSurvived += 1
                if float(row['Age']) > mean_age:
                    number_of_old_unSurvived += 1
                if float(row['Fare']) > mean_fare:
                    number_of_rich_unSurvived += 1
            elif row['Survived'] == str(1):
                if row['Sex'] == 'female':
                    number_of_female_Survived += 1
                if float(row['Age']) > mean_age:
                    number_of_old_Survived += 1
                if float(row['Fare']) > mean_fare:
                    number_of_rich_Survived += 1
    problity_of_unSurvived = number_of_unSurvived / count
    problity_of_female_unSurvived = number_of_female_unSurvived / number_of_unSurvived
    problity_of_old_unSurvived = number_of_old_unSurvived / number_of_unSurvived
    problity_of_rich_unSurvived = number_of_rich_unSurvived / number_of_unSurvived
    number_of_Survived = count - number_of_unSurvived
    problity_of_female_Survived = number_of_female_Survived / number_of_Survived
    problity_of_old_Survived = number_of_old_Survived / number_of_unSurvived
    problity_of_rich_Survived = number_of_rich_Survived / number_of_Survived
    return problity_of_unSurvived, problity_of_female_unSurvived, problity_of_old_unSurvived,problity_of_rich_unSurvived,\
           problity_of_female_Survived,problity_of_old_Survived,problity_of_rich_Survived

# 对测试集数据进行预测
def predict(age, sex, fare, problity_of_unSurvived, problity_of_female_unSurvived, problity_of_old_unSurvived,
            problity_of_rich_unSurvived,problity_of_female_Survived,problity_of_old_Survived,problity_of_rich_Survived):
    if age != '' and fare != '' and sex != '':
        if float(age) > mean_age and sex == 'male' and float(fare) > mean_fare:
            survive = (1-problity_of_unSurvived) * problity_of_old_Survived * (1-problity_of_female_Survived) * problity_of_rich_Survived
            unsurvived = problity_of_unSurvived * problity_of_old_unSurvived * (1-problity_of_female_unSurvived) * problity_of_rich_unSurvived
            if survive > unsurvived:
                return '1'
            else:
                return '0'

        elif float(age) <= mean_age and sex == 'male' and float(fare) > mean_fare:
            survive = (1-problity_of_unSurvived) * (1-problity_of_old_Survived) * (1-problity_of_female_Survived) * problity_of_rich_Survived
            unsurvived = problity_of_unSurvived * (1-problity_of_old_unSurvived) * (1-problity_of_female_unSurvived) * problity_of_rich_unSurvived
            if survive > unsurvived:
                return '1'
            else:
                return '0'

        elif float(age) > mean_age and sex == 'female' and float(fare) > mean_fare:
            survive = (1-problity_of_unSurvived) * problity_of_old_Survived * problity_of_female_Survived * problity_of_rich_Survived
            unsurvived = problity_of_unSurvived * problity_of_old_unSurvived * problity_of_female_unSurvived * problity_of_rich_unSurvived
            if survive > unsurvived:
                return '1'
            else:
                return '0'

        elif float(age) > mean_age and sex == 'male' and float(fare) <= mean_fare:
            survive = (1-problity_of_unSurvived) * problity_of_old_Survived * (1-problity_of_female_Survived) * (1-problity_of_rich_Survived)
            unsurvived = problity_of_unSurvived * problity_of_old_unSurvived * (1-problity_of_female_unSurvived) * (1-problity_of_rich_unSurvived)
            if survive > unsurvived:
                return '1'
            else:
                return '0'

        elif float(age) <= mean_age and sex == 'female' and float(fare) > mean_fare:
            survive = (1-problity_of_unSurvived) * (1-problity_of_old_Survived) * problity_of_female_Survived * problity_of_rich_Survived
            unsurvived = problity_of_unSurvived * (1-problity_of_old_unSurvived) * problity_of_female_unSurvived * problity_of_rich_unSurvived
            if survive > unsurvived:
                return '1'
            else:
                return '0'

        elif float(age) <= mean_age and sex == 'male' and float(fare) <= mean_fare:
            survive = (1-problity_of_unSurvived) * (1-problity_of_old_Survived) * (1-problity_of_female_Survived) * (1-problity_of_rich_Survived)
            unsurvived = problity_of_unSurvived * (1-problity_of_old_unSurvived) * (1-problity_of_female_unSurvived) * (1-problity_of_rich_unSurvived)
            if survive > unsurvived:
                return '1'
            else:
                return '0'

        elif float(age) > mean_age and sex == 'female' and float(fare) <= mean_fare:
            survive = (1-problity_of_unSurvived) * problity_of_old_Survived * problity_of_female_Survived * (1-problity_of_rich_Survived)
            unsurvived = problity_of_unSurvived * problity_of_old_unSurvived * problity_of_female_unSurvived * (1-problity_of_rich_unSurvived)
            if survive > unsurvived:
                return '1'
            else:
                return '0'

        if float(age) <= mean_age and sex == 'female' and float(fare) <= mean_fare:
            survive = (1-problity_of_unSurvived) * (1-problity_of_old_Survived) * problity_of_female_Survived * (1-problity_of_rich_Survived)
            unsurvived = problity_of_unSurvived * (1-problity_of_old_unSurvived) * problity_of_female_unSurvived * (1-problity_of_rich_unSurvived)
            if survive > unsurvived:
                return '1'
            else:
                return '0'

    else:
        return ''

def run_main():
    pre_list = []
    data_clean(r'./train.csv', r'./train.csv')
    data_clean(r'./test.csv', r'./test.csv')
    compute_probability(r'./train.csv')
    with open(r'./test.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            pre = predict(row['Age'], row['Sex'], row['Fare'])
            pre_list.append(pre)
    process_file = r'./gender_submission.csv'
    data_frame = pd.read_csv(process_file)
    data_frame['Survived'] = pre_list
    data_frame.to_csv(r'./gender_submission.csv', index = False)

if __name__ == '__main__':
    run_main()
