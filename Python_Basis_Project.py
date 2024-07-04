class Bank_of_Hacker:
    def __init__(self):
        print("Welcome To Bank_Of_Hacker")
     
     #FUNCTON FOR ACCEPTINNG THE MONEY FROM USER
     
    def Accept_Money_From_User(self,Total_Avilable_Amount):
        amount = int(input("Enter the Amount You Have To Deposit : "))
        #CHECKING WEATHER THE AMOUNT IS GREATER THAN THE MAXIMUM AMOUNT 
        if amount >100000:
            print("You Cannot Deposit This Much Large Amount at One Time")
            
       #IF NOT THEN IT WILL ACCEPT THE MONEY
        else:
           Total_Avilable_Amount[0] +=amount
           print("The Current Avilable Amount in your Account is : " , Total_Avilable_Amount )
    
   

     #FUNCTION FOR WITHDRAWEL AMOUNT FROM YOUR ACCOUNT
    def Withdraw_Amount(self,Total_Avilable_Amount):
        Require_Amount = int(input("Enter the Amount You Have To Be Withdrawn : "))
        #CHECK IF AMOUNT IS AVILABLE IN YOUR ACCOUNT
        if Require_Amount > Total_Avilable_Amount[0] :
            print("You Cannot Withdraw Amount ,Because You Don't Have That Much Of Balance")
        else:
            #PRINT AVILABLE AMOUNT
            print("The Avilable Amount In Your Account Is ",Total_Avilable_Amount[0]-Require_Amount)
      



Total_Avilable_Amount = [10]            
Bank_Object = Bank_of_Hacker()
Bank_Object.Accept_Money_From_User(Total_Avilable_Amount)   
Bank_Object.Withdraw_Amount(Total_Avilable_Amount)        