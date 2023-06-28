import unittest


class Account:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number

class SavingAccount(Account):
    def __init__(self, balance, account_number, interest):
        super().__init__(balance, account_number)
        self.interest = interest
    def add(self):
        self.balance = self.balance + self.balance / 100 * self.interest
        
class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self.overdraft_limit = overdraft_limit

class Bank:
    def __init__(self, accounts:list[Account]):
        self.accounts = accounts
    def uppdate(self):
        for account in self.accounts:
            if isinstance(account,SavingAccount):
                account.add()
                print(f"On your account {account.account_number}.You have {account.balance}")
            elif isinstance(account,CurrentAccount):
                print(f"On your account {account.account_number}.You have overdraft limit {account.overdraft_limit}")
            else:
                print(f"On your account {account.account_number}.You have {account.balance}")
        




class TestAccount(unittest.TestCase):
    def test_account_balance(self):
        account1 = Account(1000,103)
        self.assertEqual(account1.balance, abs(account1.balance))
        self.assertNotEqual(account1.balance,0)
    def test_saving_account(self):
        account2 = SavingAccount(1000,101,25)
        self.assertEqual(account2.balance, abs(account2.balance))
        self.assertNotEqual(account2.balance,0)
        self.assertEqual(account2.interest, abs(account2.interest))
        self.assertNotEqual(account2.interest,0)
    def test_current_account(self):
        account3 = CurrentAccount(1000,102,300)
        self.assertEqual(account3.overdraft_limit, abs(account3.overdraft_limit))


unittest.main()