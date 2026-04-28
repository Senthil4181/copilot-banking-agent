"""Banking Agent - A simple banking system with account management."""


class InsufficientFundsError(Exception):
    """Raised when attempting to withdraw more funds than available."""
    pass


class BankingAgent:
    """A banking agent for managing accounts."""
    
    def __init__(self):
        """Initialize the banking agent with an empty accounts dictionary."""
        self.accounts = {}
    
    def create_account(self, account_id: str, account_holder: str, initial_balance: float = 0.0) -> dict:
        """
        Create a new bank account.
        
        Args:
            account_id: Unique identifier for the account
            account_holder: Name of the account holder
            initial_balance: Initial balance (default: 0.0)
            
        Returns:
            Dictionary containing account details
            
        Raises:
            ValueError: If account already exists
        """
        if account_id in self.accounts:
            raise ValueError(f"Account {account_id} already exists")
        
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        
        self.accounts[account_id] = {
            "account_id": account_id,
            "account_holder": account_holder,
            "balance": initial_balance
        }
        
        return self.accounts[account_id]
    
    def deposit_acc(self, account_id: str, amount: float) -> float:
        """
        Deposit money into an account.
        
        Args:
            account_id: Account identifier
            amount: Amount to deposit
            
        Returns:
            New account balance
            
        Raises:
            ValueError: If account not found or amount is invalid
        """
        if account_id not in self.accounts:
            raise ValueError(f"Account {account_id} not found")
        
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")
        
        self.accounts[account_id]["balance"] += amount
        return self.accounts[account_id]["balance"]
    
    def withdraw_acc(self, account_id: str, amount: float) -> float:
        """
        Withdraw money from an account.
        
        Args:
            account_id: Account identifier
            amount: Amount to withdraw
            
        Returns:
            New account balance
            
        Raises:
            ValueError: If account not found or amount is invalid
            InsufficientFundsError: If account balance is insufficient
        """
        if account_id not in self.accounts:
            raise ValueError(f"Account {account_id} not found")
        
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0")
        
        if not self._validate_sufficient_funds(account_id, amount):
            raise InsufficientFundsError(
                f"Insufficient funds in account {account_id}. "
                f"Current balance: {self.accounts[account_id]['balance']}, "
                f"Requested withdrawal: {amount}"
            )
        
        self.accounts[account_id]["balance"] -= amount
        return self.accounts[account_id]["balance"]
    
    def _validate_sufficient_funds(self, account_id: str, amount: float) -> bool:
        """
        Validate if the account has sufficient funds.
        
        Args:
            account_id: Account identifier
            amount: Amount to check
            
        Returns:
            True if sufficient funds, False otherwise
        """
        return self.accounts[account_id]["balance"] >= amount
    
    def get_balance(self, account_id: str) -> float:
        """
        Get the current balance of an account.
        
        Args:
            account_id: Account identifier
            
        Returns:
            Current account balance
            
        Raises:
            ValueError: If account not found
        """
        if account_id not in self.accounts:
            raise ValueError(f"Account {account_id} not found")
        
        return self.accounts[account_id]["balance"]
    
    def get_account_info(self, account_id: str) -> dict:
        """
        Get complete account information.
        
        Args:
            account_id: Account identifier
            
        Returns:
            Account information dictionary
            
        Raises:
            ValueError: If account not found
        """
        if account_id not in self.accounts:
            raise ValueError(f"Account {account_id} not found")
        
        return self.accounts[account_id].copy()


if __name__ == "__main__":
    # Example usage
    agent = BankingAgent()
    
    # Create accounts
    agent.create_account("ACC001", "John Doe", 1000.0)
    agent.create_account("ACC002", "Jane Smith", 500.0)
    
    # Display initial balances
    print("Initial Account Balances:")
    print(f"ACC001: ${agent.get_balance('ACC001')}")
    print(f"ACC002: ${agent.get_balance('ACC002')}")
    
    # Perform transactions
    print("\nPerforming Transactions:")
    agent.deposit_acc("ACC001", 200.0)
    print(f"ACC001 after deposit: ${agent.get_balance('ACC001')}")
    
    agent.withdraw_acc("ACC001", 300.0)
    print(f"ACC001 after withdrawal: ${agent.get_balance('ACC001')}")
    
    # Try to withdraw more than available
    try:
        agent.withdraw_acc("ACC002", 600.0)
    except InsufficientFundsError as e:
        print(f"\nError: {e}")
