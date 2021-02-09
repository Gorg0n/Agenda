from pptxClass import *

filePresentazione = 'presentazione'
oo = 'gennaio-febbraio-2020.pptx'
pptx = PPTX(filePresentazione, 'IO', oo)

from datetime import date,timedelta
sdate = date(2020, 12, 28)
edate = date(2021,2,28)
delta = edate - sdate
giorni = ['lun','mart','merc','giov','ven','sab','dom']
mesi = ['gennaio', 'febbraio','marzo','aprile','maggio','giugno','luglio','agosto','settembre','ottobre','novembre','dicembre']
mese = []
giornia  = []
numeroSettimana = []
SETTIMANA = []
for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    if len(mese)==0:
        a=day.month-1
        mese.append(mesi[a])
    wd=day.weekday()
    if wd == 3:
        weekNr=date.isocalendar(day)[1]
        b = 'settimana '+str(weekNr)
        numeroSettimana.append(b)
    wd = giorni[wd]+' ' + str(day.day)
    giornia.append(wd)
    if len(giornia) == 7:
        a = day.month -1
        if mesi[a] not in mese:
            mese = mese[0] + '-' + mesi[a]
        else:
            mese = mese[0]
        SETTIMANA.append(mese)
        SETTIMANA.append(numeroSettimana[0])
        for giorno in giornia:
            SETTIMANA.append(giorno)
        print(SETTIMANA)
        pptx.addWeek(SETTIMANA)
        SETTIMANA = []
        mese =[]
        giornia =[]
        numeroSettimana=[]



#pptx.addWeek(['gennaio', 'week 2','lun 10','mar 11','mer 12', 'gio 13', 'ven 14', 'sab 15', 'dom 16'])
#pptx.addWeek(['febbraio', 'week 2','lun 10','mar 11','mer 12', 'gio 13', 'ven 14', 'sab 15', 'dom 16'])

print('ciao')


'''

for table in document.tables:
    for cell in table.cells:
        for paragraph in cell.paragraphs:
            if 'sea' in paragraph.text:
            
'''