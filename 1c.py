import Crypto
import binascii
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
import datetime
import collections
import hashlib

class Client:
    def __init__(self):
        random = Crypto.Random.new().read
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format="DER")).decode("ascii")

class Transaction:
    def __init__(self, sender, receiver, value):
        self.sender = sender
        self.receiver = receiver
        self.value = value
        self.time = datetime.datetime.now()

    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity
        return collections.OrderedDict({
            "sender": identity,
            "receiver": self.receiver,
            "value": self.value,
            "time": self.time,
        })

    def sign_transaction(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode("utf8"))
        return binascii.hexlify(signer.sign(h)).decode("ascii")

def sha256(message):
    return hashlib.sha256(message.encode("ascii")).hexdigest()

def mine(message, difficulty=1):
    assert difficulty >= 1
    prefix = "1" * difficulty
    for i in range(1000):
        digest = sha256(str(hash(message)) + str(i))
        if digest.startswith(prefix):
            print("After " + str(i) + " iterations, found nonce: " + digest)
            return digest

class Block:
    TPCoins = []

    def __init__(self):
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.Nonce = ""

    @staticmethod
    def display_transaction(transaction):
        tx_dict = transaction.to_dict()
        print("Sender: " + tx_dict["sender"])
        print("-----")
        print("Receiver: " + tx_dict["receiver"])
        print("-----")
        print("Value: " + str(tx_dict["value"]))
        print("-----")
        print("Time: " + str(tx_dict["time"]))
        print("-----")

    @staticmethod
    def dump_blockchain():
        print("Number of blocks in chain: " + str(len(Block.TPCoins)))
        for x, block in enumerate(Block.TPCoins):
            print("Block #" + str(x))
            for transaction in block.verified_transactions:
                Block.display_transaction(transaction)
            print("-------")

# --- Simulation Part ---
transactions = []

Ninad = Client()
ks = Client()
vighnesh = Client()
sairaj = Client()

t1 = Transaction(Ninad, ks.identity, 15.0)
t1.sign_transaction()
transactions.append(t1)

t2 = Transaction(Ninad, vighnesh.identity, 6.0)
t2.sign_transaction()
transactions.append(t2)

t3 = Transaction(Ninad, sairaj.identity, 16.0)
t3.sign_transaction()
transactions.append(t3)

t4 = Transaction(vighnesh, Ninad.identity, 8.0)
t4.sign_transaction()
transactions.append(t4)

t5 = Transaction(vighnesh, ks.identity, 19.0)
t5.sign_transaction()
transactions.append(t5)

t6 = Transaction(vighnesh, sairaj.identity, 35.0)
t6.sign_transaction()
transactions.append(t6)

t7 = Transaction(sairaj, vighnesh.identity, 5.0)
t7.sign_transaction()
transactions.append(t7)

t8 = Transaction(sairaj, Ninad.identity, 12.0)
t8.sign_transaction()
transactions.append(t8)

t9 = Transaction(sairaj, ks.identity, 25.0)
t9.sign_transaction()
transactions.append(t9)

t10 = Transaction(Ninad, ks.identity, 1.0)
t10.sign_transaction()
transactions.append(t10)

for transaction in transactions:
    Block.display_transaction(transaction)
    print("*" * 50)
