import requests
import json
import pprint
import tkinter
import customtkinter
import os.path
import webbrowser
import sys

customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("green")



# print(os.path.exists("api_key.txt"))

def where_api_def():
    webbrowser.open("https://checko.ru/sign-up")



    

def save_api_key():
    if len(message.get()) < 8:
        label_error = customtkinter.CTkLabel(window, text="Неверный API").place(x = 260, y = 180)
    else:
        label_success = customtkinter.CTkLabel(window, text="API успешно сохранен").place(x = 230, y = 180)
        global answer_api
        answer_api = message.get()
        with open("api_key.txt", "w") as file:
            file.write(answer_api)
        file_api = open("api_key.txt", "r").readline()
        # print(file_api)

def get_info_shortly():
    get_inn = message2.get()
    if os.path.exists("api_key.txt"):
        if len(get_inn) > 5:
            answer_api2 = open('api_key.txt', 'r').readline()

            url = f"https://api.checko.ru/v2/company?key={answer_api2}&inn={get_inn}"

            response = requests.get(url=url).json()

            inn = response['data']['ИНН']
            NaimPoln = response['data']['НаимПолн']
            NasPunkt = response['data']['ЮрАдрес']['НасПункт']
            AdressRF = response['data']['ЮрАдрес']['АдресРФ']
            okved_naim = response['data']['ОКВЭД']['Наим']
            contacts = response['data']['Контакты']
            schr = response['data']['СЧР']
            first_phone_number = response['data']['Контакты']['Тел']
            emails = response['data']['Контакты']['Емэйл']
            website_of_the_company = response['data']['Контакты']['ВебСайт']

            with open(f"info_{get_inn}.txt", "w", encoding='utf-8') as file:
                file.write(f"ИНН: {inn}\n")
                file.write(f"НаимПолн: {NaimPoln}\n")
                file.write(f"НасПункт: {NasPunkt}\n")
                file.write(f"АдресРФ: {AdressRF}\n")
                file.write(f"ОКВЭД(Наим): {okved_naim}\n")
                file.write(f"СЧР: {schr}\n")
                # file.write(f"Первый номер телефона: {first_phone_number[0]}\n")
                file.write(f"\nВсе номера телефона: {first_phone_number}")
                file.write(f"\nEmails: {emails}")
                file.write(f"\nWebsite: {website_of_the_company}")

            label_success_get_info = customtkinter.CTkLabel(window, text="Файл с информацией сохранен в текущею директорию").place(x = 150, y = 425)
        else:
            
            label_error_get_info = customtkinter.CTkLabel(window, text="Неверный ИНН").place(x = 250, y = 425)
    else:
        label_error_get_info2 = customtkinter.CTkLabel(window, text="Вы не указали API ключ").place(x = 225, y = 425)

def get_full_info():
    get_inn2 = message2.get()
    if os.path.exists("api_key.txt"):
        if len(get_inn2) > 5:
                
                answer_api4 = open('api_key.txt', 'r').readline()
                
                

                url = f"https://api.checko.ru/v2/company?key={answer_api4}&inn={get_inn2}"

                response = requests.get(url=url)
        
                

                with open(f"info_{get_inn2}.json", "w", encoding='utf-8') as file:
                    json.dump(response.json(), file, ensure_ascii=False, sort_keys=True, indent=4)

                label_success_get_info = customtkinter.CTkLabel(window, text="Файл с информацией сохранен в текущею директорию").place(x = 150, y = 425)

                
                # show_log = customtkinter.CTkButton(window, text="Посмотреть лог").place(x = 225, y = 450)

        else:
            label_error_get_info = customtkinter.CTkLabel(window, text="Неверный ИНН").place(x = 250, y = 425)
    else:
        label_error_get_info2 = customtkinter.CTkLabel(window, text="Вы не указали API ключ").place(x = 225, y = 425)


window = customtkinter.CTk()
window.title("Узнать о компании по ИНН")
window.geometry('600x600')

message = tkinter.StringVar()
message2 = tkinter.StringVar()

ask_api = customtkinter.CTkLabel(window, text="Введите свой API ключ: ", width=150).place(x = 230, y = 25)
submit_api = customtkinter.CTkButton(window, text="Сохранить API", command=save_api_key).place(x = 230, y = 110)
where_api = customtkinter.CTkButton(window, text="Где получить API", command=where_api_def).place(x = 230, y = 150)
try:
    answer_api3 = open('api_key.txt', 'r').readline()
    api_entry = customtkinter.CTkEntry(window, width=200, textvariable=message, justify='center')
    api_entry.insert(0, f"{answer_api3}")
except:
    api_entry = customtkinter.CTkEntry(window, width=200, textvariable=message, justify='center')

    

api_entry.place(x = 205, y = 70)

ask_inn = customtkinter.CTkLabel(window, text="Напишите ИНН компании о которой хотите узнать: ").place(x = 160, y = 250)

entry_count = customtkinter.CTkEntry(window, width=200, textvariable=message2, justify='center')
know_about_company_shortly = customtkinter.CTkButton(window, text="Узнать кратко", command=get_info_shortly).place(x = 230, y = 350)
know_about_company_completly = customtkinter.CTkButton(window, text="Узнать полностью", command=get_full_info).place(x = 230, y = 390)

entry_count.place(x = 205, y = 300)



window.mainloop()







