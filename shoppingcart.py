def disc_calc(u_price,quantity): # calculate the discount amount of the product which has unit price above 500
    amount = quantity * u_price
    if u_price >= 500 :
        discount = 0.05 * amount
        f_cost = amount- discount
        return f_cost
    # f_cost is the total cost or the price of the product
    else:
        return amount
def gst_calc(amount,gst):
    gst = amount * float(gst/100)

    return gst

p_list = [["Leather wallet",1100,18,1],["Umbrella",900,12,4],["cigarette",200,28,3],["Honey",100,0,2]]
#p_list is the product list
length = len(p_list)
final_price = []
max_gst = []
final_amount = []
for i in range(length):
    #for j in range(i+1):
    result1 = disc_calc(p_list[i][1],p_list[i][3])
    result2 = gst_calc(result1,p_list[i][2])
    final_price1 = result1 + result2
    final_amount.append(final_price1)
    max_gst.append(result2)
print("final amount to be payed",sum(final_amount))
print("maximum gst  amount of the prodct is ",max(max_gst),p_list[1][0])