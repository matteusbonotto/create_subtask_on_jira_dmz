from Assets.importations import By, chrome, sleep
from Assets.functions import WAITAPPEAR
def DROPDOWN_MORE_SUBTASK():
    WAITAPPEAR(10, 'create-subtask')
    chrome.find_element(By.ID, 'create-subtask').click()

def DROPDOWN_MORE():
    WAITAPPEAR(10, 'opsbar-operations_more')
    chrome.find_element(By.ID, 'opsbar-operations_more').click()

def FIELD_ISSUETYPE(key):
    WAITAPPEAR(10, 'issuetype-field')
    chrome.find_element(By.ID, 'issuetype-field').click()
    chrome.find_element(By.ID, 'issuetype-field').send_keys(key)

def FIELD_SUMMARY(key):
    chrome.find_element_by_id('summary').click()
    WAITAPPEAR(10, 'summary')
    chrome.find_element_by_id('summary').send_keys(key)

def FIELD_DESCRIPTION(key):
    WAITAPPEAR(10, 'aui-uid-4')
    chrome.find_element(By.XPATH, '//*[@id="aui-uid-4"]').click()
    chrome.find_element(By.ID, 'description').send_keys(key)

def FIELD_ASSIGNEE(key):
    WAITAPPEAR(10, 'assignee-field')
    chrome.find_element(By.ID, 'assignee-field').click()
    chrome.find_element(By.ID, 'assignee-field').send_keys(key)

def FIELD_PRIORITY(key):
    WAITAPPEAR(10, 'priority-field')
    chrome.find_element(By.ID, 'priority-field').click()
    chrome.find_element(By.ID, 'priority-field').send_keys(key)

# Preenche o campo Labels
def FIELD_LABELS(key):
    WAITAPPEAR(10, 'labels-textarea')
    chrome.find_element(By.ID, 'labels-textarea').click()
    chrome.find_element(By.ID, 'labels-textarea').send_keys(key)

def BUTTON_SUBMIT():
    WAITAPPEAR(10, 'create-issue-submit')
    chrome.find_element(By.ID, 'create-issue-submit').click()
