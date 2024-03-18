#Library Section
from tabulate import tabulate
from termcolor import colored
import os
import time
import re
#Variable Section
CityofJakarta = ('East Jakarta','West Jakarta','Central Jakarta','South Jakarta','North Jakarta','Seribu Islands')
CityofWestJava = ('Bandung','West Bandung','Banjar','Bekasi','Bogor','Ciamis','Cianjur','Cimahi','Cirebon','Depok','Garut','Indramayu','Karawang','Kuningan','Majalengka','Pangandaran','Purwakarta','Subang','Sukabumi','Sumedang','Tasikmalaya')
CityofBanten = ('Tangerang','South Tangerang','Serang','Lebak','Cilegon','Pandeglang')
CityofYogyakarta = ('Sleman','Bantul','Yogyakarta','Gunung Kidul','Kulon Progo')
CityofCentralJava = ('Brebes','Tegal','Cilacap','Purbalingga','Banyumas','Banjarnegara','Wonosobo','Purbalingga','Kebumen','Magelang','Purworejo','Klaten','Wonogiri','Boyolali','Karanganyar','Blora','Grobogan','Sukoharjo','Pati','Rembang','Jepara','Kudus','Demak','Temanggung','Salatiga','Surakarta','Kendal','Batang','Pekalongan','Pemalang','Semarang','Sragen')
CityofEastJava = ('Kediri','Blitar','Malang','Probolinggo','Pasuruan','Mojokerto','Madiun','Surabaya','Batu','Pacitan','Ponorogo','Trenggalek','Tulungagung','Lumajang','Jember','Banyuwangi','Bondowoso','Situbondo','Sidoarjo','Jombang','Nganjuk','Magetan','Ngawi','Bojonegoro','Tuban','Lamongan','Gresik','Bangkalan','Sampang','Pamekasan','Sumenep')
Jakarta = [
    {
        'Organization': 'Marigame Udon',
        'Phone': '628799917629',
        'City': 'East Jakarta',
        'Locality':'Cipinang Melayu',
        'Street Name': 'Kalimalang 40'
    },
    {
        'Organization': 'Siang Malam',
        'Phone': '62869271999',
        'City': 'South Jakarta',
        'Locality': 'Kemang',
        'Street Name': 'Kemang 20'
    },
    {
        'Organization': 'Saratoga Investama Sedaya Tbk',
        'Phone': '6287918909728',
        'City': 'South Jakarta',
        'Locality': 'Setiabudi',
        'Street Name': 'H.R. Rasuna Said X5'
    },
    {
        'Organization': 'Mulanpada Hospital Jakarta',
        'Phone': '62877782917361',
        'City': 'South Jakarta',
        'Locality': 'Lebak Bulus',
        'Street Name': 'Lebak Bulus I Kavling 29'
    }
]
West_Java = [
    {
        'Organization': 'Parahyangan Catholic University',
        'Phone': '6289826182618',
        'City': 'Bandung',
        'Locality': 'Cidadap',
        'Street Name': 'Ciumbuleuit 94'
    },
    {
        'Organization': 'Malah Dicubo',
        'Phone': '6282918193829',
        'City': 'Bandung',
        'Locality': 'Andir',
        'Street Name': 'South Train Station Hall 27'
    },
    {
        'Organization': 'Put Your Hands Up',
        'Phone': '6281123242102',
        'City': 'Bandung',
        'Locality': 'Coblong',
        'Street Name': 'Ir. H. Juanda 113'
    },
    {
        'Organization': 'Santa Baramundi Hospital',
        'Phone': '6282325192719',
        'City': 'Bandung',
        'Locality': 'Coblong',
        'Street Name': 'Ir. H. Juanda 100'
    }
]
Central_Java = [
    {
        'Organization': "Sate Kambing Wendy's",
        'Phone': '62877236271761',
        'City': 'Tegal',
        'Locality': 'Tegal Baru',
        'Street Name': 'Kapten Ismail 5',
    },
    {
        'Organization': 'Doctor Kariadi Public Hospital',
        'Phone': '62827172618271',
        'City': 'Semarang',
        'Locality': 'South Semarang',
        'Street Name': 'DR. Sutomo 16',
    },
    {
        'Organization': 'Diponegoro University',
        'Phone': '6281172637162',
        'City': 'Semarang',
        'Locality': 'Tembalang',
        'Street Name': 'Professor Sudarto 13',
    },
    {
        'Organization': 'Solo Grand Mall',
        'Phone': '62876271682618',
        'City': 'Surakarta',
        'Locality': 'Laweyan',
        'Street Name': 'Slamet Riyadi 273',
    }
]
East_Java = [
    {
        'Organization': 'Pakuwon City Mall',
        'Phone': '6286627261726',
        'City': 'Surabaya',
        'Locality': 'Mulyorejo',
        'Street Name': 'White Laguna KJW Tambak 2',
    },
    {
        'Organization': 'Pondok Pesantren Tebu Ireng',
        'Phone': '6286726182617',
        'City': 'Jombang',
        'Locality': 'Diwek',
        'Street Name': 'Irian Jaya 10',
    },
    {
        'Organization': 'Avian Office Tower',
        'Phone': '628662716271',
        'City': 'Surabaya',
        'Locality': 'Gayungan',
        'Street Name': 'East Menanggal 1',
    },
    {
        'Organization': 'Fraton Body Repair & Painting',
        'Phone': '6287728172812',
        'City': 'Surabaya',
        'Locality': 'Benowo',
        'Street Name': 'Kendung 78',
    }
]
Yogyakarta = [
    {
        'Organization': 'Gadjah Mada University',
        'Phone': '628112736261',
        'City': 'Sleman',
        'Locality': 'Depok',
        'Street Name': 'Bulaksumur Caturnunggal 1',
    },
    {
        'Organization': 'Tentrem Hotel',
        'Phone': '628627162712',
        'City': 'Yogyakarta',
        'Locality': 'Jetis',
        'Street Name': 'Prince Mangkubumi 72A',
    },
    {
        'Organization': 'Beringharjo Traditional Market',
        'Phone': '6282636216271',
        'City': 'Yogyakarta',
        'Locality': 'Gondomanan',
        'Street Name': 'Margo Mulyo 16',
    },
    {
        'Organization': 'Indonesia International Islamic University',
        'Phone': '6285627362712',
        'City': 'Sleman',
        'Locality': 'Ngemplak',
        'Street Name': 'Kaliurang KM. 14,5',
    }
]
Banten = [
    {
        'Organization': 'Purwadhika Digital School',
        'Phone': '6287261726172',
        'City': 'South Tangerang',
        'Locality': 'Cisauk',
        'Street Name': 'BSD Green Office Park 9 - G Floor',
    },
    {
        'Organization': 'Sositi Coffee & Bar',
        'Phone': '6289273827192',
        'City': 'South Tangerang',
        'Locality': 'Pagedangan',
        'Street Name': 'Main Street BSD Foresta Business District 6',
    },
    {
        'Organization': 'Indonesia Convention Exhibition',
        'Phone': '628299127812',
        'City': 'South Tangerang',
        'Locality': 'Pagedangan',
        'Street Name': 'BSD Grand Boulevard 1',
    },
    {
        'Organization': 'Krakatau Steel (Persero) Tbk',
        'Phone': '6281273727172',
        'City': 'Cilegon',
        'Locality': 'Purwakarta',
        'Street Name': 'Cilegon City Industry 5',
    }
]
#Title Section
show_title_jakarta = colored("Nick's Express Special Region of Jakarta Database\n",'green')
show_title_westjava = colored("Nick's Express West Java Database\n",'green')
show_title_centraljava = colored("Nick's Express Central Java Database\n",'green')
show_title_eastjava = colored("Nick's Express East Java Database\n",'green')
show_title_yogyakarta = colored("Nick's Express Special Region of Yogyakarta Database\n",'green')
show_title_banten = colored("Nick's Express Banten Database\n",'green')
add_title_jakarta = colored("===================# Add Data to Jakarta Database #===================","blue")
add_title_westjava = colored("===================# Add Data to West Java Database #===================","blue")
add_title_centraljava = colored("===================# Add Data to Central Java Database #===================","blue")
add_title_eastjava = colored("===================# Add Data to East Java Database #===================","blue")
add_title_yogyakarta = colored("===================# Add Data to Special Region of Yogyakarta Database #===================","blue")
add_title_banten = colored("===================# Add Data to Banten Database #===================","blue")
update_title_jakarta = colored("===================# Update Data in Jakarta Database #===================","blue")
update_title_westjava = colored("===================# Update Data in West Java Database #===================","blue")
update_title_centraljava = colored("===================# Update Data in Central Java Database #===================","blue")
update_title_eastjava = colored("===================# Update Data in East Java Database #===================","blue")
update_title_yogyakarta = colored("===================# Update Data in Special Region of Yogyakarta Database #===================","blue")
update_title_banten = colored("===================# Update Data in Banten Database #===================","blue")
delete_title_jakarta = colored("===================# Delete Data from Jakarta Database #===================","light_red")
delete_title_westjava = colored("===================# Delete Data from West Java Database #===================","light_red")
delete_title_centraljava = colored("===================# Delete Data from Central Java Database #===================","light_red")
delete_title_eastjava = colored("===================# Delete Data from East Java Database #===================","light_red")
delete_title_yogyakarta = colored("===================# Delete Data from Special Region of Yogyakarta Database #===================","light_red")
delete_title_banten = colored("===================# Delete Data from Banten Database #===================","light_red")
#Warning Section
city_warning_jakarta = colored("The city are not in Special Region of Jakarta! Please input city in Special Region of Jakarta.",'yellow')
city_warning_westjava = colored("The city are not in West Java! Please input West Java.",'yellow')
city_warning_centraljava = colored("The city are not in Central Java! Please input city in Central Java.",'yellow')
city_warning_eastjava = colored("The city are not in East Java! Please input city in East Java.",'yellow')
city_warning_yogyakarta = colored("The city are not in Special Region of Yogyakarta! Please input city in Special Region of Yogyakarta.",'yellow')
city_warning_banten = colored("The city are not in Banten! Please input city in Banten.",'yellow')
#Function Section
def greetings():
    os.system('cls')
    time.sleep(0.4)
    print("""
            Welcome to Nick's Express Organization Address Database Chapter Java, Indonesia

            Menu :
            1. Preview Nick's Express Address Database
            2. Change Nick's Express Address Database
            3. Delete Data from Nick's Address Database
            7. Exit
          """)
