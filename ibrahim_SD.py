import math
import time

def prettify_data(data):
    pretty_string = "( "
    for i in range(len(data)):
        pretty_string += f"{data[i]} "
    pretty_string += " )"
    return pretty_string

data = []
decimals = int(input("How many decimals do you want for your SD? \n"))

print("Enter your data points, type 'done' when done.")
while True:
    user_input = input("Data point: ")
    if user_input == "done":
        break
    else:
        data_point = float(user_input)
        data.append(data_point)

print(f"Data: {prettify_data(data)}\n")
mean = round(sum(data)/len(data), decimals)
print(f"Sum is {sum(data)}")
print(f"Mean is {mean}\n")

variance_data = []
for i in range(len(data)):
    substract_mean = (data[i] - mean)
    square_substracted = round(substract_mean * substract_mean, decimals)
    variance_data.append(square_substracted)

print(f"Variance data is {prettify_data(variance_data)}")
variance_sum = round(sum(variance_data), decimals)
print(f"Variance sum is {variance_sum}")
variance_divided = round(variance_sum/(len(variance_data)-1), decimals)
print(f"Divided by n-1 is {variance_divided}\n")
standard_deviation = round(math.sqrt(variance_divided), decimals)
print(f"Standard Deviation is {standard_deviation}")
time.sleep(120)
#suuum = 0
#for i in range(10):
#    suuum += slist[i]
#print(suuum)#
#
#sum_var_l = []
#sum_var = 0
#for i in range(10):
#    variance = abs(slist[i] - 16.4)
#    print(variance)
#    variance_sq = variance * variance
#    print(variance_sq)
#    sum_var_l.append(round(variance_sq, 1))
#    sum_var += variance_sq
#print(sum_var)
#sum_var /= 9
#print(sum_var, math.sqrt(sum_var))
#print(sum_var_l)#
#
#ss = 0
#for i in range(len(sum_var_l)):
#    ss += sum_var_l[i]
#print(ss)