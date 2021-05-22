# -*- coding: utf-8 -*-
"""
Created on Sat May 20 01:42:41 2021

@author: yogurtcongelado
"""

import pandas as pd
import matplotlib as plt 
#Cargamos el data set y luego hacemos lo que nos piden:
    
datf = pd.read_csv("oec.csv")

#Una forma no muy pitonica es hacerlo paso a paso


#datf.groupby(["DiscoveryMethod"]).mean()
#print(datf.groupby(["DiscoveryMethod"]).mean())
#df = datf[["DiscoveryMethod","PlanetaryMassJpt"]]
#print(df.groupby(["DiscoveryMethod"]).agg("sum"))


#Ahora para hacerlo sin guardarlo en memoria
#Con todas las columnas
print(datf.groupby(["DiscoveryMethod"]).agg("sum"))

#Solo con las que nos interesan
print(datf[["DiscoveryMethod","PlanetaryMassJpt"]].groupby(["DiscoveryMethod"]).agg("sum"))

#Ahora ploteamos los Las columnas que nos piden
plotdata = datf[["DiscoveryMethod","PlanetaryMassJpt"]].groupby(["DiscoveryMethod"]).agg("sum")
plotdata.plot(kind="bar",title = "Tarea 1 Masa vs Método de Descubrimiento")




