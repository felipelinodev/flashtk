from ui.widgets import Button, Label, Frame


def Task(app, name, callback):
    task = Frame(app, width=400, height=50)
    Label(task, text=name).pack(side="left")
    Button(task, text="Excluir", variant="destructive", width=100, command=lambda: callback()).pack(side="right")
    