import reflex as rx
from .index import index
from .text import text
from .flexpage import flexpage
from .gridpage import gridpage
from .media import media
from .forms import forms
from .color import color

# em에 영향을 주는 폰트 사이즈
style = {
    "font_size": "20px",
    "font_family": "Noto Sans KR, sans-serif", # 글씨체를 바꾸기
}

# 바꿀 글씨체를 불러오기 위한 변수
font =  "https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100..900&display=swap"

# 글씨체와 폰트 사이즈를 바꾸기 위해서는 App에 매개변수를 아래와 같이 추가한다.
app = rx.App(stylesheets=[font,], style=style)

app.add_page(index)
app.add_page(text)
app.add_page(flexpage)
app.add_page(gridpage)
app.add_page(media)
app.add_page(forms)
app.add_page(color)