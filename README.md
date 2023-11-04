# Test task for CaptainTrunky
A simple stock market simulator.

## Basic technologies
![Python](https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white)![version](https://img.shields.io/badge/3.11-gray) <br>
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00.svg?style=flat&logo=SQLAlchemy&logoColor=white)![version](https://img.shields.io/badge/2.0.23-gray) <br>
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white)![version](https://img.shields.io/badge/7.4.3-gray) <br>

## About implementation
I used SQLite for storing and SQLAlchemy for managing orders,
because it's very simple and light software. Although, even it is too complex for the task,
I'm used to reserve a margin of technologies for potential development of the projects. 
For unit tests I used Pytest.
I applied pattern _Repository_ for Order Book class to manage stored orders, because
I think it's obvious solution here. 


## Running of the project
### Install
1. Open your work directory in terminal.
2. Make sure you have the latest versions of Git and Python installed.
3. Clone repository:
```bash
git clone https://github.com/JxSol/captaintrunky_test.git
```
4. Install requerements:
```bash
pip install -r requirements.txt
```
### Test
1. For running tests type into the terminal
```bash
pytest tests
```
2. Everything is fine if you see green results.
### Run
1. To run the simulation type into the terminal:
```bash
python main.py
```
2. To provide more iterations add an integer at the end of the command:
```bash
python main.py 1000
```


## Assignment Description

---

- Objective: To build a simple market simulator that can process orders and update the order book accordingly.
- Skills Tested: Python programming, understanding of algorithms, and software design principles.
- Estimated Time: 3-4 hours
### Task Description:
#### Design the Order Class:
Create an Order class with attributes like order_id, timestamp, type (buy/sell), quantity, and price.
#### Design the Order Book:
Create an OrderBook class that maintains a list of buy and sell orders.
Implement methods to add, modify, and remove orders from the order book.
#### Order Matching Algorithm:
Implement a method in the OrderBook class to match orders.
The method should match the highest price buy order with the lowest price sell order.
If the order can’t be matched, it should be added to the order book.
#### Market Simulator:
Create a function to simulate the market.
It should generate random orders and pass them to the order book.
It should periodically match orders in the order book and print out the trades.
#### Testing:
Write unit tests to ensure your classes and methods are working as expected.
#### Deliverables:
Python script(s) with classes and functions implemented.
A text file explaining your design choices and any assumptions you made.
Unit tests and their results.

Remember, this is a simple simulator. There are many complexities in a real trading system that we’re not considering here for simplicity’s sake. In case you will join our team, this time will be paid, Good luck! 🍀 

---