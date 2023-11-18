import pandas as pd
from IPython.display import display



df = pd.read_excel('info.xlsx') 
df = df.dropna(how='all')



df = df.iloc[1:, :]



df = df.rename(columns={"RespondentID": "ID голосовавшего", "Have you seen any of the 6 films in the Star Wars franchise?": "Смотрел ли хоть один из 6 фильмов Звездных Воинов",
	"Do you consider yourself to be a fan of the Star Wars film franchise?": "ID голосовавшего",
	"Which of the following Star Wars films have you seen? Please select all that apply.": "Смотрел(а) ли 1 часть",
	"Unnamed: 4": "Смотрел(а) ли 2 часть",
	"Unnamed: 5": "Смотрел(а) ли 3 часть",
	"Unnamed: 6": "Смотрел(а) ли 4 часть",
	"Unnamed: 7": "Смотрел(а) ли 5 часть",
	"Unnamed: 8": "Смотрел(а) ли 6 часть",
	"Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.": "Оценка 1 части",
	"Unnamed: 10": "Оценка 2 части",
	"Unnamed: 11": "Оценка 3 части",
	"Unnamed: 12": "Оценка 4 части",
	"Unnamed: 13": "Оценка 5 части",
	"Unnamed: 14": "Оценка 6 части",
	"Please state whether you view the following characters favorably, unfavorably, or are unfamiliar with him/her.": "Оценка Хана Соло",
	"Unnamed: 16": "Оценка Люка Скайуокера",
	"Unnamed: 17": "Оценка Принцессы Леи",
	"Unnamed: 18": "Оценка Энакена Скайуокера",
	"Unnamed: 19": "Оценка Оби Вана Кеноби",
	"Unnamed: 20": "Оценка Императора Палпатина",
	"Unnamed: 21": "Оценка Дарта Вейдера",
	"Unnamed: 22": "Оценка Ландо Калрисиона",
	"Unnamed: 23": "Оценка Боба Фетта",
	"Unnamed: 24": "Оценка C-3P0",
	"Unnamed: 25": "Оценка R2 D2",
	"Unnamed: 26": "Джар Джар Бинкса",
	"Unnamed: 27": "Падмы Амидала",
	"Unnamed: 28": "Йоды",
	"Which character shot first?": "Кто был застрелян первым?",
	"Are you familiar with the Expanded Universe?": "Вы знакомы с расширенной вселенной?",
	"Do you consider yourself to be a fan of the Expanded Universe?Œæ": "Считаете ли вы себя фанатом расширенной вселенной?",
	"Do you consider yourself to be a fan of the Star Trek franchise?": "Считаете ли вы себя фанатом Стар Трека?",
	"Gender": "Пол",
	"Age": "Возраст",
	"Household Income": "Семейный доход",
	"Education": "Образование",
	"Education": "Образование",
	"Location (Census Region)": "Местоположение (регион)",
	})



'''замена на true/false'''
columns_to_process = df.columns[3:9]  
for column in columns_to_process:
    df[column] = df[column].fillna('false')  
    df[column] = df[column].apply(lambda x: 'true' if x != 'false' else x)




'''filtered males'''
''
male_df = df[(df['Пол'] == 'Male') &
                 ((df['Оценка 1 части'].isin(['5', '6'])) &
                  (df['Оценка 2 части'].isin(['5', '6'])) &
                  (df['Оценка 3 части'].isin(['5', '6'])) &
                  (df['Оценка 4 части'].isin(['1', '2'])) &
                  (df['Оценка 5 части'].isin(['1', '2'])) &
                  (df['Оценка 6 части'].isin(['1', '2'])))]
       
count = len(male_df[male_df['Считаете ли вы себя фанатом Стар Трека?'] == 'Yes'])
print("Количество фанатов Стар Трека в amle_df", count)






'''filttered females'''

female_rows = df[
	(df['Пол'] == 'Female') & 
	((df['Оценка 4 части'] == 1) & (df['Оценка 5 части'] != '1') & (df['Оценка 6 части'] != '1')) or 
	((df['Оценка 4 части'] != 1) & (df['Оценка 5 части'] == '1') & (df['Оценка 6 части'] != '1')) or
	((df['Оценка 4 части'] != 1) & (df['Оценка 5 части'] != '1') & (df['Оценка 6 части'] == '1'))
]
print(female_rows)




'''Скольким нрав части'''


count = len(df[(df['Оценка 1 части'] == '1')])
print("Сколько оценили 1 часть как 1", count)


count = len(df[(df['Оценка 2 части'] == '1')])
print("Сколько оценили 2 часть как 1", count)


count = len(df[(df['Оценка 3 части'] == '1')])
print("Сколько оценили 3 часть как 1", count)


count = len(df[(df['Оценка 4 части'] == '1')])
print("Сколько оценили 4 часть как 1", count)


count = len(df[(df['Оценка 5 части'] == '1')])
print("Сколько оценили 5 часть как 1", count)


count = len(df[(df['Оценка 6 части'] == '1')])
print("Сколько оценили 6 часть как 1", count)


