# State와 Event 다루기
import reflex as rx
from .navbar import navbar

# templete 폴더에서 불러오기
# templete 폴더를 불러오려면 비어있는 __init__.py가 있어야 함
from .templete.button import button
from .templete.checkbox import checkbox
from .templete.my_input import my_input
from .templete.radio import radio
from .templete.select import select
from .templete.slider import slider
from .templete.switch import switch

def forms():
    return navbar(
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("버튼", value="button"),
                rx.tabs.trigger("체크박스", value="checkbox"),
                rx.tabs.trigger("인풋", value="input"),
                rx.tabs.trigger("라디오그룹", value="radio"),
                rx.tabs.trigger("선택", value="select"),
                rx.tabs.trigger("슬라이더", value="slider"),
                rx.tabs.trigger("스위치", value="switch"),
            ),
            rx.tabs.content(button(),value="button"),
            rx.tabs.content(checkbox(),value="checkbox"),
            rx.tabs.content(my_input(),value="input"),
            rx.tabs.content(radio(),value="radio"),
            rx.tabs.content(select(),value="select"),
            rx.tabs.content(slider(),value="slider"),
            rx.tabs.content(switch(),value="switch"),
            # 버튼이 아닌 다른 폼을 수정할 때는 기본 값을 바꾸면 편함
            default_value="button",
        )
    )