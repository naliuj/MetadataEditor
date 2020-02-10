from kivy.uix.gridlayout import GridLayout


class EditorScreen(GridLayout):

    def __init__(self, **kwargs):
        super(EditorScreen, self).__init__(**kwargs)
        self.rows = 1
        self.cols = 2

