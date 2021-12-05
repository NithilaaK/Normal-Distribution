import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("Project/stuper.csv")
mstu_list = df["math score"].to_list()

mmean = statistics.mean(mstu_list)
mstd_dev = statistics.stdev(mstu_list)
mmedian = statistics.median(mstu_list)
mmode = statistics.mode(mstu_list)

m1stdevs, m1stdeve = mmean - mstd_dev, mmean + mstd_dev
m2stdevs, m2stdeve = mmean - (mstd_dev*2), mmean + (mstd_dev*2)
m3stdevs, m3stdeve = mmean - (mstd_dev*3), mmean + (mstd_dev*3)

m_1_list_of_data = [result for result in mstu_list if result > m1stdevs and result < m1stdeve]
m_2_list_of_data = [result for result in mstu_list if result > m2stdevs and result < m2stdeve]
m_3_list_of_data = [result for result in mstu_list if result > m3stdevs and result < m3stdeve]

print("MATH SCORES")
print("The mean of the data is {}".format(mmean))
print("The median of the data is {}".format(mmedian))
print("The mode of the data is {}".format(mmode))
print("{}% of data lies within the 1st standard deviation".format(len(m_1_list_of_data)*100.0/len(mstu_list)))
print("{}% of data lies within the 2nd standard deviation".format(len(m_2_list_of_data)*100.0/len(mstu_list)))
print("{}% of data lies within the 3rd standard deviation".format(len(m_3_list_of_data)*100.0/len(mstu_list)))
plo = input("Would you like to plot this data (Y/N)? ")
if plo == "Y":
    fig = ff.create_distplot([mstu_list], ["Math Scores"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mmean, mmean], y=[0, 0.17], mode="lines", name="Mean"))
    fig.add_trace(go.Scatter(x=[m1stdevs, m1stdevs], y=[0, 0.17], mode="lines", name="Standard Deviation 1"))
    fig.add_trace(go.Scatter(x=[m1stdeve, m1stdeve], y=[0, 0.17], mode="lines", name="Standard Deviation 1"))
    fig.add_trace(go.Scatter(x=[m2stdevs, m2stdevs], y=[0, 0.17], mode="lines", name="Standard Deviation 2"))
    fig.add_trace(go.Scatter(x=[m2stdeve, m2stdeve], y=[0, 0.17], mode="lines", name="Standard Deviation 2"))
    fig.add_trace(go.Scatter(x=[m3stdevs, m3stdevs], y=[0, 0.17], mode="lines", name="Standard Deviation 3"))
    fig.add_trace(go.Scatter(x=[m3stdeve, m3stdeve], y=[0, 0.17], mode="lines", name="Standard Deviation 3"))
    fig.show()
elif plo == "N":
    print("OK.")
else:
    print("This is an invalid command.")