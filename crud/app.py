# Import libraries
from flask import Flask, request, redirect, render_template, url_for
# Instantiate Flask functionality
app = Flask('crud_app')
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]
# Read operation
@app.route('/')
def get_transactions():
    return render_template('transactions.html', transactions=transactions)
# Create operation
@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        date = request.form['date']
        amount = float(request.form['amount'])
        new_transaction = {'id': len(transactions) + 1, 'date': date, 'amount': amount}
        transactions.append(new_transaction)
        return redirect(url_for('get_transactions'))
    return render_template('form.html')
# Update operation
@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    if request.method == 'POST':
        date = request.form['date']
        amount = float(request.form['amount'])
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date
                transaction['amount'] = amount
                return redirect(url_for('get_transactions'))
        return redirect(url_for('get_transactions'))
    # If the request method is GET, find the transaction with the matching ID and render the edit form
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            return render_template('edit.html', transaction=transaction)
    # If the transaction with the specified ID is not found, handle this case (optional)
    return {"message": "Transaction not found"}, 404

# Delete operation
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break 
    return redirect(url_for('get_transactions'))
# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
    