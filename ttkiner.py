import tkinter
from tkinter import ttk, Tk, PhotoImage, Label, Image, Button
from requests import get,put,post,delete
from requests_futures.sessions import FuturesSession
from threading import Thread
from functools import partial
from datetime import datetime
from json import loads


powerState1,powerState2,powerState3,powerState4 = False,False,False,False
url_hexa = "http://34.225.222.91:5000/SMARTERICSSON0001/"


liga19 = 'relay_action/19/1/'
desliga19 = 'relay_action/19/2/'
liga20 = 'relay_action/20/1/'
desliga20 = 'relay_action/20/2/'
liga21 = 'relay_action/21/1/'
desliga21 = 'relay_action/21/2/'
liga22 = 'relay_action/22/1/'
desliga22 = 'relay_action/22/2/'

metodos = {
    'relay_action':[0,1],
    'get_modules' : 'get_modules/',
    'get_available_modules' : 'get_available_modules/',
    'get_actuations' : 'get_actuations/',
    'relay_action' : 'relay_action/',
    'insert_actuation' : 'insert_actuation/',
    'insert_actuation_exception' : 'insert_actuation_exception/',
    'update_actuation' : 'update_actuation/',
    'delete_actuation' : 'delete_actuation/',
    'delete_actuation_exception' : 'delete_actuation_exception/',
    'insert_circuit' : 'insert_circuit/',
    'get_circuits' : 'get_circuits/',
    'get_circuit_measures_by_date' : 'get_circuit_measures_by_date/',
    'get_circuits_measure_between_dates' : 'get_circuits_measures_between_dates/',
    'get_instant_circuit_measures_by_date' : 'get_instant_circuit_measures_by_date/',
    'get_instant_circuit_measures_between_dates' : 'get_instant_circuit_measures_between_dates/',
    'get_break_panel_energys_by_date' : 'get_break_panel_energys_by_date/',
    'get_break_panel_energys_between_dates': 'get_break_panel_energys_between_dates/',
    'get_instant_break_panel_energys_by_date' : 'get_instant_break_panel_energys_by_date/',
    'get_instant_break_panel_energys_between_dates' : 'get_instant_break_panel_energys_between_dates/',
    'delete_circuit' : 'delete_circuit/'
}

def startThread(labelId):
        process = Thread(target=attLabel(labelId))
        process.start()


