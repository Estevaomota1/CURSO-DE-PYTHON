# passo a passodo projeto 
#entrar no sistema da empresa 
#baixar pip py auto gui 
#baixe o pandas 2 frameworks importantes para o projeto

import pyautogui

pyautogui.PAUSE = 1 

tabela =pandas.read_csv("produtos.csv")
print tabela

for linha in tabela.index: 

    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")

    pyautogui.white("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
    pyautogui.write(link)
    pyautogui.press("enter")

    time.sleep(3)

    pyautogui.click(x=733, y=455)

    pyautogui.white("estevao.lindo.maravilhoso@gmail.com")

    pyautogui.write("sua senha aqui")

    pyautogui.press("tab")

    pyautogui.press("enter")

    time.sleep(3)

    tabela = pandas.read_csv("produtos.csv")
    #verifique se csv esta funcionando
    print(tabela)

    pyautogui.click(x=756, y=300)
    codigo = tabela.loc[linha,"codigo"]
    codigo = tabela.loc[linha,"Marca"]
    codigo = tabela.loc[linha,"Tipo"]
    codigo = tabela.loc[linha,"Categoria"]
    codigo = tabela.loc[linha,"Preço"]
    codigo = tabela.loc[linha,"Custo"]
    

    OBS = tabela.loc[linha,"OBS"]
    if not pandas.isna(OBS):
              pyautogui.write(link)
       
    








    pyautogui.write(str("Codigo"))
    pyautogui.press("Tab")
    pyautogui.write(str("Marca"))
    pyautogui.press("Tab")
    pyautogui.write(str("Tipo"))
    pyautogui.press("Tab")
    pyautogui.write(str("Categoria"))
    pyautogui.press("Tab")
    pyautogui.write(str("Preço"))
    pyautogui.press("Tab") 
    pyautogui.write(str("Custo"))
    pyautogui.press("Tab") 
    pyautogui.write(str("OBS"))
  
    pyautogui.press("Tab") 
    pyautogui.press("Enter")

pyautogui.scroll(500000)

enviar_e-mail()