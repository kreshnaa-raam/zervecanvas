import matplotlib.pyplot as plt

setosa = iris[iris.variety == "Setosa"]
versicolor = iris[iris.variety=='Versicolor']
virginica = iris[iris.variety=='Virginica']

fig, ax = plt.subplots()
fig.set_size_inches(13, 12) # adjusting the length and width of plot

# lables and scatter points
ax.scatter(setosa['petal.length'], setosa['petal.width'], label="Setosa", facecolor="blue")
ax.scatter(versicolor['petal.length'], versicolor['petal.width'], label="Versicolor", facecolor="green")
ax.scatter(virginica['petal.length'], virginica['petal.width'], label="Virginica", facecolor="red")


ax.set_xlabel("petal.length")
ax.set_ylabel("petal.width")
ax.grid()
ax.set_title("Iris petals")
ax.legend()


