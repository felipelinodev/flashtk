import customtkinter

class Root(customtkinter.CTk):
    def __init__(self, title, geometry, **kwargs):
        customtkinter.set_default_color_theme("ui/theme.json")
        super().__init__(**kwargs)
        self.title(title)
        self.geometry(geometry)
