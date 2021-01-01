#!/usr/bin/env python
# coding: utf-8

# Pastoral Datasets: Marriage Preparation Seminar

# In[71]:
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# MarriagePreparationSeminar.csv is a history of monthly summary record of one of the church ministry called 
# Pastoral Services. This data represents the performance accomplishment for an event named 
# "Marriage Preparation Seminar". This event is usually projected on a monthly basis as presented during 
# Yearend Strategic Planning for the incoming year.
# 		Reports are usually presented every end of the month (in my time, every last Wednesday).
# 			Month_End : Last Saturday of the month
# 			Min_Month : Projected participants every event. Please take note that each number 
# 						represents a couple.
# 			Actual_Month : Represent the actual number of participants who completed the events.
# 
# NOTE: Schedule that would fall on holidays and important family days were usually compressed to a 
# 		shorter meetings depending on the duration of the holidays (e.g. Holy Week, Christmas weeks, etc.)

# In[72]:
MPS_data = pd.read_csv("MarriagePreparationSeminar.csv", index_col=0, parse_dates=True)

# In[73]:
MPS_data.head()

# Creating a column for the variance between projected and actual participants
# In[74]:
MPS_data["Unable To Complete"] = MPS_data["Min_Month"] - MPS_data["Actual_Month"]

# In[75]:
MPS_data.head()


# Creating a column for the percentage of accomplishment
# In[76]:
MPS_data["PercentagePerformance"] = (MPS_data["Actual_Month"] / MPS_data["Min_Month"]) * 100

# In[77]:
MPS_data.head()


# Description of our data set
# In[78]:
MPS_data.info()

# In[79]:
MPS_data[["Min_Month", "Actual_Month"]].describe()

# In[80]:
MPS_data[["Min_Month", "Actual_Month"]].mean()

# In[81]:
MPS_data[["Min_Month", "Actual_Month"]].median()

# In[82]:
MPS_data.shape

# In[83]:
MPS_data.size


# Creating a pandas plot comparison
# In[84]:
MPS_data[["Min_Month", "Actual_Month"]].plot()

# Creating a scatter plot comparison
# In[85]:
MPS_data.plot.scatter(x="Min_Month", y="Actual_Month", alpha=1)


# Presenting each column in a pandas separate subplot
# In[86]:
MPS_data = pd.read_csv("MarriagePreparationSeminar.csv", index_col=0, parse_dates=True)
MPS_data.plot.area(figsize=(12, 4), subplots=True)

# In[87]:
fig, axs = plt.subplots(figsize=(12, 4))
MPS_data.plot.area(ax=axs)
axs.set_ylabel("Number of Participants")
axs.set_xlabel("End of the Month")
fig.savefig("mps.png")


# Creating pivot table from existing columns and can be plotted instantly
# In[88]:
MPS_data.pivot(columns="Min_Month", values="Min_Month")

# In[89]:
# MPS_data.pivot(columns="Min_Month", values="Min_Month").plot()

# In[90]:
MPS_data.pivot(columns="Actual_Month", values="Actual_Month")

# In[91]:
# MPS_data.pivot(columns="Actual_Month", values="Actual_Month").plot()


# Creating matplotlib plot plt line comparison 
# In[92]:
MPS_data = pd.read_csv("MarriagePreparationSeminar.csv", parse_dates=True)
target_perform = MPS_data['Min_Month']
actual_perform = MPS_data['Actual_Month']
endofmonth = MPS_data['Month_End']

# In[93]:
plt.figure(figsize=(14,4))
plt.plot(endofmonth, actual_perform, color='green', marker='', linestyle='dotted', label='Actual')
plt.plot(endofmonth, target_perform, color='red', marker='', linestyle='dotted', label='Target')
plt.title("Marriage Preparation 2015-2020")
plt.ylabel("Participants (couples)")
plt.xlabel("End of the Month")
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.legend(loc='upper left')
plt.show()

