// VULNERABLE CONTRACT FOR TESTING
pragma solidity ^0.7.0;

contract BadBank {
    mapping(address => uint) balances;
    
    function withdraw() public {
        uint amount = balances[msg.sender];
        // VULN 1: Reentrancy - external call before state change
        msg.sender.call{value: amount}("");
        balances[msg.sender] = 0;
    }
    
    function getOwner() public view returns(address) {
        // VULN 2: msg.sender used
        return msg.sender;
    }
}
