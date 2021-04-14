import requests
from bs4 import BeautifulSoup
import smtplib
import email.message

def send_message():
    #Dentro da variavel abaixo, contem o link da pagina, que aparecerá no corpo do email
    email_content = """
        https://www.americanas.com.br/produto/2917267090?pfm_carac=Celulares%20e%20Smartphones&pfm_page=category&pfm_pos=grid&pfm_type=vit_product_grid&cor=AZUL%20CLARO
    """
    msg = email.message.Message()
    msg['subject'] = f'Produto {title} com preço abaixo do normal'
    msg['From'] = 'email@hotmail.com.com'
    msg['To'] = 'Clientemail@hotmail.com'
    password = 'Password'
    msg.add_header('Content_Type', 'text/html')
    msg.set_payload(email_content)

    s = smtplib.SMTP('smtp.outlook.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string())

    print('Email enviado')
    

url = "https://www.americanas.com.br/produto/2917267090?pfm_carac=Celulares%20e%20Smartphones&pfm_page=category&pfm_pos=grid&pfm_type=vit_product_grid&cor=AZUL%20CLARO"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser') # Parser: Analisa a requisição do site e verifica o html

title = soup.find('span', class_ = 'src__Text-sc-154pg0p-0 src__Title-uexifx-0 dItrhU').get_text()
price = soup.find('div', class_ = 'src__BestPrice-sc-1jvw02c-5 cBWOIB priceSales').get_text().strip()

nPrice = price[3:8] #Ignorando os centavos
nPrice = nPrice.replace('.', '') #Retirando o '.' para transformar a string em um float
nPrice = float(nPrice)

if(nPrice < 3999):
    send_message()

#Add task scheduler