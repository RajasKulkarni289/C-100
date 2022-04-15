class bankAtm(object):
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber

    def balnceEnquiry(self):
        print("Balance Enquiry")
    
    def cashWithdrawl(self):
        print("Cash WithDrawl")

Rajas=bankAtm(123456,654321)
print(Rajas.cardNumber)