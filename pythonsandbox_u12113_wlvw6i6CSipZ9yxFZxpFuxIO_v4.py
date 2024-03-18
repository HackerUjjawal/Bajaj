url = "https://customer-analytics-34146.my.salesforce-sites.com/services/apexrest/buyStocks"
headers = {
    "Content-Type": "application/json",
    "bfhl-auth": str(2110991923)  
}

data = {
    "company": "Bajaj Finserv",
    "currentPrice": 1571.65,  
    "accountNumber": 102031000,
    "githubRepoLink": "https://github.com/HackerUjjawal/Bajaj"  
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Investment successful!")
else:
    print("Error buying stocks:", response.text)