def categories_choose():
        os.system('cls')
        time.sleep(0.4)
        print("""
            Nick's Express Address Database Sub-Menu #1: Database Category
            Menu :
            1. Special Region of Jakarta
            2. West Java
            3. Central Java
            4. East Java
            5. Special Region of Yogyakarta
            6. Banten  
            0. Back
        """)
def write_data():
     os.system('cls')
     time.sleep(0.4)
     print("""
            What you want to do Sub-Menu #1: Create or update data
            Menu :
            1. Add Data
            2. Update Data
            0. Back
        """)
def back():
        back = input('Back to previous menu type (Y), to main menu type (N): ').capitalize()
        return back
def numbers(input):
    return input.isdigit()
def clean_phone_number(phone):
    clean_phone_numbers = []
    # Remove any non-digit characters
    cleaned_phone_number = re.sub(r'\D', '', phone)
    # Check if the cleaned phone number starts with '62' and has more than 9 digits
    if cleaned_phone_number.startswith('62') and len(cleaned_phone_number) > 9:
        # Remove the '62' prefix
        cleaned_phone_number = cleaned_phone_number[0:]
    elif cleaned_phone_number.startswith('08') and len(cleaned_phone_number) > 9:
        # Remove the '08' prefix
        cleaned_phone_number = '62'+cleaned_phone_number[1:]
    elif cleaned_phone_number.startswith('8') and len(cleaned_phone_number) > 9:
        cleaned_phone_number = '62'+cleaned_phone_number[0:]
    else:
        # If the phone number is invalid, replace it with 'Invalid Number'
        cleaned_phone_number = 'Invalid Number'
    clean_phone_numbers.append(cleaned_phone_number)
    return clean_phone_numbers
