#!/usr/bin/env python3
# coding=utf-8
import os

from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida

# from fila_normal import FilaNormal
# from fila_prioritaria import FilaPrioritaria

os.system("cls||clear")

# fila_p = FilaNormal()
# fila_p.atualiza_fila()
# fila_p.atualiza_fila()
# fila_p.atualiza_fila()
# print(fila_p.chama_cliente(10))
# print(fila_p.chama_cliente(1))
# print(fila_p.estatistica('10/01/1993', 198, 'detail'))

teste_fabrica = FabricaFila.pega_fila('prioritaria')
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(10))
print(teste_fabrica.chama_cliente(10))
print(teste_fabrica.chama_cliente(10))
print(teste_fabrica.chama_cliente(10))
print(teste_fabrica.estatistica(EstatisticaResumida('10/01/1993', 200)))
