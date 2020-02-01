pragma solidity >=0.4.22 <0.6.0;

contract reportsRecords {

	struct report {
		string name;
		string record;
	}

	report[] allReports;

	function addNewReportRecord(string memory rName, string memory rRecord) public returns (bool) {
		report memory reportObj = report({name: rName, record: rRecord});
		allReports.push(reportObj);

		return true;
	}

	function getAllReportsSize() public returns (uint) {
		return allReports.length;
	}

}