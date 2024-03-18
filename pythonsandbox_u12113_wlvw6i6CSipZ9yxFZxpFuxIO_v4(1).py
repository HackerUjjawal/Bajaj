import requests
import json

url = "https://customer-analytics-34146.my.salesforce-sites.com/services/apexrest/createAccount"
headers = {"Content-Type": "application/json"}

# Replace with your details
data = {
    "name": "Your Full Name",
    "email": "your_colle@example.com",
    "rollNumber": 2110991923,  
    "phone": 8709403012  
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    # Account creation successful
    data = response.json()
    account_number = data["accountNumber"]
    print("Investment account created successfully!")
    print(f"Your account number: {account_number}")
else:
    print("Error creating account:", response.text)
