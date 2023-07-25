# laoding package

from Function import *
import os 
####### set work direction
os.getcwd()
upDir = os.path.pardir
os.chdir(upDir)
##############

###########Evaluation################

# ZZ1000 
## read data
ZZ_data, ZZ_price = read_data(indexs="ZZ1000")
## PB PE PBPE Roverrt
ZZ_evaluation = evaluation_rank(data=ZZ_data)
## prepare data for plot
ZZ_evaluation_price = ZZ_evaluation.merge(ZZ_price)
## plot for PB PE PBPE Roverrt
for i in ["PE", "PB", 'PBPE', "Risk"]:
    vis_plot(price_data = ZZ_evaluation_price[["Date", "Close"]], 
              factor_data = ZZ_evaluation_price[["Date", i]], 
              title = i, index_name="ZZ1000" ,y_axis = i, file_name=i)
    plt.clf()
## Combine PBPE and Risk
ZZ_evaluation_price["Sign"] = ZZ_evaluation_price.apply(sign_evaluation, axis = 1)
ZZ_upper = ZZ_evaluation_price[ZZ_evaluation_price["Sign"] == "High"]
ZZ_low = ZZ_evaluation_price[ZZ_evaluation_price["Sign"] == "Low"]
## plot PBPE Roverrt
PBPE_risk_plot(data = ZZ_evaluation_price, upper_data = ZZ_upper, lower_data = ZZ_low, index_name = "ZZ1000")

# ZZ500
## read data
ZZ500_data, ZZ500_price =  read_data(indexs="ZZ500")
## PB PE PBPE Roverr
ZZ500_evaluation = evaluation_rank(data=ZZ500_data)
## prepare data for plot
ZZ500_evaluation_price = ZZ500_evaluation.merge(ZZ500_price)
## plot for PB PE PBPE Roverrt
for i in ["PE", "PB", 'PBPE', "Risk"]:
    vis_plot(price_data = ZZ500_evaluation_price[["Date", "Close"]], 
              factor_data = ZZ500_evaluation_price[["Date", i]], 
              title = i, index_name="ZZ500" ,y_axis = i, file_name=i)
    plt.clf()
## Combine PBPE and Risk
ZZ500_evaluation_price["Sign"] = ZZ500_evaluation_price.apply(sign_evaluation, axis = 1)
ZZ500_upper = ZZ500_evaluation_price[ZZ500_evaluation_price["Sign"] == "High"]
ZZ500_low = ZZ500_evaluation_price[ZZ500_evaluation_price["Sign"] == "Low"]
## plot PBPE Roverrt
PBPE_risk_plot(data = ZZ500_evaluation_price, upper_data = ZZ500_upper, lower_data = ZZ500_low, index_name = "ZZ500")


#HS300
## read data
HS_data, HS_price = read_data(indexs="HS300")
## plot PBPE Roverrt
HS_evaluation = evaluation_rank(data=HS_data)
## prepare data for plot
HS_evaluation_price = HS_evaluation.merge(HS_price)
## plot for PB PE PBPE Roverrt
for i in ["PE", "PB", 'PBPE', "Risk"]:
    vis_plot(price_data = HS_evaluation_price[["Date", "Close"]], 
              factor_data = HS_evaluation_price[["Date", i]], 
              title = i, index_name="HS300" ,y_axis = i, file_name=i)
    plt.clf()
## Combine PBPE and Risk
HS_evaluation_price["Sign"] = HS_evaluation_price.apply(sign_evaluation, axis = 1)
HS_upper = HS_evaluation_price[HS_evaluation_price["Sign"] == "High"]
HS_low = HS_evaluation_price[HS_evaluation_price["Sign"] == "Low"]
## plot PBPE Roverrt
PBPE_risk_plot(data = HS_evaluation_price, upper_data = HS_upper, lower_data = HS_low, index_name = "HS300")

################### Crowded

# Z1000