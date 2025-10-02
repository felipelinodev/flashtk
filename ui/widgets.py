import customtkinter
from PIL import Image as PILImage

class Button(customtkinter.CTkButton):
    def __init__(self, master, variant="default", **kwargs):
        super().__init__(master=master, **kwargs, height=36, font=("Geist", 14, "normal"))
        self.pack(padx=10, pady=10)
        if variant == "desabled":
            self.configure(
                fg_color=("#27272A", "#27272A"),
                text_color=("#727272", "#727272")
            )
            self._state = "desabled"
        if variant == "destructive":
            self.configure(
                fg_color=("#9E4042", "#9E4042"),
                text_color=("#FAFAFA","#FAFAFA"),
                hover_color=("#803537", "#803537")
            
        
                
            )
        




class CheckBox(customtkinter.CTkCheckBox):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs, checkbox_width=16, checkbox_height=16, corner_radius=5)
        self.pack(padx=10, pady=10)



class ComboBox(customtkinter.CTkComboBox):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs, width=200, text_color="#E7E7E7",  height=36, font=("Geist", 14, "normal"))
        self.pack(padx=20, pady=20)



class Entry(customtkinter.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, width=320, height=36, font=("Geist", 14, "normal"),  text_color="#E7E7E7", **kwargs)
        self.pack(padx=10, pady=10)
        
    def get_value(self):
        return self.get()


class Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.pack(pady=10, padx=10)
        self.pack_propagate(False)



class Label(customtkinter.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", font=("Geist", 14, "normal"), **kwargs)
        self.pack(padx=10, pady=10)



class TextBox(customtkinter.CTkTextbox):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, border_spacing=12, width=598, height=64, font=("Geist", 14, "normal") ,**kwargs)
        self.pack(padx=10, pady=10)

    def placeholder(self, placeholder_text):
        if self.get("1.0", "end-1c") == "":
            self.insert("1.0", placeholder_text)
            self.configure(text_color="#D4D4D4")



class Image:
    def __init__(self, app, path, porcent=100):
        self.app = app
        self.path = path
        self.porcent = porcent
        
        img_original = PILImage.open(path)
        w_original, h_original = img_original.size
        
        nova_largura = int(w_original * (porcent / 100))
        nova_altura = int(h_original * (porcent / 100))
        
        self.imagem = customtkinter.CTkImage(
            light_image=img_original,
            size=(nova_largura, nova_altura)
        )
        
        self.label_imagem = customtkinter.CTkLabel(
            app, 
            image=self.imagem, 
            text=""
        )

        self.label_imagem.pack(pady=10, padx=10)
    
    def pack(self, pady=None, padx=None, **kwargs):
        self.label_imagem.pack(pady=pady, padx=padx, **kwargs)
    
    def grid(self, row=None, column=None, **kwargs):
        self.label_imagem.grid(row=row, column=column, **kwargs)
    
    def place(self, x=None, y=None, **kwargs):
        self.label_imagem.place(x=x, y=y, **kwargs)
    
    def hide(self):
        self.label_imagem.pack_forget()

    
        