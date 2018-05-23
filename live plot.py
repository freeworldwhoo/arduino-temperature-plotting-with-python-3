import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import datetime as dta
'''configuring the plot'''
style.use('ggplot')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    dateconv = dta.datetime.fromtimestamp
    '''define the function that gonna convert the unix time to date'''
    graph_data = open('example.txt','r').read()
    '''read the data from the txt file'''
    lines = graph_data.split('\n')
    ''' split the lines as a list'''
    xs = []
    ''' x axis the tempurature'''
    ys = []
    ''' y axis the date'''
    for line in lines:
        ''' read the lines and append the data to ys ans xs'''
        if len(line) > 1:
            '''get only the non-empty line'''
            x, y = line.split(',')
            x=float(x)
            y=float(y)
            xs.append(x)
            y = dateconv(y)
            ''' converte the unix time'''
            ys.append(y)
    '''plot the data'''
    ax1.clear()
    ax1.plot(ys, xs,label='temperature')
    for label in ax1.xaxis.get_ticklabels():
        '''set the rotation of the date into 45 degree in order to be readable'''
        label.set_rotation(45)
    plt.xlabel('date')
    plt.ylabel('temperature')
    plt.legend()
ani = animation.FuncAnimation(fig, animate, interval=1000)
'''animate the plot and refresh evry 1 second'''
plt.subplots_adjust(left=0.09, bottom=0.23, right=0.93, top=0.90, wspace=0.2, hspace=0)
'''just configurations'''
plt.show()

