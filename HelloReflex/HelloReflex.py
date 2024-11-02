import reflex as rx
from .index import index
from .text import text
from .flexpage import flexpage
from .gridpage import gridpage
from .media import media
from .button import button
from .color import color

app = rx.App()
app.add_page(index)
app.add_page(text)
app.add_page(flexpage)
app.add_page(gridpage)
app.add_page(media)
app.add_page(button)
app.add_page(color)