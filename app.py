from flask import Flask
from flask import request
import  json
from helpers import util

app=Flask(__name__)


accounts = {}
transactions_insert = []
total_points = 0
@app.route('/transactions', methods=['POST'])
def transactions():
    global total_points
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
        if payer in accounts and (accounts[payer] - points) < 0 :
            response["Error"] = "Payer Amount is going negative"
        elif payer in accounts and (accounts[payer] - points) > 0:
            total_points += points
            accounts[payer]+=points
            transactions_insert.append(content)
            response["Suscess"] = "Record inserted successfully"
        else:
            response["Error"] = "Not a Valid Transaction"
    transactions_insert.sort(key= lambda x:x["timestamp"])
    
    return response

@app.route('/delete_points', methods=['POST'])
def delete_points():
    global total_points
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
        return response
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
    return json.dumps(remaining_balance)

if __name__ == '__name__':
    app.run(debug=True)