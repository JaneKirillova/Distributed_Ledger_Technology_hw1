from digital_signature import sign, verify, generate_keys
import argparse


def main():
    parser = argparse.ArgumentParser(description="Digital Signature Tool")
    parser.add_argument("input", help="Message that you want to sign or verify", type=str)
    parser.add_argument("action", help="Action to perform: 'verify' or 'sign' the message", choices=["verify", "sign"])

    args = parser.parse_args()

    message = args.input
    action = args.action
    public_key, private_key = generate_keys()
    signature = sign(message, private_key)

    if action == "verify":
        is_verified = verify(message, signature, public_key)
        print("Signature Verified:", is_verified)
    elif action == "sign":
        print("Sign message:", signature)


if __name__ == "__main__":
    main()
