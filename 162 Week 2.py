import matplotlib.pyplot as plot
# set up your lists
numlist = [7, 5, 4, 8]
namelist = ['morning', 'afternoon', 'evening', 'night']
colorlist = ['#91D9D1', '#EDD432', '#B06FFF', '#4575DB']
explodelist = [0.0, 0.0, 0.0, 0.05]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.2f%%', colors=colorlist,
									explode=explodelist, startangle=90)
plot.axis('equal')
plot.text(-0.9,1.2,"Amount of Hours for Each Time of Day")
plot.savefig('piechart.png')
