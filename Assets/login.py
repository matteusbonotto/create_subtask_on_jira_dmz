from Assets.importations import chrome, url_site
from Assets.index import user, password

chrome.get(url_site)

field_user_name = 'os_username'
field_password_name = 'os_password'
button_login_name = "login"

#Elementos da tela 
field_user = chrome.find_element_by_name(field_user_name)
field_pass = chrome.find_element_by_name(field_password_name)
button_login = chrome.find_element_by_name(button_login_name)

#Execução
def LOGAR():
    field_user.send_keys(user)
    field_pass.send_keys(password)
    button_login.click()