def show_data(title, data):
    os.system('cls')
    time.sleep(0.4)
    canvas = data
    if(canvas == Jakarta):
        index_database = [{'Index': 'DKI - '+ str(i+1), **row} for i, row in enumerate(data)]
    elif(canvas == West_Java):
        index_database = [{'Index': 'JABAR - ' + str(i+1), **row} for i, row in enumerate(data)]
    elif(canvas == Central_Java):
        index_database = [{'Index': 'JATENG - ' + str(i+1), **row} for i, row in enumerate(data)]
    elif(canvas == East_Java):
        index_database = [{'Index': 'JATIM - ' + str(i+1), **row} for i, row in enumerate(data)]
    elif(canvas == Yogyakarta):
        index_database = [{'Index': 'YK - ' + str(i+1), **row} for i, row in enumerate(data)]
    elif(canvas == Banten):
        index_database = [{'Index': 'A - ' + str(i+1), **row} for i, row in enumerate(data)]
    else:
        index_database = data
    index_database = (tabulate(index_database,headers= 'keys', tablefmt= 'github'))
    print(title)
    print(index_database)
    return
def new_data(title1, title2, data, town, city_warning):
    print(title1)
    time.sleep(1.5)
    show_data(title2, data)
    while True:
        new_organization = input('Organization Name : ').title()
        if(new_organization in [row['Organization'] for row in data]):
            print(colored(f'The {new_organization} information is already in database.','yellow'))
            continue
        new_phone_number = clean_phone_number(input('Organization Phone Number : '))
        while new_phone_number[0] == 'Invalid Number':
            print(colored('Invalid phone number! Please input the right phone number.','red'))
            new_phone_number = clean_phone_number(input('Organization Phone Number : '))
        city = input("City : ").title()
        while city not in town:
            print(city_warning)
            city = input("City : ").title()
        new_locality = input("Locality : ").title()
        new_street_name = input('Street Address : ').title()
        check = input('Are you sure to input this data (Y/N)? : ').capitalize()
        while check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.", 'red'))
            check = input('Are you sure to input this data (Y/N)?: ').capitalize()
        if(check == 'Y'):
            fresh_data = {
            'Organization': new_organization,
            'Phone': new_phone_number[0],
            'City': city,
            'Locality': new_locality,
            'Street Name': new_street_name
            }
            data.append(fresh_data)
            print(colored(f"{new_organization} succesfully added.", 'green'))
            time.sleep(1.0)
            show_data(title2, data)
        else:
            print(colored(f"Information of {new_organization} isn't added to databases.", 'red'))
            time.sleep(1.0)
            show_data(title2, data)
        double_check = str(input("Add another data (Y/N)? : ")).capitalize()
        while double_check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.",'red'))
            continue
        if(double_check == 'Y'):
            continue
        else:
            break
    return
