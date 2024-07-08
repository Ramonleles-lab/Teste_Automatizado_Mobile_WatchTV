
class  Elements_variable ():

    #capabilities
    desired_cap = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "avd": "teste_watch",
    "appPackage": "br.tv.watch.watchbrasil",
    "appActivity": "br.tv.watch.watchbrasil.MainActivity",
    "automationName": "UIAutomator2"
    }

    #Login usuário válido
    botao_entrar = '//android.widget.Button[@text="Entrar"]'
    login_email = '//android.view.View[@resource-id="page"]/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.EditText'
    login_email_valido = "ramon_leles@hotmail.com"
    login_password = '//android.view.View[@resource-id="page"]/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.EditText'
    login_password_valido = "Leles1990"
    Botao_login = '//android.widget.Button[@text="Entrar"]'
    
    #Login usuário com email inválido
    login_email_valor_invalido = "ramon@hotmail.com"
    
    #selecionando perfil de usuário
    Selecionar_perfil = '(//android.widget.Image[@text="orange-app"])[1]'
    
    #Selecionando menu da home page do usuário
    Selecionar_menu = '//android.widget.Image[@text="hamburguer"]'
    
    #icone de lupa para buscar conteúdo
    pesquisar_conteudo = '//android.widget.TextView[@text="Busca"]'
    
    #icone para perfil
    icone_perfil = '//android.widget.TextView[@text="Perfil"]'
    
    # lista de favoritos
    icone_minha_lista = '//android.widget.TextView[@text="Minha Lista"]'
    
    #clicando em conteudo
    selecionar_conteudo_pra_assistir = '//android.widget.Image[@text="1_qngfzpsk"]'