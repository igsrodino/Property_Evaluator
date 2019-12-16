# PASS OR FAIL PROPERTY INVESTMENT CALCULATOR #


purchase_price_total = int(input("Please enter total price for property wanted: "))
purchase_price_cash = int(input("Please enter $ amount used for purchase: "))
purchase_price_borrowed = (purchase_price_total - purchase_price_cash)
print("You are looking to borrow", purchase_price_borrowed, "dollars.")

closing_costs_total = int(input("Please enter total closing costs: "))
closing_costs_cash = int(input("Please enter closing costs paid with own cash: "))
closing_costs_borrowed = (closing_costs_total - closing_costs_cash)
print("Total borrowed for costs:", closing_costs_borrowed)

improvement_costs_total = int(input("Please enter total improvement costs: "))
improvement_costs_cash = int(input("Please enter improvement costs paid with own cash: "))
improvement_costs_borrowed = (improvement_costs_total - improvement_costs_cash)
print("Total borrowed for improvements:", improvement_costs_borrowed)

other_costs_total = int(input("Please enter total for any other costs: "))
other_costs_cash = int(input("Please enter other costs paid with own cash: "))
other_costs_borrowed = (other_costs_total - other_costs_cash)
print("Total borrowed for other costs:", other_costs_borrowed)


sub_total = (purchase_price_total + closing_costs_total + improvement_costs_total + other_costs_total)
print("Total $ for desired property:", sub_total)

initial_finance_total = int(input("Please enter total initial finance costs: "))
initial_finance_cash = int(input("Please enter initial costs paid with cash: "))
initial_finance_borrowed = (initial_finance_total - initial_finance_cash)
print("Total borrowed for initial finance costs: ")

total_borrowings = (purchase_price_borrowed + closing_costs_borrowed + improvement_costs_borrowed + \
                   other_costs_borrowed + initial_finance_borrowed)

total_cash_down = (purchase_price_cash + closing_costs_cash + improvement_costs_cash +
                   other_costs_cash + initial_finance_cash)

estimated_market_value = int(input("What is the estimated current market value for this property? "))
estimated_annual_growth = int(input("What is the estimated annual growth in dollar amount? "))

weekly_rent = int(input("What will be the weekly rent charged: "))
annual_rent = (weekly_rent * 52)
annual_management_fees = int(input("What will be the annual management fees: "))
annual_finance_costs = int(input("What will be the annual finance costs: "))
body_corp_fees = int(input("What will be the annual body corporate costs: "))
council_rates = int(input("What will be the annual council rate costs: "))
utility_costs = int(input("What will be the annual utility costs: "))
annual_insurance = int(input("What will be the annual insurance costs: "))
annual_taxes = int(input("What will be the annual tax costs: "))
annual_repairs = int(input("What will be the annual estimated repair costs: "))
annual_other_costs = int(input("What will be the estimated other annual costs: "))

annual_cash_flow = (annual_rent - annual_management_fees - annual_finance_costs -
                   body_corp_fees - council_rates - utility_costs - annual_insurance -
                   annual_taxes - annual_repairs - annual_other_costs)
print("Total annual cash flow is", annual_cash_flow)

estimated_annual_profit = (annual_cash_flow + estimated_annual_growth)
print("The estimated annual profit is:", estimated_annual_profit)

equity = (estimated_market_value - total_borrowings)
print("Total equity is:", equity)

gross_rent_return = ((annual_rent / purchase_price_total) * 100)
print("Estimated gross rent return:", gross_rent_return, "%")

return_on_investment = ((annual_cash_flow / purchase_price_total) * 100)
print("Estimated return on investment:", return_on_investment, "%")

growth_equity_return = ((estimated_annual_growth / equity) * 100)
print("Growth/Equity return: ", growth_equity_return)

cash_on_cash_return = ((annual_cash_flow / total_cash_down) * 100)
print("Cash/Cash Return:", cash_on_cash_return)

net_profit = ((estimated_annual_profit / total_cash_down) * 100)
print("Net profit:", net_profit)

current_interest_rate = (float(input("What is the current market interest rate:")))
cur_int_rate_times3 = (current_interest_rate * 3)

print(cur_int_rate_times3)











































































