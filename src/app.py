from flask import Flask, jsonify, request
from expense_service import add_expense, get_all_expenses, filter_by_category,calculate_total,delete_expense
app = Flask(__name__)
@app.route("/")
def home():
    return jsonify({
        "message": "Hi!! Welcome to Expense Tracker API"})
@app.route("/expenses",methods=["POST"])
def create_expense():
    data = request.get_json()
    expense = add_expense(data)
    return jsonify(expense), 201
@app.route("/expenses", methods=["GET"])
def get_expenses():
    category = request.args.get("category")
    if category:
        return jsonify(filter_by_category(category))
    return jsonify(get_all_expenses())
@app.route("/expenses/total", methods=["GET"])
def total_expenses():
    return jsonify(calculate_total())
@app.route("/expenses/<int:expense_id>", methods=["DELETE"])
def delete(expense_id):
    deleted = delete_expense(expense_id)
    if deleted:
        return jsonify({"message": "Expense deleted successfully"}), 200
    return jsonify({"message": "Expense not found"}), 404
if __name__ == "__main__":
    app.run(debug=True)