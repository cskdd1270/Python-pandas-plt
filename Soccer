import csv
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('SoccerLEagues.csv',encoding = 'cp949')
df2 = pd.read_csv('results.csv',encoding = 'utf-8')

color = ['gold', 'silver', 'lightgray']
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 2}

mean_HW = df['HomeWins'].mean()
mean_HD = df['HomeDraw'].mean()
mean_HL = df['HomeLoss'].mean()
mean_AW = df['AwayWins'].mean()
mean_AD = df['AwayDraw'].mean()
mean_AL = df['AwayLoss'].mean()

plt.figure(figsize=(15,15))
plt.subplot(1,3,1)
size = [mean_HW,mean_HD,mean_HL]
label= ['Win','Draw', 'Lose']
explode = [0.05, 0.05, 0.05]
plt.title('Soccer Home')
plt.pie(size, labels =label , autopct="%0.1f%%" , explode = explode , shadow=True, colors = color, counterclock=False,startangle=130, wedgeprops=wedgeprops)


plt.subplot(1,3,2)
size2 = [mean_AW,mean_AD,mean_AL]
label= ['Win','Draw', 'Lose']
plt.title('Soccer Away')
plt.pie(size2, labels =label , autopct="%0.1f%%", explode = explode , shadow=True ,  colors = color, counterclock=False,startangle=110, wedgeprops=wedgeprops)


mean_HS = df2['home_score'].mean()
mean_AS = df2['away_score'].mean()
plt.subplot(1,3,3)
plt.title('Goal')
label_goal = ['home','away']
size3 = [mean_HS , mean_AS]
plt.pie(size3, autopct="%0.1f%%" ,labels = label_goal, shadow=True ,counterclock=False,startangle=140, wedgeprops=wedgeprops)

plt.show()
