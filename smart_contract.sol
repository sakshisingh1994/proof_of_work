// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ProofOfWorkExample {
    address public owner;
    string public message;
    uint256 public nonce;
    bytes32 public hash;

    event WorkSubmitted(address miner, string message, uint256 nonce, bytes32 hash);

    constructor() {
        owner = msg.sender;
    }

    function submitWork(string memory _message, uint256 _nonce) public {
        bytes32 guessHash = keccak256(abi.encodePacked(_message, _nonce));
        require(guessHash < bytes32(0x00000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff), "Proof of work not valid");

        message = _message;
        nonce = _nonce;
        hash = guessHash;

        emit WorkSubmitted(msg.sender, _message, _nonce, guessHash);
    }
}
