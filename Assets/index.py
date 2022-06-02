from PySimpleGUI import PySimpleGUI as sg

def popupMessage(text):
    sg.popup(text)

#layout
sg.theme('Reddit')
layout_login = [
    [sg.Text('User')],
    [sg.InputText('', key='user', size=(20, 1))],
    
    [sg.Text('Password')],
    [sg.InputText('', key='password', size=(20, 1), password_char='*')]
]

layout_Task = [
     [sg.Text('import xlsx')], [sg.InputText('us.xlsx', key='file'), sg.FileBrowse()]
]
layout = [
          [sg.Frame('Login Jira DMZ', layout_login, font='Any 12', title_color='blue', size=(800, 150))],
          [sg.Frame('Import issues', layout_Task, font='Any 12', title_color='blue', size=(800, 100))],
          [sg.Button('Run', size=(17, 2))]
         ]
#Janela
viewWindow = sg.Window('[Bot - Create Task]', layout, size=(450, 320))
#Ler os eventos
while True:
    events, values = viewWindow.read()
    user = values['user']
    password = values['password']
    file = values['file']
    if events == sg.WINDOW_CLOSED:
        popupMessage('Bye bye!')
    break
