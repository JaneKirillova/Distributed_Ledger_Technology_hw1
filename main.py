from digital_signature import sign, verify, generate_keys

if __name__ == "__main__":
    public_key, private_key = generate_keys()

    message = "Message to sign."

    signature = sign(message, private_key)

    is_verified = verify(message, signature, public_key)
    print("Signature Verified:", is_verified)