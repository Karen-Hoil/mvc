from flet_mvc import FletModel, data
import flet as ft
import random


class SettingsModel(FletModel):
    @data
    def example_content(self):
        my_array=['no estoy entendiendo', 'no entendi nada']
        a = random.choice(my_array)
        return a
