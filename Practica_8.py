#Name - Ekta Buneti
#Roll No - S078

print("Name - Ekta Buneti")
print("Roll No - S078")

import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset("tips")


print(tips.head())


sns.scatterplot(x="total_bill", y="tip", data=tips)


plt.title("Restaurant Bill vs Tip")
plt.show()
