'''
------------
Overview
------------

Python script to automatically post on multiple different
social media sites, such as Facebook and Linkedin. Each
class represents a module in the GUI. There is a viewer
for each of the different sites to help get a feel for
what it looks like on each site.

------------
Libraries
------------

Flexx:      https://flexx.readthedocs.io/en/stable/
PyAutoGUI:  https://pyautogui.readthedocs.io/en/latest/ 
'''

from flexx import flx, ui, event
import pyautogui


class UserInterface(flx.Widget):
    '''
    Final user interface shown to the user.
    Essentiallly the outside wraper for the project.
    '''
    def init(self):
        with ui.VSplit():
            Controls(flex=1)
            with ui.HSplit(flex=12):
                ContentSection()
                Editor()
            Feeds(flex=4)


class Editor(flx.Widget):
    '''
    Text editor for the post.
    '''
    def init(self):
        ui.MultiLineEdit(style='width: 100%; height: 100%;')


class ContentSection(flx.Widget):
    '''
    Section for the image, video, or link.
    '''
    def init(self):
        pass


class SimulationView(flx.Widget):
    '''
    Shows post from the perspective of specific media platform.
    '''
    def init(self):
        pass


class Controls(flx.Widget):
    '''
    Settings for the view and content can also be used to save.
    '''
    def init(self):
        with ui.HBox(style='justify-content: start;'):
            self.file = ui.Button(text='File')
            self.view = ui.Button(text='View')
            self.help = ui.Button(text='Help')


class Feeds(flx.Widget):
    '''
    Displays recent information from different media platforms.
    '''
    def init(self):
        pass


class Actions(flx.PyComponent):
    '''
    All of the functions needed to be run in order to
    save, post and load media posts.
    '''
    def init(self):
        pass

# Runs the interface as a desktop app.
if __name__ == "__main__":
    app = flx.App(UserInterface)
    app.launch('app')
    flx.run()