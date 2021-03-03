# Fetch-Rewards-BE
Web-Services for user's points

**Installation Requirements:**
1. python 3
2. pip

**Clone repository in your system**
cd Fetch-Rewards-BE

**Instllation on Windows**
1. py -m pip install --user virtualenv
2.  py -3 -m venv venv
3. venv\Scripts\activate
4. pip install Flask
5. pip3 install -r requirements.txt
6. flask run -- To run the application

**Instllation on Mac & Linux**
1. python3 -m pip install --user virtualenv
2. python3 -m venv env
3. source env/bin/activate
4. pip3 install -r requirements.txt
5. flask run -- To run the application

**To run the test file**
1. start server using (flask run) on one terminal
2. In second terminal come to root directory and run (pytest)

**Assumptions**
1. Transactions records are in Json
2. In transactions reocrds points can be negative 

**Two ways to test HTTP request**
1. Using curl command (use command prompt)
2. using postman [Download Postman](https://www.postman.com/downloads/)

**Using Curl**
1. Case One (Inserting Transactions)
``` curl
curl --header "Content-Type: application/json" -d "{\"payer\":\"DANNON\",\"points\":100,\"timestamp\":\"2020-10-31T10:00:00Z\"}" http://localhost:5000/transactions
```
```response
{"Suscess":"Record inserted successfully"}
```
2. Case Two (To delete points)
```curl
curl --header "Content-Type: application/json" -d "{\"points\":100}" http://localhost:5000/delete_points
```
```response
[{"payer": "DANNON", "points": 1100}, {"payer": "UNILEVER", "points": 200}, {"payer": "MILLER COORS", "points": 10000}]
```
3. Case Three (To show balance)
```curl
curl  http://localhost:5000/balance
```
```response
{"DANNON":1100,"MILLER COORS":10000,"UNILEVER":200}
```

**Using Postman**
1. Case One (Inserting Transactions)
![image](https://user-images.githubusercontent.com/46578168/109746522-84a19600-7ba3-11eb-9468-45fd7e90cfbd.png)

2. Case Two (To delete points)
![image](https://user-images.githubusercontent.com/46578168/109746632-b4e93480-7ba3-11eb-8c26-3340c4d617c1.png)

3. Case Three (To show balance)
![image](https://user-images.githubusercontent.com/46578168/109746724-d9451100-7ba3-11eb-9557-d2cfe3a404cc.png)

