from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self,name,email,nid):
        self.name=name
        self.email=email
        self.nid=nid
        self.wallet=0
        
    @abstractmethod
    def display_profile(self):
        raise NotImplemented
    
class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_amount):
        super().__init__(name, email, nid)
        self.current_ride = None
        self.wallet = initial_amount
        self.current_location = current_location
    
    def display_profile(self):
        print(f"Rider: {self.name} and Email: {self.email}")
        
    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
        else:
            print(f"Amount less than 0")