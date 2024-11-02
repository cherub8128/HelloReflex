import reflex as rx
from .navbar import navbar

# py -m 
def index():
    return navbar(
        rx.heading("메인페이지"),
        rx.text("py -m reflex init"),
        rx.text("py -m reflex run"),
        rx.text.strong("⚠️매개변수 넣을 때 ,(콤마)를 항상 잊지 말기")
    )
