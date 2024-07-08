from appium import webdriver
from appium.options.android import UiAutomator2Options
from typing import Any, Dict  
from Environments import*
from Elements import*
from AssertsByGroups import*
from AssertDefinitions_Pipeline import*
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

def teste_selecionar_conteudo_pra_assistir(environment_app):
        
        #Start_test
        
        #login com email e senha do usuário credenciado
        Login_user()
        
        #clicando em conteudo na homepage para assistir
        selecionar_conteudo_pra_assistir()
        
        #Quit_test
        quit_app()

        #End_test