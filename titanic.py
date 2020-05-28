import pandas as pd

tit=pd.read_csv('e_titanic.csv', header=0, sep=',', index_col='PassengerId')

print(tit)
k=1
male=0
female=0
while (k<892):
	sex=tit.ix[k]['Sex']
	if sex=='male':
		male=male+1
	elif sex=='female' :
		female=female+1
	k=k+1
print('\nmale=',male)
print('\nfemale=',female)
print(tit['Sex'].value_counts())

#_______Гистограмма женских имен__________

w_name=tit.Name[:892][(tit.Sex=="female")]
w_name=w_name.str.split(',', expand=True)
print(w_name[:20])
print(w_name[0].value_counts())
#_________________________________________

#____________Количество_Выживших___________

print(tit['Survived'].value_counts())
surv=34200/892
print('\nsurv=',surv)
#__________________________________________
#____________Возраст_пассажиров_____________

print(tit['Age'].describe())
print('\nmedian=',tit['Age'].median())

#____________________________________________
#____________Количество в первом классе_____
print(tit['Pclass'].value_counts())
one_class=21600/892
print('\none_class=',one_class)

#___________________________________________

#_________Корреляция_Пирса___________________

corr_Pirs=tit['SibSp'].corr(tit['Parch'])
print('\ncorr_Pirs=',corr_Pirs)
#____________________________________________

#print(tit.Name[:20][(tit.Sex=="female")])

# frame=pd.DataFrame({'num': range(2), 'chars':'Nastya, Ms.Anastasia', })
# name=(frame[:2]['chars'])
# print(name)

# name=name.str.split(',', expand=True)
# print(name)
# frame=pd.DataFrame(name)
# print(frame[0].value_counts())
# print(frame)

print("finish")
