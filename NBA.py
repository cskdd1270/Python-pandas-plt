import csv
import pandas as pd
import matplotlib.pyplot as plt

df_nba = pd.read_csv('NBA.csv',encoding = "utf-8")
color = ['gold' ,'lightgray']
nba_HW = df_nba['Home Wins'].mean()
nba_HL = df_nba['Home Loss'].mean()
nba_AW = df_nba['Away Wins'].mean()
nba_AL = df_nba['Away Loss'].mean()
plt.figure(figsize=(10,10))

plt.subplot(2,2,1)
size = [nba_HW,nba_HL]
label= ['Win','Lose']
explode = [0.05, 0.05]
plt.title('NBA Home')
plt.pie(size, labels =label , autopct="%0.1f%%" , explode = explode , shadow=True, colors = color, counterclock=False,startangle=170, wedgeprops=wedgeprops)


plt.subplot(2,2,2)
size2 = [nba_AW , nba_AL]
label= ['Win','Lose']
plt.title('NBA Away')
plt.pie(size2, labels =label , autopct="%0.1f%%", explode = explode , shadow=True ,  colors = color, counterclock=False,startangle=120, wedgeprops=wedgeprops)

plt.show()
