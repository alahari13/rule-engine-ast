from flask import Flask, request, jsonify
from models import db, Rule
import operator

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

@app.route('/')
def index():
    return "Welcome to the Rule Engine!"

@app.route('/create_rule', methods=['POST'])
def create_rule():
    data = request.json
    rule_string = data.get('rule_string')

    if not rule_string:
        return jsonify({'error': 'Rule string is required'}), 400

    new_rule = Rule(rule_string=rule_string)
    db.session.add(new_rule)
    db.session.commit()

    return jsonify({'message': 'Rule created successfully', 'rule_id': new_rule.id}), 201

@app.route('/evaluate_rule/<int:rule_id>', methods=['POST'])
def evaluate_rule(rule_id):
    rule = Rule.query.get(rule_id)
    if not rule:
        return jsonify({'error': 'Rule not found'}), 404

    user_data = request.json  # Get user data from request

    try:
        evaluation_result = parse_and_evaluate_rule(rule.rule_string, user_data)
        return jsonify({
            'rule_string': rule.rule_string,
            'evaluation_result': evaluation_result
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 400

def parse_and_evaluate_rule(rule_string, user_data):
    # Manually evaluate conditions
    conditions = rule_string.split()  # Simple split by space for now; can be improved for complex rules
    print(f"Parsed conditions: {conditions}")  # Debugging

    ops = {
        '>=': operator.ge,
        '<=': operator.le,
        '>': operator.gt,
        '<': operator.lt,
        '==': operator.eq,
        'AND': operator.and_,
        'OR': operator.or_,
    }

    # Example parsing and evaluation of conditions
    # For a rule like: (age >= 30 AND department == 'Marketing') OR salary > 50000
    # We will manually evaluate these based on the user_data provided
    if 'age' in rule_string:
        age_condition = user_data['age'] >= 30
    if 'department' in rule_string:
        department_condition = user_data['department'] == 'Marketing'
    if 'salary' in rule_string:
        salary_condition = user_data['salary'] > 50000

    # Combine conditions manually for now (this should be improved for more complex rules)
    result = (age_condition and department_condition) or salary_condition
    return result

# Create the database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
