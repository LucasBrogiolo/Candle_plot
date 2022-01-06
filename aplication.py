from tkinter import *
from tkinter import ttk
import pandas as pd
from pandas_datareader import data as web
import plotly.graph_objects as go

def grafico_candle():
    df = pd.DataFrame()
    ativo = acao.get()
    df = web.DataReader(ativo, data_source="yahoo", start="01-12-2020")

    trace1 = {
        "x": df.index,
        "open": df.Open,
        "close": df.Close,
        "high": df.High,
        "low": df.Low,
        "type": "candlestick",
        "name": ativo,
        "showlegend": False
        }

    data = [trace1]
    layout = go.Layout()
    fig = go.Figure(data=data, layout=layout)
    fig.show()

root = Tk()
root.title("Gerar gráfico")

main_frame = ttk.Frame(root, padding="3 3 12 12").grid(row=0, column=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(main_frame, text="Insira a empresa: ").grid(
    column=0, row=0, columnspan=2, sticky=W)
acao = StringVar()
ttk.Entry(main_frame, textvariable=acao).grid(
    column=0, row=1, columnspan=2)
ttk.Button(main_frame, text="gerar gráfico",
    default="active", command=grafico_candle).grid(column=2, row=1)

ttk.Label(main_frame, text="thank for use\ndev.percussa").grid(column=1, row=4)


root.mainloop()