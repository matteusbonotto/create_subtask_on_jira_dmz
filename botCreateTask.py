from multiprocessing.connection import wait
from time import sleep
from Assets.importations import pd
from Assets.functions import ACCESSUS, WAITAPPEAR
from Assets.elements import *
from Assets.index import file, popupMessage
from Assets.login import LOGAR

df = pd.read_excel(file)
LOGAR()
for i, row in df.iterrows():
    US = row["US"]
    issuetype = row['Issue Type']
    ACCESSUS(US)

    if (issuetype == "Task"):
        DROPDOWN_MORE()
        DROPDOWN_MORE_SUBTASK()        
        FIELD_ISSUETYPE(row['Issue Type'])
        FIELD_SUMMARY(row['Summary'])
        FIELD_DESCRIPTION(row['Description'])   # Preenche o campo Description
        FIELD_ASSIGNEE(row['Assignee'])         # Preenche o campo Assignee
        FIELD_PRIORITY(row['Priority'])
        FIELD_LABELS(row['Labels'])
        # BUTTON_SUBMIT()
        WAITAPPEAR(10, 'opsbar-operations_more')

    if (issuetype == "Sub-task"):
        DROPDOWN_MORE()
        DROPDOWN_MORE_SUBTASK()    
        FIELD_ISSUETYPE(row['Issue Type'])
        FIELD_SUMMARY(row['Summary'])
        FIELD_DESCRIPTION(row['Description'])   # Preenche o campo Description
        FIELD_ASSIGNEE(row['Assignee'])         # Preenche o campo Assignee
        FIELD_PRIORITY(row['Priority'])
        FIELD_LABELS(row['Labels'])
        # BUTTON_SUBMIT()
        WAITAPPEAR(10, 'opsbar-operations_more')
popupMessage('Done!')
