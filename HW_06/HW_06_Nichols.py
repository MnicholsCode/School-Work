import numpy as np

class LinReg:
    
    def __init__(self, x, y):
        #Convert x,y to arrays if list is provided
        self.x = np.array(x)
        self.y = np.array(y)

        avg_x = np.mean(self.x)
        avg_y = np.mean(self.y)
        
        sxx = np.sum((self.x-avg_x)**2) 
        sxy = np.sum((self.x-avg_x) * (self.y - avg_y))
            
        self.b1 = sxy / sxx
        self.b0 = avg_y - self.b1 * avg_x
        
    def display_model(self):
        print(f'Intercept: {self.b0}')
        print(f'Slope:     {self.b1}')
        
    def predict(self, x):
        self.x = np.array(x)
        pred_y_values = self.x * self.b1 + self.b0
        return pred_y_values
    
    def score(self, x, y):
        pred_y_values = self.predict(x)
        errors = np.sum(y - pred_y_values)
        sse = np.sum(errors ** 2)
        sst = np.sum(y - np.mean(self.y) ** 2 )
        r2 = 1 - sse / sst
        return r2

class ATM:
    
    def __init__(self, first, last, balance):
        self.first = first
        self.last = last
        self.balance = balance
    
    def __check_balance__(self):
        print(f'Hello, {self.first}. Your current balance is: ${self.balance}')
    
    def __deposit__(self, amount):
        self.balance += amount
        print(f'Deposit of ${amount} complete.')
        
    def __withdrawal__(self, amount):
        if self.balance < amount:
            print(f'Withdrawal of ${amount} failed. Insufficient funds.')
        else:
            self.balance -= amount
            print(f'Withdrawal of ${amount} complete.')