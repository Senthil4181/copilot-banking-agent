# Copilot Banking Agent

A simple banking system implementation demonstrating account management with Copilot integration capabilities.

## Overview

The Banking Agent is a Python-based system that provides core banking operations including:
- **Account Creation**: Create new bank accounts with initial balances
- **Deposits**: Add funds to existing accounts
- **Withdrawals**: Remove funds with automatic validation
- **Balance Inquiry**: Check current account balance
- **Insufficient Funds Validation**: Automatic checks to prevent overdrafts

## Features

✅ Create multiple bank accounts  
✅ Deposit and withdraw funds  
✅ Track account balances  
✅ Validate sufficient funds before withdrawal  
✅ Custom exception handling for financial operations  
✅ Account information retrieval  

## Installation

No external dependencies are required for basic functionality.

```bash
# Clone the repository
git clone https://github.com/Senthil4181/copilot-banking-agent.git
cd copilot-banking-agent
```

## Usage

### Basic Example

```python
from main import BankingAgent, InsufficientFundsError

# Initialize the banking agent
agent = BankingAgent()

# Create accounts
agent.create_account("ACC001", "John Doe", 1000.0)
agent.create_account("ACC002", "Jane Smith", 500.0)

# Deposit funds
agent.deposit_acc("ACC001", 200.0)

# Withdraw funds
agent.withdraw_acc("ACC001", 300.0)

# Check balance
balance = agent.get_balance("ACC001")
print(f"Current balance: ${balance}")

# Handle insufficient funds
try:
    agent.withdraw_acc("ACC002", 600.0)
except InsufficientFundsError as e:
    print(f"Error: {e}")
```

### Running the Example

```bash
python main.py
```

## API Reference

### BankingAgent Class

#### Methods

- **`create_account(account_id, account_holder, initial_balance=0.0)`**
  - Creates a new bank account
  - Returns: Account details dictionary

- **`deposit_acc(account_id, amount)`**
  - Deposits funds into an account
  - Returns: New account balance
  - Raises: `ValueError` if account not found or amount invalid

- **`withdraw_acc(account_id, amount)`**
  - Withdraws funds from an account
  - Returns: New account balance
  - Raises: `InsufficientFundsError` if insufficient funds
  - Raises: `ValueError` if account not found or amount invalid

- **`get_balance(account_id)`**
  - Retrieves the current balance
  - Returns: Current balance as float

- **`get_account_info(account_id)`**
  - Retrieves complete account information
  - Returns: Account details dictionary

## Error Handling

The system provides specific exception types for error handling:

- **`InsufficientFundsError`**: Raised when attempting to withdraw more than available balance
- **`ValueError`**: Raised for invalid operations (negative amounts, non-existent accounts, etc.)

## Project Structure

```
copilot-banking-agent/
├── main.py           # Main banking agent implementation
├── requirements.txt  # Project dependencies
└── README.md        # This file
```

## Future Enhancements

- Transaction history tracking
- Interest calculation
- Multi-currency support
- Database persistence
- REST API interface
- Unit and integration tests
- Copilot integration examples

## License

MIT License - feel free to use this project as a learning resource.

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues for bugs and feature requests.
