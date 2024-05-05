'''
Currency Converter
-------------------------------------------------------------
pip install requests
'''

import requests

def convert_currency():
   init_currency = input('Enter an initial currency (instert symbol like USD,EUR,GBP): ')
   target_currency = input('Enter a target currency (instert symbol like USD,EUR,GBP): ')

   while True:
       try:
           amount = float(input('Enter the amount: '))
       except:
           print('The amount must be a numeric value!')
           continue

       if not amount > 0:
           print('The amount must be greater than 0')
           continue
       else:
           break

   url = ('https://api.apilayer.com/fixer/convert?to='
          + target_currency + '&from=' + init_currency +
          '&amount=' + str(amount))
   
   #print ("url call: "+url)
   payload = {}
   # look for your personal API at apilayer
   headers = {'apikey': '<INSERT API>'}
   response = requests.request('GET', url, headers=headers, data=payload)
   status_code = response.status_code

   if status_code != 200:
       print('Uh oh, there was a problem. Please try again later')
       quit()

   result = response.json()
   #print(result)
   print('Conversion result: ' + str(amount) +' '+ str(init_currency) +' are '
         + str(result['result']) +' '+ str(target_currency))


if __name__ == '__main__':
   convert_currency()