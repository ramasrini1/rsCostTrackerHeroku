import os
from venmo_api import Client

class Venmo:
    def __init__(self, access_token):
        self.client = Client(access_token=access_token)

    def get_user_id_by_username(self, username):
        print(f"username is {username}")
       
        user = self.client.user.get_user(username)
        if (user):
            return user.id
        else:
            print("ERROR: user did not comeback. Check username.")
            return None

    def request_money(self, amount, message, user_id):
        # Returns a boolean: true if successfully requested
        success = self.client.payment.request_money(amount, message, user_id)
        return success

    def send_money( self, payment_amount, payment_note, payee_id):
        #Get funding source id
        payment_methods = self.client.payment.get_payment_methods()
        
        for pm in payment_methods:
            funding_source_id = pm._json['id']

        # Returns a boolean: true if successfully requested
        success = self.client.payment.send_money(
                        payment_amount, 
                        payment_note, payee_id,
                        funding_source_id=funding_source_id)
       
        return success
    

