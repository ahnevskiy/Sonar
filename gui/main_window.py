from tkinter import *
from tkinter_wrapper.button import MyButton
from tkinter_wrapper.check_box import MyCheckBox
from tkinter_wrapper.container_labeled import MyContainerLabeled

WINDOW_HEIGHT = 810
WINDOW_WIDTH = 1310

INDENT = 5

ACTIONS_UNIT_HEIGHT = 250
ACTIONS_UNIT_WIDTH = 250

SUBMARINE_UNIT_HEIGHT = 250
SUBMARINE_UNIT_WIDTH = 905

MAIN_MENU_WIDTH = 405
MAIN_MENU_HEIGHT = 100

CHAT_WIDTH = 405
CHAT_HEIGHT = 145

UNITS_WIDTH = 295
UNITS_HEIGHT = 310

MAP_WIDTH = 400
MAP_HEIGHT = 400


def create_main_window():
    window = Tk()
    window.title("[Настольный симулятор] Субмарина")
    window.iconbitmap("gui/data/sonar.ico")
    window["height"] = WINDOW_HEIGHT
    window["width"] = WINDOW_WIDTH
    window.resizable(height=False, width=False)

    cl_team_actions = MyContainerLabeled(parent=window,
                                         label="Действия экипажа",
                                         x=INDENT,
                                         y=INDENT,
                                         width=ACTIONS_UNIT_WIDTH-2*INDENT,
                                         height=ACTIONS_UNIT_HEIGHT-INDENT,
                                         name="cl_enemy_actions",
                                         del_name="!labelframe")

    cl_enemy_actions = MyContainerLabeled(parent=window,
                                          label="Действия противника",
                                          x=ACTIONS_UNIT_WIDTH+MAIN_MENU_WIDTH+INDENT,
                                          y=INDENT,
                                          width=ACTIONS_UNIT_WIDTH-2*INDENT,
                                          height=ACTIONS_UNIT_HEIGHT-INDENT,
                                          name="cl_enemy_actions",
                                          del_name="!labelframe2")

    cl_submarine = MyContainerLabeled(parent=window,
                                      label="Субмарина",
                                      x=INDENT,
                                      y=window["height"] - SUBMARINE_UNIT_HEIGHT,
                                      width=SUBMARINE_UNIT_WIDTH-2*INDENT,
                                      height=SUBMARINE_UNIT_HEIGHT-INDENT,
                                      name="cl_submarine",
                                      del_name="!labelframe3")

    cl_main_menu = MyContainerLabeled(parent=window,
                                      label="Главное меню",
                                      x=ACTIONS_UNIT_WIDTH,
                                      y=INDENT,
                                      width=MAIN_MENU_WIDTH,
                                      height=MAIN_MENU_HEIGHT,
                                      name="cl_main_menu",
                                      del_name="!labelframe4")

    cl_chat = MyContainerLabeled(parent=window,
                                      label="Чат",
                                      x=ACTIONS_UNIT_WIDTH,
                                      y=INDENT+MAIN_MENU_HEIGHT,
                                      width=CHAT_WIDTH,
                                      height=CHAT_HEIGHT,
                                      name="cl_chat",
                                      del_name="!labelframe5")

    cl_captain_bridge = MyContainerLabeled(parent=window,
                                           label="Капитанский мостик",
                                           x=INDENT,
                                           y=INDENT+MAIN_MENU_HEIGHT+CHAT_HEIGHT,
                                           width=UNITS_WIDTH,
                                           height=UNITS_HEIGHT,
                                           name="cl_captain_bridge",
                                           del_name="!labelframe6")

    cl_engineering_unit = MyContainerLabeled(parent=window,
                                             label="Машинное отделение",
                                             x=INDENT*2+UNITS_WIDTH,
                                             y=INDENT+MAIN_MENU_HEIGHT+CHAT_HEIGHT,
                                             width=UNITS_WIDTH,
                                             height=UNITS_HEIGHT,
                                             name="cl_engineering_unit",
                                             del_name="!labelframe7")

    cl_armory = MyContainerLabeled(parent=window,
                                   label="Арсенал",
                                   x=INDENT*3+2*UNITS_WIDTH,
                                   y=INDENT+MAIN_MENU_HEIGHT+CHAT_HEIGHT,
                                   width=UNITS_WIDTH,
                                   height=UNITS_HEIGHT,
                                   name="cl_armory",
                                   del_name="!labelframe8")

    cl_captains_map = MyContainerLabeled(parent=window,
                                         label="Карта капитана",
                                         x=SUBMARINE_UNIT_WIDTH,
                                         y=INDENT,
                                         width=MAP_WIDTH,
                                         height=MAP_HEIGHT,
                                         name="cl_captains_map",
                                         del_name="!labelframe9")

    cl_radioman_map = MyContainerLabeled(parent=window,
                                         label="Карта радиста",
                                         x=SUBMARINE_UNIT_WIDTH,
                                         y=INDENT+MAP_HEIGHT,
                                         width=MAP_WIDTH,
                                         height=MAP_HEIGHT,
                                         name="cl_captains_map",
                                         del_name="!labelframe10")

    return window

