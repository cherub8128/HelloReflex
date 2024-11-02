# State와 Event 다루기
import reflex as rx
from .navbar import navbar

# 웹에서 실시간으로 반영시킬 수 있는 변수
# 이 변수를 사용하면 변수가 바뀌면 웹페이지도 실시간으로 바뀐다.
class Counter(rx.State):
    count : int = 0
   
    def count_up(self):
        self.count += 1
    def count_down(self):
        self.count -= 1

def button():
    return navbar(
        rx.vstack(
            rx.heading("윈도우 창 띄우는 버튼"),
            rx.button("클릭", on_click=rx.window_alert("❤️")),
            rx.divider(),
            rx.heading(Counter.count),
            rx.button("+1", on_click=Counter.count_up, color_scheme="cyan"),
            rx.button("-1", on_click=Counter.count_down, color_scheme="crimson"),
        )
    )