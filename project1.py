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
        account1 = Account(-1000,103)
        account2 = Account(0,103)
        account3 = Account(-1000,103)
        list_ = [account1,account2,account3]
        for account in list_:
            self.assertEqual(account.balance, abs(account.balance))
    def test_saving_account(self):
        account1 = SavingAccount(1000,103,25)
        account2 = SavingAccount(1000,103,0)
        account3 = SavingAccount(1000,103,-10)
        list_ = [account1,account2,account3]
        for account in list_:
            self.assertEqual(account.balance, abs(account.balance))
            self.assertNotEqual(account.balance,0)
            self.assertEqual(account.interest, abs(account.interest))
            self.assertNotEqual(account.interest,0)
    def test_current_account(self):
        account1 = CurrentAccount(1000,102,300)
        account2 = CurrentAccount(1000,102,-300)
        list_ = [account1,account2]
        for account in list_:
            self.assertEqual(account.overdraft_limit, abs(account.overdraft_limit))
    def test_update(self):
        a = SavingAccount(1000,101,25)
        b = CurrentAccount(1000,102,300)
        c = Account(1000,103)
        banks = Bank([a,b,c])
        banks.uppdate([a,b,c])
        self.assertIsNone(banks.uppdate())

unittest.main()
