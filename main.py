#!/usr/bin/env python3
# coding=utf-8
import os

# from fila_normal import FilaNormal
# from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila
# from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida

os.system("cls||clear")

fila = FabricaFila.pega_fila('prioritaria')
fila.atualiza_fila()
fila.atualiza_fila()
fila.atualiza_fila()
print(fila.chama_cliente(5))
print(fila.estatistica(EstatisticaResumida('01/01/1991', 1234)))