def attLabel(labelId):
    global powerState1,powerState2,powerState3,powerState4
    if labelId == 'lbl1' and powerState1 == False:
        powerState1 = not powerState1
        resp=put(url_hexa+liga19)
        resp.raise_for_status()
        print(resp.status_code)
        if resp.status_code !=200:
            lbl1['text'] = 'Problemas na solicitação...'
        else:
            lbl1['text'] = 'Ligado!'

    elif labelId == 'lbl1' and powerState1 == True:
        resp = put(url_hexa + desliga19)
        powerState1 = not powerState1
        if resp.status_code != 200:
            lbl1['text'] = 'Problemas na solicitação...'
        else:
            lbl1['text'] = 'Desligado!'

    elif labelId == 'lbl2' and powerState2 == False:
        powerState2 = not powerState2
        resp = put(url_hexa + liga20)
        resp.raise_for_status()
        print(resp.status_code)
        if resp.status_code != 200:
            lbl3['text'] = 'Problemas na solicitação...'
        else:
            lbl3['text'] = 'Ligado!'
    elif labelId == 'lbl2' and powerState2 == True:
        resp = put(url_hexa + desliga20)
        powerState2 = not powerState2
        if resp.status_code != 200:
            lbl3['text'] = 'Problemas na solicitação...'
        else:
            lbl3['text'] = 'Desligado!'
    elif labelId == 'lbl3' and powerState3 == False:
        powerState3 = not powerState3
        resp = put(url_hexa + liga21)
        resp.raise_for_status()
        print(resp.status_code)
        if resp.status_code != 200:
            lbl2['text'] = 'Problemas na solicitação...'
        else:
            lbl2['text'] = 'Ligado!'
    elif labelId == 'lbl3' and powerState3 == True:
        resp = put(url_hexa + desliga21)
        powerState3 = not powerState3
        if resp.status_code != 200:
            lbl2['text'] = 'Problemas na solicitação...'
        else:
            lbl2['text'] = 'Desligado!'
    elif labelId == 'lbl4' and powerState4 == False:
        powerState4 = not powerState4
        resp = put(url_hexa + liga22)
        resp.raise_for_status()
        print(resp.status_code)
        if resp.status_code != 200:
            lbl4['text'] = 'Problemas na solicitação...'
        else:
            if lbl4['text'] == 'Ligado!':
                lbl4['text'] = 'Desligado'
            else:
                lbl4['text'] = 'Ligado!'
    elif labelId == 'lbl4' and powerState4 == True:
        resp = put(url_hexa + desliga21)
        powerState4 = not powerState4
        if resp.status_code != 200:
            lbl4['text'] = 'Problemas na solicitação...'
        else:
            if lbl4['text'] == 'Desligado!':
                lbl4['text'] = 'Ligado'
            else:
                lbl4['text'] = 'Desligado'
    elif labelId == 'lbl5':
        nowS = datetime.now().strftime("%S")
        if int(nowS) <30:
            now = datetime.now().strftime("%Y-%m-%d_%H:%M:00")
        elif int(nowS)>= 30:
            now = datetime.now().strftime("%Y-%m-%d_%H:%M:30")
        resp = get('http://34.225.222.91:5000/SMARTERICSSON0001/get_instant_circuit_measures_between_dates/19/'+now+'/'+now+'/', timeout=10)
        print(resp.url)
        resp_json = resp.json()
        print(resp_json)
        if resp.status_code != 200:
            lbl5['text'] = 'Problemas na solicitação...'
        else:
            print(resp)
            lbl5['text'] ='Potencia ativa: '+str(resp_json['instant_circuit_meaures'][0]['active_power'])+'\n'+'Potencia Aparente: '+str(resp_json['instant_circuit_meaures'][0]['apparent_power'])+'\n'+'Corrente: '+str(resp_json['instant_circuit_meaures'][0]['current'])+'\n'+'Energia Ativa de Exportação: '+str(resp_json['instant_circuit_meaures'][0]['export_active_energy'])+'\n'+'Exportação de Energia Reativa: '+str(resp_json['instant_circuit_meaures'][0]['export_active_energy'])+'\n'+'Exportação de Energia Ativa: '+str(resp_json['instant_circuit_meaures'][0]['export_active_energy'])+'\n'+'Importação de Energia Ativa : '+str(resp_json['instant_circuit_meaures'][0]['import_active_energy'])+'\n'+'Importação de Energia Reativa : '+str(resp_json['instant_circuit_meaures'][0]['import_reactive_energy'])+'\n'+ 'Frequencia de linha: '+str(resp_json['instant_circuit_meaures'][0]['line_frequency'])+'\n'+ 'Fator de potencia: '+str(resp_json['instant_circuit_meaures'][0]['power_factor'])+'\n'+'Potencia Reativa : '+str(resp_json['instant_circuit_meaures'][0]['reactive_power'])+'\n'+'Tensão: '+str(resp_json['instant_circuit_meaures'][0]['voltage'])+'\n'+'Medição feita em: '+str(resp_json['instant_circuit_meaures'][0]['timestamp'][0:-4])                                                                                                                                                         #
    elif labelId == 'lbl6':
        nowS = datetime.now().strftime("%S")
        if int(nowS) < 30:
            now = datetime.now().strftime("%Y-%m-%d_%H:%M:00")
        elif int(nowS) >= 30:
            now = datetime.now().strftime("%Y-%m-%d_%H:%M:30")
        resp = get(
            'http://34.225.222.91:5000/SMARTERICSSON0001/get_instant_circuit_measures_between_dates/20/' + now + '/' + now + '/',
            timeout=10)
        print(resp.url)
        resp_json = resp.json()
        if resp.status_code != 200:
            lbl6['text'] = 'Problemas na solicitação...'
        else:
            print(resp)
            lbl6['text'] = 'Potencia ativa: '+str(resp_json['instant_circuit_meaures'][0]['active_power'])+'\n'+'Potencia Aparente: '+str(resp_json['instant_circuit_meaures'][0]['apparent_power'])+'\n'+'Corrente: '+str(resp_json['instant_circuit_meaures'][0]['current'])+'\n'+'Energia Ativa de Exportação: '+str(resp_json['instant_circuit_meaures'][0]['export_active_energy'])+'\n'+'Exportação de Energia Reativa: '+str(resp_json['instant_circuit_meaures'][0]['export_active_energy'])+'\n'+'Exportação de Energia Ativa: '+str(resp_json['instant_circuit_meaures'][0]['export_active_energy'])+'\n'+'Importação de Energia Ativa : '+str(resp_json['instant_circuit_meaures'][0]['import_active_energy'])+'\n'+'Importação de Energia Reativa : '+str(resp_json['instant_circuit_meaures'][0]['import_reactive_energy'])+'\n'+ 'Frequencia de linha: '+str(resp_json['instant_circuit_meaures'][0]['line_frequency'])+'\n'+ 'Fator de potencia: '+str(resp_json['instant_circuit_meaures'][0]['power_factor'])+'\n'+'Potencia Reativa : '+str(resp_json['instant_circuit_meaures'][0]['reactive_power'])+'\n'+'Tensão: '+str(resp_json['instant_circuit_meaures'][0]['voltage'])+'\n'+'Medição feita em: '+str(resp_json['instant_circuit_meaures'][0]['timestamp'][0:-4])                                                                                                                                                         #
    elif labelId == 'lbl7':
        nowS = datetime.now().strftime("%S")
        if int(nowS) < 30:
            now = datetime.now().strftime("%Y-%m-%d_%H:%M:00")
        elif int(nowS) >= 30:
            now = datetime.now().strftime("%Y-%m-%d_%H:%M:30")
        resp = get(
            'http://34.225.222.91:5000/SMARTERICSSON0001/get_instant_circuit_measures_between_dates/21/' + now + '/' + now + '/',
            timeout=10)
        print(resp.url)
        resp_json = resp.json()
        if resp.status_code != 200:
            lbl7['text'] = 'Problemas na solicitação...'
        else:
            print(resp)
            lbl7['text'] = 'Potencia ativa: '+str(resp_json['instant_circuit_meaures'][0]['active_power'])+'\n'+'Potencia Aparente: '+str(resp_json['instant_circuit_meaures'][0]['apparent_power'])+'\n'+'Corrente: '+str(resp_json['instant_circuit_meaures'][0]['current'])+'\n'+'Energia Ativa de Exportação: '+str(resp_json['instant_circuit_meaures'][0]['export_active_energy'])+'\n'+'Exportação de Energia Reativa: '+str(resp_json['instant_circuit_meaures'][0]['export_active_energy'])+'\n'+'Exportação de Energia Ativa: '+str(resp_json['instant_circuit_meaures'][0]['export_active_energy'])+'\n'+'Importação de Energia Ativa : '+str(resp_json['instant_circuit_meaures'][0]['import_active_energy'])+'\n'+'Importação de Energia Reativa : '+str(resp_json['instant_circuit_meaures'][0]['import_reactive_energy'])+'\n'+ 'Frequencia de linha: '+str(resp_json['instant_circuit_meaures'][0]['line_frequency'])+'\n'+ 'Fator de potencia: '+str(resp_json['instant_circuit_meaures'][0]['power_factor'])+'\n'+'Potencia Reativa : '+str(resp_json['instant_circuit_meaures'][0]['reactive_power'])+'\n'+'Tensão: '+str(resp_json['instant_circuit_meaures'][0]['voltage'])+'\n'+'Medição feita em: '+str(resp_json['instant_circuit_meaures'][0]['timestamp'][0:-4])                                                                                                                                                         #
    elif labelId == 'lbl8':
        nowS = datetime.now().strftime("%S")
        if int(nowS) < 30:
            now = datetime.now().strftime("%Y-%m-%d_%H:%M:00")
        elif int(nowS) >= 30:
            now = datetime.now().strftime("%Y-%m-%d_%H:%M:30")
        resp = get(
            'http://34.225.222.91:5000/SMARTERICSSON0001/get_instant_circuit_measures_between_dates/22/' + now + '/' + now + '/',
            timeout=10)
        print(resp.url)
        resp_json = resp.json()
        if resp.status_code != 200:
            lbl8['text'] = 'Problemas na solicitação...'
        else:
            print(resp)
            lbl8['text'] = 'Potencia ativa: '+str(resp_json['instant_circuit_meaures'][0]['active_power'])+'\n'+'Potencia Aparente: '+str(resp_json['instant_circuit_meaures'][0]['apparent_power'])+'\n'+'Corrente: '+str(resp_json['instant_circuit_meaures'][0]['current'])+'\n'+'Energia Ativa de Exportação: '+str(resp_json['instant_circuit_meaures'][0]['export_active_energy'])+'\n'+'Exportação de Energia Reativa: '+str(resp_json['instant_circuit_meaures'][0]['export_active_energy'])+'\n'+'Exportação de Energia Ativa: '+str(resp_json['instant_circuit_meaures'][0]['export_active_energy'])+'\n'+'Importação de Energia Ativa : '+str(resp_json['instant_circuit_meaures'][0]['import_active_energy'])+'\n'+'Importação de Energia Reativa : '+str(resp_json['instant_circuit_meaures'][0]['import_reactive_energy'])+'\n'+ 'Frequencia de linha: '+str(resp_json['instant_circuit_meaures'][0]['line_frequency'])+'\n'+ 'Fator de potencia: '+str(resp_json['instant_circuit_meaures'][0]['power_factor'])+'\n'+'Potencia Reativa : '+str(resp_json['instant_circuit_meaures'][0]['reactive_power'])+'\n'+'Tensão: '+str(resp_json['instant_circuit_meaures'][0]['voltage'])+'\n'+'Medição feita em: '+str(resp_json['instant_circuit_meaures'][0]['timestamp'][0:-4])                                                                                                                                                         #
    janela.update_idletasks()