def update_data(title1, title2, data):
    print(title1)
    show_data(title2, data)
    while True:
        upd_index = input('Put Number Index of The Data You Want to Update. Type 0 to Abort The Process : ')
        if not numbers(upd_index):
            print(colored("Just Input Number! Please Input Again",'yellow'))
            time.sleep(1.0)
            continue
        update_index = int(upd_index)
        if((update_index-1) > len(data) or update_index < 0):
            print(colored(f"The Data with Index {update_index} doesn't exsist on",'red') + f' The {title2}')
            time.sleep(0.4)
            continue
        elif(update_index == 0):
            break
        else:
            update_phone = clean_phone_number(input(f"{data[update_index - 1]['Organization']} New Phone Number : "))
            while update_phone[0] == 'Invalid Number':
                print(colored('Invalid phone number! Please input the right phone number.','red'))
                update_phone = clean_phone_number(input(f"{data[update_index - 1]['Organization']} New Phone Number : "))
            update_locality = input(f"{data[update_index - 1]['Organization']} New Locality : ").title()
            update_street_name = input(f"{data[update_index - 1]['Organization']} New Street Address : ").title()
            check = input(f"Are you sure to update {data[update_index - 1]['Organization']} data (Y/N)?: ").capitalize()
            while check not in ['Y', 'N']:
                print(colored("Invalid function! Just type Y or N.", 'red'))
                check = input(f"Are you sure to update {data[update_index - 1]['Organization']} data (Y/N)?: ").capitalize()
            if(check == 'Y'):
                data[update_index -1]['Phone'] = update_phone[0]
                if(update_locality == ''):
                    data[update_index -1]['Locality'] = data[update_index -1]['Locality']
                else:
                    data[update_index -1]['Locality'] = update_locality
                if(update_street_name == ''):
                    data[update_index -1]['Street Name'] = data[update_index -1]['Street Name']
                else:
                    data[update_index -1]['Street Name'] = update_street_name
                print(colored(f"Information of {data[update_index -1]['Organization']} is succesfully updated.", 'green'))
                time.sleep(1.0)
                show_data(title2, data)
            else:
                print(colored(f"Information of {data[update_index -1]['Organization']} isn't updated.", 'red'))
                show_data(title2, data)
        double_check = input("Update another data (Y/N)? : ").capitalize()
        while double_check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.",'red'))
            double_check = input("Update another data (Y/N)? : ").capitalize()
        if(double_check == 'Y'):
            continue
        else:
            break
    return
