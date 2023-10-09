from flet_mvc import data
from .index import IndexModel
import flet as ft
import random


class HomeModel(IndexModel):
    @data
    def example_content(self):
        op = ["piedra", "papel", "tijera"]
        computer = random.choice(op)
        return f"Del arreglo {op} el random escogio sacar {computer}"
