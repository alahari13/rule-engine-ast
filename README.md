# Rule Engine with Abstract Syntax Tree (AST)

## Overview
This application is a simple 3-tier rule engine that uses an Abstract Syntax Tree (AST) to determine user eligibility based on various attributes like age, department, income, etc. The engine allows for dynamic creation, combination, and modification of rules.

## Features
- Create rules dynamically via a RESTful API.
- Evaluate rules against user data.
- Combine multiple rules into a single evaluation.
- Store rules and their metadata in a SQLite database.

## Technologies Used
- Python 3.x
- Flask
- Flask-SQLAlchemy
- SQLite

## Prerequisites
Make sure you have installed Python and Git.

## Installation
1. **Clone the Repository:**
   git clone https://github.com/alahari13/rule-engine-ast.git
   cd rule-engine-ast
   
2.**Set Up a Virtual Environment:**
python -m venv env

3.**Activate the Virtual Environment:**
env\Scripts\activate

4.**Install Dependencies:**
pip install -r requirements.txt

5.**Run the Application:**
python app.py
The application will start running on http://127.0.0.1:5000.

## API Endpoints
**Create a Rule**
Endpoint: /create_rule
Method: POST
Request Body:
{
  "rule_string": "((age >= 30 AND department = 'Marketing') OR (salary > 50000))"
}

**Evaluate a Rule**
Endpoint: /evaluate_rule/<int:rule_id>
Method: POST
Request Body:
{
  "age": 35,
  "department": "Marketing",
  "salary": 60000
}

**Delete a Rule**
Endpoint: /delete_rule/<int:rule_id>
Method: DELETE