def remove_data(title1, title2, data):
    print(title1)
    show_data(title2, data)
    while True:
        del_index = input('Put Index Number of The Data You Want to Delete or Type 0 to Abort The Process: ')
        if not numbers(del_index):
            print(colored("Just input Number! Please Input Again",'yellow'))
            time.sleep(1.0)
            continue
        delete_index = int(del_index)
        if (delete_index > len(data) or delete_index < 0):
            print(colored(f"The Data with Index {delete_index} doesn't exsist on",'red') + f' The {title2}')
        elif(delete_index == 0):
            break
        else:
            check = input(f"Are you sure to delete {data[delete_index-1]['Organization']} (Y/N)?: ").capitalize()
            while check not in ['Y', 'N']:
                print(colored("Invalid function! Just type Y or N.", 'red'))
                check = input(f"Are you sure to delete {data[delete_index-1]['Organization']} (Y/N)?: ").capitalize()
            if(check == 'Y'):
                del data[delete_index-1]
                print(colored("Data succesfully deleted.",'red'))
                time.sleep(1.0)
                show_data(title2, data)
            else:
                print(colored(f"Data {data[delete_index -1]['Organization']} unsuccessful deleted.", 'yellow'))
                time.sleep(1.0)
                show_data(title2, data)
        double_check = input("Delete another data (Y/N)? : ").capitalize()
        while double_check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.",'red'))
            double_check = str(input("Add another data (Y/N)? : ")).capitalize()
        if(double_check == 'Y'):
            continue
        else:
            break
