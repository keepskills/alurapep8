#!/usr/bin/env python3
# coding=utf-8
import os

from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida

os.system("cls||clear")

teste_fabrica = FabricaFila.pega_fila('prioritaria')
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(10))
print(teste_fabrica.chama_cliente(10))
print(teste_fabrica.chama_cliente(10))
print(teste_fabrica.estatistica(EstatisticaResumida('01/01/1991', 200)))
