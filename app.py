from ui.widgets import Button, Label, Image, Frame
from core.index import Root
from core.hooks import useState
from core.utils import flash_action, destroy_widget


app = Root("FlasTK", "1200x700")

def render():
    destroy_widget(app)

    Image(app, path="public/logo.png", porcent=6).pack(pady=100, padx=0)

    frame = Frame(app, width=350, height=170)
    Label(frame, text=f"CONT: {number.state}")
    Button(frame, text="Incrementar", width=320, command=increment)
    Button(frame, text="Decrementar", width=320, command=decrement)


number = useState(0)

@flash_action(render)
def increment():
    number.set_state(number.state + 1)

@flash_action(render)
def decrement():
    number.set_state(number.state - 1)


render()
app.mainloop()