# 색깔 사용 방법
import reflex as rx
from .navbar import navbar

def color():
    return navbar(
        rx.vstack(
            rx.link(rx.button("구글 컬러피커",color_scheme="indigo"), href="https://g.co/kgs/6sDP61x", is_external=True),
            rx.card(
                "색상을 지정하는 방법1: HEX \"#bbcef0\"",
                bg = "#bbcef0",
            ),
            rx.card(
                "색상을 지정하는 방법2: RGB \"RGB(154, 218, 237)\"",
                bg = "RGB(154, 218, 237)",
            ),
            rx.card(
                rx.text("색상을 지정하는 방법3: RGBA \"RGBA(240, 146, 198, 0.3)\""),
                rx.text("여기서 A는 Alpha 투명도로 0~1사이의 실수 값"),
                bg = "RGB(240, 146, 198, 0.3)",
            ),
            rx.card(
                rx.text("색상을 지정하는 방법4: Radix Color rx.color(\"grass\",3)"),
                rx.text("rx.color(색깔이름, 명암 1~12사이 정수)"),
                rx.link("Radix Color 보기", href="https://www.radix-ui.com/colors", is_external=True),
                bg = rx.color("grass", 3),
            ),
            rx.card(
                rx.text("색상을 지정하는 방법4: Radix Color Var \"var(--mint-3)\""),
                bg = "var(--mint-3)",
            ),
            rx.card(
                rx.text("색상을 지정하는 방법5: Radix Color Scheme", color_scheme = "crimson"),
                rx.text("매개변수가 있는 특정 컴포넌트(버튼,텍스트 등)에서만 사용 가능하다."),
            ),
            padding="1em"
        )
    )