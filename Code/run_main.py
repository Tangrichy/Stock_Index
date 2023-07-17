from Function import * 

# ZZ1000 
ZZ_data, ZZ_price = read_data(indexs="ZZ1000")

ZZ_evaluation = evaluation_rank(data=ZZ_data)

ZZ_evaluation_price = ZZ_evaluation.merge(ZZ_price)

for i in ["PE", "PB", 'PBPE', "Risk"]:
    vis_plot(price_data = ZZ_evaluation_price[["Date", "Close"]], 
              factor_data = ZZ_evaluation_price[["Date", i]], 
              title = i, index_name="ZZ1000" ,y_axis = i, file_name=i)
    plt.clf()

# ZZ500
ZZ500_data

#HS300
HS_data, HS_price = read_data(indexs="HS300")

HS_evaluation = evaluation_rank(data=HS_data)

HS_evaluation_price = HS_evaluation.merge(HS_price)

for i in ["PE", "PB", 'PBPE', "Risk"]:
    vis_plot(price_data = HS_evaluation_price[["Date", "Close"]], 
              factor_data = HS_evaluation_price[["Date", i]], 
              title = i, index_name="HS300" ,y_axis = i, file_name=i)
    plt.clf()
