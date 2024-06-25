import phonenumbers
from phonenumbers import timezone, geocoder, carrier

def get_info(data):
    
    phoneNumber = phonenumbers.parse(data, 'GB') # Parsing String to Phone number 
     
    timeZone = timezone.time_zones_for_number(phoneNumber) # Pass the parsed phone number in below function

    Carrier = carrier.name_for_number(phoneNumber, 'en') # Getting carrier of a phone number
 
    Region = geocoder.description_for_number(phoneNumber, 'en') # Getting region information
    
    information = f"\nThe phone number: {phoneNumber}\nTimezone: {timeZone}\nCarrier: {Carrier}\nRegion: {Region}\n\n"
    
    return  information

if __name__ =="__main__":
    number = input("\nEnter your phone number starting with the country code: ")
    print(get_info(number))