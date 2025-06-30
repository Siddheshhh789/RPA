// 1. Contracts
pragma solidity ^0.5.0;

contract ContractDemo {
    string message = "Hello Shivam";

    function dispMsg() public view returns (string memory) {
        return message;
    }
}

// Inheritance
pragma solidity >=0.4.22 <0.6.0;

contract Parent {
    uint256 internal sum;

    function setValue() external {
        uint256 a = 10;
        uint256 b = 20;
        sum = a + b;
    }
}

contract Child is Parent {
    function getValue() external view returns (uint256) {
        return sum;
    }
}
contract Caller {
    Child cc = new Child();

    function testInheritance() public returns (uint256) {
        cc.setValue();
        return cc.getValue();
    }

    function showValue() public view returns (uint256) {
        return cc.getValue();
    }
}

// -------------------------
// Constructors
pragma solidity ^0.5.0;
// Creating a contract
contract constructorExample {
string str;
constructor() public {
str = "Shankar Narayan College";
}
function getValue() public view returns (string memory) {
return str;
}
}


// Abstract Contracts
pragma solidity ^0.5.17;
contract Calculator {
function getResult() external view returns (uint256);
}
contract Test is Calculator {
constructor() public {}
function getResult() external view returns (uint256) {
uint256 a = 1;
uint256 b = 2;
uint256 result = a + b;
return result;
}
}


// Interfaces - Just change the name of the contract to something else because it is already used in the previous code
// pragma solidity ^0.5.0;
// interface Calculator {
// function getResult() external view returns (uint);
// }
// contract Test is Calculator {
// constructor() public {}
// function getResult() external view returns (uint) {
// uint a = 1;
// uint b = 2;
// uint result = a + b;
// return result;
// }
// }