#Main Program
while True:
    greetings()
    input_menu = input('Enter Menu you want : ')
    if(not numbers(input_menu)):
        print(colored("Just input Number! Please input again.",'red'))
        time.sleep(1.0)
        continue
    menu = int(input_menu)
    if(menu == 1):
        while True:
            categories_choose()
            time.sleep(0.3)
            input_categories = input('Enter Menu you want : ')
            if(not numbers(input_categories)):
                print(colored("Just input Number! Please input again.",'red'))
                time.sleep(1.0)
                continue
            categories = int(input_categories)
            if(categories == 1):
                print(show_title_jakarta)
                time.sleep(1.0)
                show_data(show_title_jakarta, Jakarta)
            elif(categories == 2):
                print(show_title_westjava)
                time.sleep(1.0)
                show_data(show_title_westjava, West_Java)
            elif(categories == 3):
                print(show_title_centraljava)
                time.sleep(1.0)
                show_data(show_title_centraljava, Central_Java)
            elif(categories == 4):
                print(show_title_eastjava)
                time.sleep(1.0)
                show_data(show_title_eastjava, East_Java)
            elif(categories == 5):
                print(show_title_yogyakarta)
                time.sleep(1.0)
                show_data(show_title_yogyakarta, Yogyakarta)
            elif(input_categories == 6):
                print(show_title_banten)
                time.sleep(1.0)
                show_data(show_title_banten, Banten)
            elif(input_categories == 0):
                break
            else:
                print(colored("Invalid function, please input again!", 'red'))
                time.sleep(1.0)
                continue
            toTheMoon = back()
            while toTheMoon not in ['Y', 'N']:
                print(colored("Invalid function! Just type Y or N.",'red'))
                toTheMoon = back()
            if(toTheMoon == 'Y'):
                continue
            else:
                break
    elif(menu == 2):
        while True:
            write_data()
            time.sleep(0.4)
            input_write_menu = input('Enter Menu you want : ')
            if(not numbers(input_write_menu)):
                print(colored("Just input Number! Please input again.",'red'))
                time.sleep(1.0)
                continue
            write_menu = int(input_write_menu)
            if(write_menu == 1):
                while True:
                    categories_choose()
                    time.sleep(0.4)
                    input_categories = input('Enter Categories : ')
                    if(not numbers(input_categories)):
                        print(colored("Just input Number! Please input again.",'red'))
                        time.sleep(1.0)
                        continue
                    categories = int(input_categories)
                    if(categories == 1):
                        new_data(add_title_jakarta, show_title_jakarta, Jakarta, CityofJakarta, city_warning_jakarta)
                        break
                    elif(categories == 2):
                        new_data(add_title_westjava, show_title_westjava, West_Java, CityofWestJava, city_warning_westjava)
                        break
                    elif(categories == 3):
                        new_data(add_title_centraljava, show_title_centraljava, Central_Java, CityofCentralJava, city_warning_centraljava)
                        break
                    elif(categories == 4):
                        new_data(add_title_eastjava, show_title_eastjava, East_Java, CityofEastJava, city_warning_eastjava)
                        break
                    elif(categories == 5):
                        new_data(add_title_yogyakarta, show_title_yogyakarta, Yogyakarta, CityofYogyakarta, city_warning_yogyakarta)
                        break
                    elif(categories == 6):
                        new_data(add_title_banten, show_title_banten, Banten, CityofBanten, city_warning_banten)
                        break
                    elif(categories == 0):
                        break
                    else:
                        print(colored("Function not found. Please input again!",'red'))
                        time.sleep(1.0)
            elif(write_menu == 2):
                while True:
                    categories_choose()
                    time.sleep(0.4)
                    input_categories = input('Enter Categories : ')
                    if(not numbers(input_categories)):
                        print(colored("Just input Number! Please input again.",'red'))
                        time.sleep(1.0)
                        continue
                    categories = int(input_categories)
                    if(categories == 1):
                        update_data(update_title_jakarta, show_title_jakarta, Jakarta)
                        time.sleep(1.5)
                        break
                    elif(categories == 2):
                        update_data(update_title_westjava, show_title_westjava, West_Java)
                        time.sleep(1.5)
                        break
                    elif(categories == 3):
                        update_data(update_title_centraljava, show_title_centraljava, Central_Java)
                        time.sleep(1.5)
                        break
                    elif(categories == 4):
                        update_data(update_title_eastjava, show_title_eastjava, East_Java)
                        time.sleep(1.5)
                        break
                    elif(categories == 5):
                        update_data(update_title_yogyakarta, show_title_yogyakarta, Yogyakarta)
                        time.sleep(1.5)
                        break
                    elif(categories == 6):
                        update_data(update_title_banten, show_title_banten, Banten)
                        time.sleep(1.5)
                        break
                    elif(categories == 0):
                        break
                    else:
                        print(colored("Function not found. Please input again!",'red'))
                        time.sleep(1.0)
            elif(write_menu == 0):
                break
            else:
                print(colored("Invalid function, please input again!", 'red'))
                time.sleep(1.0)
                continue
            toTheMoon = back()
            while toTheMoon not in ['Y', 'N']:
                print(colored("Invalid function! Just type Y or N.",'red'))
                toTheMoon = back()
            if(toTheMoon == 'Y'):
                time.sleep(0.4)
                continue
            else:
                break
    elif(menu == 3):
        while True:
            categories_choose()
            time.sleep(0.4)
            input_categories = input('Enter Category You Want to Delete: ')
            if(input_categories == '1'):
                remove_data(delete_title_jakarta, show_title_jakarta, Jakarta)
                time.sleep(1.5)
                break
            elif(input_categories == '2'):
                remove_data(delete_title_westjava, show_title_westjava, West_Java)
                time.sleep(1.5)
                break
            elif(input_categories == '3'):
                remove_data(delete_title_centraljava, show_title_centraljava, Central_Java)
                time.sleep(1.5)
                break
            elif(input_categories == '4'):
                remove_data(delete_title_eastjava, show_title_eastjava, East_Java)
                time.sleep(1.5)
                break
            elif(input_categories == '5'):
                remove_data(delete_title_yogyakarta, show_title_yogyakarta, Yogyakarta)
                time.sleep(1.5)
                break
            elif(input_categories == '6'):
                remove_data(delete_title_banten, show_title_banten, Banten)
                time.sleep(1.5)
                break
            elif(input_categories == '0'):
                break
            else:
                print(colored("Function not found. Please input again!",'red'))
                time.sleep(1.0)
            toTheMoon = back()
            while toTheMoon not in ['Y', 'N']:
                print(colored("Invalid function! Just type Y or N.",'red'))
                toTheMoon = back()
            if(toTheMoon == 'Y'):
                time.sleep(0.4)
                continue
            else:
                break
    elif(menu == 7):
        exit()
    else:
        print(colored("Function not found. Please input again!",'red'))
        time.sleep(1.0)