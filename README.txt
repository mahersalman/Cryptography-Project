Data Security and Cryptology – Project Report

Project Topic: 
An Application for secure email exchange: encryption-decryption with Cast-128 in CBC mode, secret key delivery with RSA + EL-Gamal signature.
Components:  
ENCRYPTION : 
	Check KEY – MUST be between 40 and 128 and divided by 8
	Text –partition the text to 64bit each block,
	If the last block is less than 64bit then add ‘0’ to all the bits to be 64 bit
	In CBC mode loop on the blocks as hex and encrypt each block using Cast128
	Concatenation all ciphertext to one string and return it.
DECRYPTION:
	Check KEY – MUST be between 40 and 128 and divided by 8 
	Text –partition the text to 64bit each block
	Decrypt according to cast128 and CBC mode 
Key Exchange: For resolving key exchange in the symmetric algorithm, we use an asymmetric RSA algorithm by encrypting the cast128 key with the public key received from the person who wants to decrypt it.
Digital signature: In order to verify the identity of the person who send the cast128 key we anticipate that the key will be signed, in our case we use the El-Gamal algorithm shared by authorized authority. 

The Project Flow:
Alice wants to send a secure email to Bob.
	Alice generates El-Gamal keys (private key, secret key)
	Bob Generate RSA keys 
public key∶{n,e} 
private key∶{d,p,q} 

	Alice and Bob shared their public key with each other.
	Alice use RSA and bob public key to encrypt the CAST128 key.
	Alice signs on the cipher text of the  cast128 key.
	Bob receives the cipher text of the CAST128 key and verifies it.
	Bob decrypts cipher text using RSA and his private key.
	Alice encrypts the message using Cast128 CBC mode 
	Alice send the message to Bob.
	Bob use Cast128 key and decrypt the message .

Example Output :
 

Conclusions: 
the algorithm implemented employs a robust combination of cryptographic techniques to ensure secure communication and data protection. 
The CAST-128 encryption algorithm in CBC mode offers strong confidentiality by encrypting data blocks with a secret key. 
The RSA encryption scheme, used for secret key delivery, provides secure key exchange through the encryption of a symmetric key. Additionally, the ElGamal signature scheme adds an extra layer of authentication and integrity verification, ensuring the legitimacy of the sender. 
Together, these techniques provide a comprehensive approach to encryption, decryption, and secure key delivery, bolstering the overall security of the system.

References:  
	rfc2144.txt.pdf (rfc-editor.org) 
	RSA Algorithm: Theory and Implementation in Python – AskPython 
	 - awnonbhowmik/RSA-Python: The RSA algorithm coded in Python
	 PowerPoint-esitys (hut.fi)
	GitHub - amritesh-dasari/ElGamal-signature-scheme: Verification of the ElGamal Signature Scheme Cryptography

