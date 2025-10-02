
def flash_action(render):

    def decorator(fn):
        def weapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            render()
            return result
        return weapper
    return decorator 

def destroy_widget(app):
    for widget in app.winfo_children():
        widget.destroy()