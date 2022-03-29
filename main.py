import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Niemcy", "Francja", "Włochy", "Hiszpania", "Polska", "Rumunia", "Holandia", "Belgia", "Grecja", "Czehy", "Portugalia", "Szwecja", "Węgry", "Austria", "Bułgaria", "Dania", "Finlandia", "Słowacja", "Irlandia", "Chorwacja", "Litwa", "Słowenia", "Łotwa", "Estonia", "Cypr", "Luksemburg", "Malta"])
y = np.array([3134070, 2228857, 1672438, 1113851, 424269, 169578, 697219, 421611, 175888, 174412, 184931, 462057, 112399, 349344, 47364, 276805, 214062, 80958, 265835, 45557, 38637, 39769, 25021, 20916, 17901, 54195, 9898])

plt.bar(x,y)
plt.show()
'''
x = np.array([25.7, 24.1, 14.8, 11.5, 10.3, 4.9, 8.7])
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))
mylabels = ["SPD", "CDU/CSU", "Greens", "FDP", "AfD", "Left Party", "Others"]
mycolors = ["red", "brown", "green", "yellow", "blue", "purple", "grey"]

plt.pie(x, labels = mylabels, colors = mycolors, autopct="%1.00f%%")
plt.show()
'''