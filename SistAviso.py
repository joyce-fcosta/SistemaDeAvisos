from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


page='https://web.whatsapp.com/'


class automation(object):

    driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def __init__(self,page):
        self.page = page
    
    def ReturnDriver(self):
        return self.driver

    def Conection(self):
        self.driver.get(self.page)
        time.sleep(60)

    def Localation_Element(self, String_Road):
        return self.driver.find_element_by_xpath(String_Road)

    def Clik_Item(self, String_Road):
        Element_Xpath = self.Localation_Element(String_Road)
        Element_Xpath.click()
        time.sleep(3)
        

    def Typing(self, String_Road, String_Typing):
        Element_Xpath = self.Localation_Element(String_Road)
        for read in String_Typing:
            Element_Xpath.send_keys(read)
            time.sleep(0.3)

    def GUI_HTML(self, soup):

        #Função do webdrive que copia o codigo da página
        html_page = auto.ReturnDriver().page_source

        #converte em caracter
        soup = BeautifulSoup(html_page, 'html.parser')

        #Estrutura o código HTML 
        return soup.prettify()
     
    def Read_Menssager(self,soup,tag,name_class):
        return soup.find_all(tag,name_class)
        pass
        
        
    

#Main
Element_ = "//div[@title='Caixa de texto de pesquisa']"
group = "Salvar tudo!"

auto = automation(page)
auto.Conection()

#Precisa do elemento no qual vai ser digitado apontado
auto.Clik_Item(Element_)

#Digitando
auto.Typing(Element_, group)

Element_Group = '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/span'
#"//span[@title='Salvar tudo!']"
time.sleep(5)

#Click na conversa desejada
auto.Clik_Item(Element_Group)


try:
    html = auto.GUI_HTML()
    print(html)
except:
    print("Erro, verifica a função Read_Menssager")


#Read_Menssager





