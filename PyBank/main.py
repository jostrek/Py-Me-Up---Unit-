import csv
import os
#file import
filename= 'pybank_data.csv'
#file output
file_to_output=os.path.join("analysis", "budget_analysis.txt")

#creating the important parameters
total_months=0
month_of_change=[]
net_change_list=[]
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0



with open(filename) as f:
	reader=csv.reader(f)
	header_row=next(reader)
	

	for row in reader:
		#tracking the total
		total_months=total_months + 1
		total_net= total_net+ int(row[1])	

	#tracking net change
		prev_net= int(row[1])
		net_change= int(row[1]) - prev_net
		net_change_list= net_change_list + [net_change]
		month_of_change= month_of_change + [row[0]]

	#getting greatest increase
		if net_change > greatest_increase[1]:
			greatest_increase[0]= row[0]
			greatest_increase[1]= net_change
	#getting greatest decrease
		if net_change < greatest_decrease[1]:
			greatest_decrease[0]= row[0]
			greatest_decrease[1]= net_change

#calc average net change
net_monthly_avg= sum(net_change_list) / len(net_change_list)

output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output)

with open (file_to_output, "w") as txt_file:
	txt_file.write(output)

