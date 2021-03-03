"""
app.py file is entry point of the application which handle 3 requests.
1. Insert Transaction
2. Delete Points
3. Show transactions
Created by: Priyank Dharani 03/01/2021
Modefied by:
"""

from flask import Flask
from flask import request
import  json
from helpers import util

app=Flask(__name__)


accounts = {}
transactions_insert = []
total_points = 0
status_code = 200

#1. Insert Transaction
@app.route('/transactions', methods=['POST'])
def transactions():
    global total_points
    global status_code
    response = {}
    content = request.get_json()
    util.check_required_args(content,'payer','points','timestamp')
    payer = content["payer"]
    points = content["points"]
    dttime = content["timestamp"]
    if points > 0 :
        total_points+= points
        if payer not in accounts:
            accounts[payer] = points
        else:
            accounts[payer] += points
        transactions_insert.append(content)
        response["Suscess"] = "Record inserted successfully"
    elif points < 0 :
        if payer in accounts and (accounts[payer] + points) < 0 :
            response["Error"] = "Payer Amount is going negative"
            status_code = 400
        elif payer in accounts and (accounts[payer] + points) > 0:
            total_points += points
            accounts[payer]+=points
            transactions_insert.append(content)
            response["Suscess"] = "Record inserted successfully"
        else:
            response["Error"] = "Not a Valid Transaction"
            status_code = 400
    else:
        response["Warning"] = "Points value should be greater than 0"
    transactions_insert.sort(key= lambda x:x["timestamp"])
    
    return response,status_code
	
#2. Delete Points
@app.route('/delete_points', methods=['POST'])
def delete_points():
    global total_points
    global status_code
    response = {}
    content = request.get_json()
    remaining_balance = {}
    util.check_required_args(content,'points')
    poins_deduct = content["points"]
    chk_points=0
    used_points=0
    if total_points < poins_deduct:
        response["Error"] = "Not Enough Points Available"
        response["Available Points"] = total_points
        status_code = 400
        return response,status_code
    else:
        for transid,transaction in enumerate(transactions_insert):
            chk_points = transaction["points"]
            trans_payer = transaction["payer"]
            if poins_deduct >0 and chk_points !=0:
                if poins_deduct >=chk_points:
                    used_points = chk_points
                    poins_deduct -= used_points
                    transactions_insert[transid]["points"] = 0
                else:
                    used_points = poins_deduct
                    remaining_points = chk_points - poins_deduct
                    transactions_insert[transid]["points"] = remaining_points
                    poins_deduct = 0
            if trans_payer in remaining_balance:
                remaining_balance[trans_payer] += transactions_insert[transid]["points"]
            else:
                remaining_balance[trans_payer] = transactions_insert[transid]["points"]
        
    total_points = sum([x["points"] for x in transactions_insert])
    final_result = [
        {"payer":payer,"points":points} for payer,points in remaining_balance.items()
    ]
    return json.dumps(final_result),status_code

#3. Show transactions
@app.route('/balance', methods=['GET'])
def balance():
	global status_code
	balance = {}

	for transaction in transactions_insert:
		payer = transaction["payer"]
		if payer not in balance:
			balance[payer] = transaction["points"]
		else:
			balance[payer] += transaction["points"]
	return balance,status_code

if __name__ == '__name__':
    app.run(debug=True)