def alteraEstado():
    session = FuturesSession() #inicia a sessão http
    fut1 = session.put()




def hello():
    print('hello')


janela = Tk()

styleBtn = ttk.Style()
styleBtn.map("C.TButton",
          foreground = [('pressed','red'),('active','blue')],
          background = [('pressed', '!disabled','black'),('active','white')])

btnImage = PhotoImage(file = 'testeBtn.png')

background_image= PhotoImage(file = '22222.png')
background_label = Label(janela, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
#background_label.image = background_image


btn1 = ttk.Button(master = janela,text='Mudar estado C1',style = "C.TButton", command = partial(startThread,'lbl1'),
          width = '20')
btn1.place(x=30,y=20)
btn2 = ttk.Button(master = janela,text='Mudar estado C2',style = "C.TButton", command = partial(startThread,'lbl3'),
          width = '20')
btn2.place(x=30,y=120)
btn3 = ttk.Button(master = janela,text='Mudar estado C3',style = "C.TButton", command = partial(startThread,'lbl2'),
          width = '20')
btn3.place(x=30,y=220)
btn4 = ttk.Button(master = janela,text='Mudar estado C4',style = "C.TButton", command = partial(startThread,'lbl4'),
          width = '20')
btn4.place(x=30,y=320)
btn5 = ttk.Button(master = janela,text='Ler C1',style = "C.TButton", command = partial(startThread,'lbl5'),
          width = '20')
btn5.place(x=230,y=20)
btn6 = ttk.Button(master = janela,text='Ler C2',style = "C.TButton", command = partial(startThread,'lbl6'),
          width = '20')
btn6.place(x=470,y=20)
btn7 = ttk.Button(master = janela,text='Ler C3',style = "C.TButton", command = partial(startThread,'lbl7'),
          width = '20')
btn7.place(x=710,y=20)
btn8 = ttk.Button(master = janela,text='Ler C4',style = "C.TButton", command = partial(startThread,'lbl8'),
          width = '20')
btn8.place(x=950,y=20)

'''resp = get(url_hexa+metodos['get_circuits'])
resp = resp.json()
print(resp)'''


lbl1 = ttk.Label(master = janela, text = 'Ligado!',relief = 'flat', background= 'green', foreground = 'white')
lbl1.place(x=80, y=75)
lbl2 = ttk.Label(master = janela, text = 'Ligado!',relief = 'flat', background = 'green', foreground = 'white')
lbl2.place(x=80, y=175)
lbl3 = ttk.Label(master = janela, text = 'Ligado!',relief = 'flat', background = 'green', foreground = 'white')
lbl3.place(x=80, y=275)
lbl4 = ttk.Label(master = janela, text = 'Ligado!',relief = 'flat', background = 'green', foreground = 'white')
lbl4.place(x=80, y=375)
lbl5 = ttk.Label(master = janela, text = 'Saída',relief = 'flat',background= 'green', foreground = 'white')
lbl5.place(x=180, y=55)
lbl6 = ttk.Label(master = janela, text = 'Saída',relief = 'flat',background= 'green', foreground = 'white')
lbl6.place(x=420, y=55)
lbl7 = ttk.Label(master = janela, text = 'Saída',relief = 'flat',background= 'green', foreground = 'white')
lbl7.place(x=660, y=55)
lbl8 = ttk.Label(master = janela, text = 'Saída',relief = 'flat',background= 'green', foreground = 'white')
lbl8.place(x=900, y=55)

janela.geometry('1200x450')


janela.title('Smart Quadro Controlador')



janela.mainloop()

