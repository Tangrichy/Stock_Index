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

def PBPE_risk_plot(data, upper_data, lower_data, index_name):

    file = "./Plot/" + index_name + "evaluation" + ".jpg"


    plt.figure(num = 1, figsize = (12,6))
    plt.grid()
    plt.plot(data.Date, data.Close , label = "Close")
    plt.plot(upper_data.Date, upper_data.Close, "^",label = "High")
    plt.plot(lower_data.Date, lower_data.Close, "^",label = "Lower")
    leg = plt.legend(loc='best')
    plt.title(index_name + " " + str("PBPE and Risk"))
    plt.xlabel('Date')
    plt.ylabel("Close")
    plt.savefig(file)


# PBPE, risk release sign

def sign_evaluation(data, upper = 0.95, lower = 0.05):
    if data["PBPE"] > upper or data["Risk"] >= upper:
        return "High"
    elif data["PBPE"] <= lower or data["Risk"] <= lower:
        return "Low"
    else:
        return "Stable"
    
# crowding
## prepare data
def crowding_data(data):
    output = data[["Date", "Close","volume", "turn", "High", "Low"]]
    # log return
    output["Close"] = np.log(output["Close"].pct_change() + 1)
    return output

## the power of upword

def exp_fun(data, window_len = None, moving_window = 20):

    if window_len == None:
        end_date = data["Date"][0] + datetime.timedelta(days = 365*5)
        window_len = len(data[data["Date"] <= end_date])
    else:
        window_len = window_len

    output = data[["Date", "Close"]] # select data and Close price
    # calucualte slop
    output["exp_fun"] = output["Close"].rolling(moving_window).sum()
    # rank
    output["exp_rank"] = output["exp_fun"].rolling(window_len).rank(pct = True)
    output = output.dropna()
    return output

def skew_kur(data, window_len = None, moving_window = 20):
    # initial window
    if window_len == None:
        end_date = data["Date"][0] + datetime.timedelta(days = 365*5)
        window_len = len(data[data["Date"] <= end_date])
    else:
        window_len = window_len

    output = data[["Date", "Close"]]
    return output