from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.options import Options
import os
# import requests
import time
from datetime import date
import mysql.connector
import pyperclip


#API 
agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

#CHAVE    xgLNUFtZsAbhZZaxkRh5ofM6Z0YIXwwv
with open("api.txt", "r") as file:
     api = file.read()
api = api.split(".n.")
bolinha_notificacao = api[3].strip()
contato_cliente = api[4].strip()
# contato_cliente = "//span[@class='fe5nidar fs7pz031 tl2vja3b e1gr2w1z']"
caixa_msg = api[5].strip()
msg_cliente = api[6].strip()
caixa_msg2 = api[7].strip()
caixa_pesquisa = api[8].strip()


#SALVA SESSAO
dir_path = os.getcwd()
chrome_options2 = webdriver.ChromeOptions()
chrome_options2.add_argument(r"user-data-dir=" + dir_path + "/pasta/sessao")
driver = webdriver.Chrome(chrome_options2)
url = "https://web.whatsapp.com/"
driver.get(url)






#BOT
def bot():
    try:
        
        #CAPTURAR A BOLINHA
        bolinha = driver.find_elements(By.CLASS_NAME,bolinha_notificacao)
        clica_bolinha = bolinha[-1]
        clica_bolinha.click()
        telefone_cliente2 = driver.find_element(By.XPATH, contato_cliente)
        telefone_final2 = telefone_cliente2.text

    
      
        #PEGAR O TELEFONE
        # telefone_cliente = driver.find_element(By.XPATH, contato_cliente)
        # # telefone_cliente2 = driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div/div/div/span')
        # # telefone_final = telefone_cliente.text 
        # telefone_final = telefone_cliente.text
        # print(telefone_final2)
    

        #PEGAR A MSG DO CLIENTE
        todas_as_msg = driver.find_elements(By.CLASS_NAME,msg_cliente)
        todas_as_msg_texto = [e.text for e in todas_as_msg]
        msg = todas_as_msg_texto[-1]
        today_date = date.today()
        act = ActionChains(driver)
        
    


        

        #RESPONDENDO CLIENTE
        def responder_mensagem(resp):
            campo_de_texto = driver.find_element(By.XPATH, caixa_msg)
            pyperclip.copy(resp)
            act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
            campo_de_texto.send_keys(Keys.ENTER)
            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
       
        def send_msg(resp):
            campo_de_texto = driver.find_element(By.XPATH, caixa_msg)
            pyperclip.copy(resp)
            act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
            campo_de_texto.send_keys(Keys.ENTER)
            
        
        
    
     


    ############################R#############################################################################################################
        welcome = """E aí, tudo beleza? Espero que sim 😊
Sou o Rodrigo e estou super empolgado em te ver por aqui!
Que legal que você quer turbinar seu desenvolvimento ainda mais!
🤩🚀📈"""
        info_name = "Para darmos início, me informe o seu nome logo abaixo (em uma única linha):"
        congratulatios = f"É um grande prazer ter você conosco, {msg} 🥰"
        list_options =  f""" Agora, {msg}, *escolha* uma das opções abaixo (_ex: 2_):
1 --> ⚙ Como Funciona
2 --> 💳 Realizar Pagamento
3 --> 🧑‍💻 Falar com Atendente
4 --> ✍ Informar um Curso"""

        option_1 = ", acesse este link e encontre mais informações: "
        option_2 = "Clique no link abaixo e acesso para poder realizar o pagamento:\nrateiosocial.com"
        option_3 = ", aguarde um momento, já iremos  entrar em contato!"
        op_incorreta = f""", *escolha* uma opção correta (_ex: 2_):
1 --> ⚙ Como Funciona
2 --> 💳 Realizar Pagamento
3 --> 🧑‍💻 Falar com Atendente
4 --> ✍ Nos Informe um Curso"""
        info_course = f', agora digite o nome do curso e do autor. Se possível, envie a página venda do produto 😉'

            

    ###########################################################################################################################################

       
     
     # Cria uma conexão com o banco de dados

        conn = mysql.connector.connect(
    host= '173.211.81.11',  
    user= 'ljywsbcn_admin',
    password= '#desenvolvendo2024',
    database= 'ljywsbcn_bot_atendimento',

)
        def insert(phone, status, dateContact):
                cursor.execute("INSERT INTO usuario (userPhone,status,dateContact) VALUES ('{}', '{}', '{}')".format(phone, status, dateContact))
                conn.commit()
      
        def search_name(phone):
            query = "SELECT nameUser FROM usuario WHERE userPhone = '{}' ".format(phone)
            result  =  cursor.execute(query)
            return result

        
        def status(phone, status):
            query = "SELECT * FROM usuario WHERE userPhone = '{}' AND status = '{}'".format(phone, status)
            cursor.execute(query)
            qt_status = len(cursor.fetchall())
            return qt_status
        
        def update_status(status, phone):
            query = "UPDATE usuario SET status = '{}' WHERE userPhone = '{}'".format(status, phone)
            cursor.execute(query)
            conn.commit()

        def date_str_int(dateStr):
                datE = dateStr
                datE2 = datE.replace("-", "")
                year = int(datE2[:4:])
                moth = int(datE2[4:6:])
                day = int(datE2[6:8:])
                data1 = date(year, moth, day)
                data2 = date.today()
                result = (data2 - data1).days
                return result
                
       
        def dateUser(phone):
            query = "SELECT dateContact FROM usuario WHERE userPhone = '{}'".format(phone)
            cursor.execute(query)
            resultCursor = cursor.fetchone()
            strdate = resultCursor[0]
            result = date_str_int(strdate)
            return result
        
        def userName(userName, phone):
               cursor.execute("UPDATE usuario SET nameUser = '{}' WHERE userPhone = '{}'".format(userName, phone))
               conn.commit()

        def search_name(phone):
            query = "SELECT nameUser FROM usuario WHERE userPhone = '{}' ".format(phone)
            cursor.execute(query)
            resultSearch =  cursor.fetchone()
            return resultSearch[0]
             


        cursor = conn.cursor(buffered=True)
        query = "SELECT * FROM usuario WHERE userPhone = '{}'".format(telefone_final2)
        cursor.execute(query)
        total = len(cursor.fetchall())

    

        if total == 0: 
            insert(telefone_final2, 1, today_date)
            send_msg(welcome)
            responder_mensagem(info_name)
        
        if status(telefone_final2, 1):
           userName(msg, telefone_final2)
           send_msg(congratulatios)
           responder_mensagem(list_options)
           update_status(2, telefone_final2)
        
        if status(telefone_final2, 2):
           if msg == "1":
             responder_mensagem(search_name(telefone_final2) + option_1)
           elif msg == "2":
             responder_mensagem("Código pix gerado com sucesso, "+ search_name(telefone_final2) + "!"+ option_2)
           elif msg == "3":
              responder_mensagem(search_name(telefone_final2) + option_3)
              update_status(3, telefone_final2)
           elif msg == "4":
              responder_mensagem(search_name(telefone_final2) + info_course)
              update_status(3, telefone_final2)
               
           else:
            responder_mensagem(search_name(telefone_final2) + op_incorreta)
       
        if dateUser(telefone_final2) == 3:
             update_status(1, telefone_final2)
        

           

     
    
    

    except:
        pass
#entao vou tentar isso aqui 

        


while True:
    bot()
    
   

    

