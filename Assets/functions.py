from Assets.importations import By, chrome, EC, WebDriverWait

def WAITAPPEAR(time, element):
    WebDriverWait(chrome, time).until(EC.element_to_be_clickable((By.ID, element)))

def ACCESSUS(us):
    url_site = "http://dmz-5.dmz.org.br:8080/browse/" + us
    print(url_site)
    chrome.get(url_site)

