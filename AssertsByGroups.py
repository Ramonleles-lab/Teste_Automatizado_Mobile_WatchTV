from appium import webdriver
from appium.options.android import UiAutomator2Options
from typing import Any, Dict  
from Environments import*
from Elements import*
from AssertDefinitions_Pipeline import*
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def Login_user():
    click_by_xpath(Elements_variable.botao_entrar)
    send_keys(Elements_variable.login_email,Elements_variable.login_email_valido)
    send_keys(Elements_variable.login_password,Elements_variable.login_password_valido)
    click_by_xpath(Elements_variable.Botao_login)

def Login_user_invalido():
    click_by_xpath(Elements_variable.botao_entrar)
    send_keys(Elements_variable.login_email,Elements_variable.login_email_valor_invalido)
    send_keys(Elements_variable.login_password,Elements_variable.login_password_valido)
    click_by_xpath(Elements_variable.Botao_login)

def selecionar_menu():
    click_by_xpath(Elements_variable.Selecionar_perfil)
    click_by_xpath(Elements_variable.Selecionar_menu)

def selecionar_meninha_lista():
    click_by_xpath(Elements_variable.Selecionar_perfil)
    click_by_xpath(Elements_variable.Selecionar_menu)
    click_by_xpath(Elements_variable.icone_minha_lista)

def selecionar_conteudo_pra_assistir():
    click_by_xpath(Elements_variable.Selecionar_perfil)
    click_by_xpath(Elements_variable.selecionar_conteudo_pra_assistir)