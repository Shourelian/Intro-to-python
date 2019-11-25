market = {"dairy":["yogurt","cheese"] , 
"fruits":["banana","apple","orange","lemon","apple","banana","banana"]}

market["candies"]=["mars", "kinder", "twix"]

lala= set(market["fruits"]) 

market["fruits"] = list(lala)
market["fruits"].sort()
print(market)
