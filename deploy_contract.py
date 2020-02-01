from web3 import Web3
import json

def setup_w3_addr():

	w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
	bin_file = 'contracts_reports_sol_reportsRecords.bin'
	abi_file = 'contracts_reports_sol_reportsRecords.abi'

	def abi_and_bin():

		bin = ''
		abi = ''

		with open(abi_file) as f:
			abi = json.load(f)

		with open(bin_file) as f:
			bin = f.read()

		return abi, bin


	def deploy_contract():

		abi, bin = abi_and_bin()
		w3.eth.defaultAccount = w3.eth.accounts[0]
		contract = w3.eth.contract(
				abi=abi,
				bytecode=bin
			)
		tx_hash = contract.constructor().transact()
		tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

		contract_address = tx_receipt.contractAddress

		return contract_address


	abi, _ = abi_and_bin()
	contract_address = deploy_contract()
	myContract = w3.eth.contract(
			address=contract_address,
			abi=abi
		)
	return w3, myContract
