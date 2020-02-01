## Project Title : Ethereum Track "MediEarn"

## Theme : SDG - Reducing Wealth Inequality

## Project Description
We're working towards creating a democratized healthcare data platform where users will be incentivized to retain complete ownership over their personal medical records. This is an attempt to disrupt monopoly over the ownership and access of data by corporates profitting off of it due to the unawareness of contibuting users which reduces wealth inequality by dis-empowering the **richer** section of the society from commercializing the data of the **poorer** section. This real world data will be anonymized and made available to medical research facilities for the study of innovative solutions to global health problems.

## What it Does?
* The user is assigned a unique address 
* The user uploads a document 
* The document is validated to check if it's a medical report or not using OpenCV and PyTesseract
* If the document is a medical report, the record is added to the ledger
* The incentive is then credited into the Ethereum wallet of the user

## Technology Stack Used
- Ganache CLI 
- Ethereum Blockchain
- Solidity for Smart Contracts
- Web3Py for Interfacing
- Python 
- PyTesseract to perform OCR
- OpenCV to read text from documents
- Flask as web framework

## Installation Steps

* Clone the repository using `git`
* Installing Ganache CLI and Solidity Compiler

 `$~ npm install -g ganache-cli solc`
* Installing the Python requirements

 `$~ pip install -r requirements.txt`
* Open a terminal and run ganache-cli

 `$~ ganache-cli`
* Follow the steps to setup and run the Flask Server

 ```bash
 $~ cd <project_directory>
 $~ virtualenv -p python3 venv
 $~ source venv/bin/activate
 $~ export FLASK_DEBUG=1 && export FLASK_APP=server.py
 $~ flask run
 ```
* Open up your favourite browser and type
 `localhost:5000` to get started.

### Available Endpoints

* `/` : frontpage endpoint.
* `/new` : generates a new token for the user. replicates a basic registration process.
* `/<token>` : endpoint for submitting documents
* `/wallet/<token>` : endpoint for viewing current wallet balance.


### Team Members

- Anjali Jain - [aj2966@gmail.com](aj2966@gmail.com)
- Rumanu - [rumanubhardwaj@gmail.com](rumanubhardwaj@gmail.com)
- Manish Devgan - [manish.nsit8@gmail.com](manish.nsit8@gmail.com)

