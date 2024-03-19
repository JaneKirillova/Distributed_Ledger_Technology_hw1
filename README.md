# Distributed_Ledger_Technology_hw1

Before usage please install all required libraries by running the following command:

`pip install -r requirements.txt`

The code allows to do two type of actions:

1. Sign some message. To do it please run the following in the command line from the root directory:

`python main.py "Your message to sign here" sign`

After this command signed message will be printed.

2. Verify that signature on the message. To do this please run the following in the command line from the root directory:

`python main.py "Your signed message here" verify`

This will print false or positive result of the verification