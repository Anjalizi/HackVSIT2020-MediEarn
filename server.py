import json
from werkzeug import secure_filename
from flask import Flask
from web3 import Web3
from flask import request, render_template
from .deploy_contract import setup_w3_addr
from .img2txt import validate_document

app = Flask(__name__, static_url_path='/static')
w3, reports = setup_w3_addr()

avail_addr = w3.eth.accounts
avail_addr = avail_addr[1:]

base_addr = avail_addr[0]
base_addr_pk = '0xa00e77d96ddc77f3f66cda7e9a9d7cd00beff8140c571a91651de2b8bcaa8ff3'

@app.route('/', methods=['GET'])
def index():
	# print(avail_addr)
	# tx_hash = reports.functions.addNewReportRecord('Manish', 'Wow What a report').transact()
	# tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
	# print(reports.functions.getAllReportsSize().call())
	return render_template('index.html', isThere=False)

@app.route('/<token>', methods=['GET'])
def index_token(token):
	return render_template('index.html', isThere=True, token=token)

@app.route('/new', methods=['GET'])
def get_new_token():
	try:
		new_addr = avail_addr.pop()
		return render_template('new.html', sorry=False, addr=new_addr)
	except Exception as e:
		return render_template('new.html', sorry=True)


@app.route('/submit', methods=['POST', 'GET'])
def submit_form():
	try:
		file = request.files['file']
		secure_name = secure_filename(file.filename)
		file.save(secure_name)
		user_addr = dict(request.form).get('token')
		result = validate_document(secure_name)
		if result[0]:
			try:
				tx_hash = reports.functions.addNewReportRecord(user_addr, result[1]).transact()
				tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
				print('added to contract')

				try:
					tx_hash = w3.eth.sendTransaction({
						'to': user_addr,
						'from': base_addr,
						'value': w3.toWei('1', 'ether')
						})
					print(tx_hash)
					print('payment made')
					return render_template('submit.html', successful=True, addr=user_addr)

				except Exception as e:
					print('problem with giving incentives')
					return render_template('submit.html', successful=False, addr=user_addr)

			except Exception as e:
				print('error while adding to contract')
				return render_template('submit.html', successful=False, addr=user_addr)
		else:
			print('report validation not successful')
			return render_template('submit.html', successful=False, addr=user_addr)

	except Exception as e:
		print('error somewhere else')
		return render_template('submit.html', successful=False)

@app.route('/balance', methods=['GET'])
def balance_all():
	for i in range(10):
		print(w3.eth.getBalance(w3.eth.accounts[i]))
	return "balance"

@app.route('/wallet/<token>', methods=['GET'])
def balance_wallet(token):
	try:
		balance = w3.fromWei(w3.eth.getBalance(token), 'ether')
		return render_template('wallet.html', wallet=True, balance=balance, addr=token)
	except Exception as e:
		return render_template('wallet.html', wallet=False)

if __name__ == '__main__':
	app.run(debug=True)