//npm install web3
const { Web3 } = require('web3');
const web3 = new Web3(new Web3.providers.HttpProvider('http://127.0.0.1:7545'));
async function mine() {
    const accounts = await web3.eth.getAccounts();
    const coinbaseacc1 = accounts[0];
    const coinbaseacc2 = accounts[1];
    console.log('Mining etheron Ganache with coinbase address:${coinbaseacc1}');
    while (true) {
        try {
            await web3.eth.sendTransaction({
                from: coinbaseacc1, to: coinbaseacc2,
                value: 50,
            });
            console.log('Hii Shiva Mined a new block!');
        } catch (err) {
            console.error(err);
        }
    }
} mine();