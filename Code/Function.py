# Loading package
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read data
## 沪深300 HS300
## 中证1000 ZZ1000
## 中证500 ZZ500

def read_data(indexs):
    if indexs == "ZZ1000":
        file = indexs + str(".xlsx")
    
    elif indexs == "HS300":
        file = indexs + str(".xlsx")
    
    elif indexs == "ZZ500":
        file = indexs + str(".xlsx")
    
    input_data = pd.read_excel(f"./Data/{file}")

    input_data["Date"] =  input_data["Date"].apply(pd.to_datetime)

    price_data = input_data[["Date", "Close"]]

    return input_data, price_data

# Calculate PE, PB, and Reverret
def evaluation_rank(data, window_len = None):
    if window_len == None:
        end_date = data["Date"][0] + datetime.timedelta(days = 365*5)
        window_len = len(data[data["Date"] <= end_date])
    else:
        window_len = window_len

    input_data = data[["Date","PE", "PB", "Risk"]]

    input_data.loc[:,["PE", "PB"]] = input_data.loc[:,["PE", "PB"]].rolling(window_len).rank(pct = True)
    input_data.loc[:,"Risk"] = input_data.loc[:,"Risk"].rolling(window_len).rank(pct = True, ascending=False)

    input_data = input_data.dropna()

    input_data["PBPE"] = (input_data["PE"] + input_data["PB"])/2

    return input_data

# save plot in file
def vis_plot(price_data, factor_data, title, index_name,y_axis,file_name, up_line=0.95, lower_line = 0.05):

    file = "./Plot/" + index_name + file_name + ".jpg"
    title_name = index_name + " " +title

    fig, ax1 = plt.subplots(num = 1, figsize = (12,6))
    ax1.plot(factor_data.Date, factor_data.iloc[:,1], color = 'blue', label = factor_data.iloc[:,1].name)
    ax1.set_ylabel(y_axis)
    ax1.axhline(y = up_line, color = "red", alpha = 0.8,label = "0.95")
    ax1.axhline(y = lower_line, color = "red", alpha = 0.8,label = "0.05")
    ax2 = ax1.twinx()
    ax2.plot(price_data.Date, price_data.iloc[:,1], color = 'orange', label = "Close")
    ax2.set_ylabel("Close")
    ax1.set_xlabel("Date")
    plt.title(title_name)
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.grid(True)
    ax1.legend(lines1 + lines2, labels1 +labels2, loc = "best")
    plt.savefig(file)