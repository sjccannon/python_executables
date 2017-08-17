from tkinter import *
import _tkinter
import requests, sys
from multiprocessing import Queue


def calculate_ENST(enst):
    print(enst)
    total = 11
    base = 'ENST'
    this_enst = total - len(enst)
    zeros = "0" * this_enst
    enst_str = base + zeros + enst
    print(enst_str)
    return enst_str

#external_db=RefSeq_mRNA
def return_NM():
    enst = content.get()
    #ENST00000407236
    enst_str = calculate_ENST(enst)
    server = "http://grch37.rest.ensembl.org"
    ext = "/xrefs/id/" + enst_str + "?object_type=transcript"
    r = requests.get(server + ext, headers={ "Content-Type" : "application/json"})
    json_r = r.json()
    row_count = 4
    for item in json_r:
        for k,v in item.items():
            if 'NM_' in str(v) or 'NM_' in str(k):
                #print(k, v)
                row_count += 1
                mylabel = Label(master, text=str(v))
                mylabel.grid(row=row_count, column=0)

master = Tk()
Label(master, text="Enter all numbers > 0 from ENST_ID").grid(row=0)
Label(master, text="(E.g. for ENST0000544455 enter 544455)").grid(row=1) 

content=StringVar()
e1 = Entry(master, textvariable=content)
e1.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Click here to Return NM IDs', command=return_NM).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
