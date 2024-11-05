import reflex as rx 

class Check(rx.State):
    check : bool = False
    def change(self):
        self.check = not self.check

def checkbox():
    return rx.vstack(
        rx.checkbox(
            "동의합니다.",
            size="3",
            color_scheme="red",
            variant="soft",
        ),
        rx.checkbox(
            "체크하면 윈도우 창",
            on_change=rx.window_alert("👍")
        ),
        rx.divider(),
        rx.heading(rx.cond(Check.check,"체크됨","체크되지 않음"), color_scheme="amber"),
        rx.checkbox("글씨가 바뀌는 체크박스",on_change=Check.change()),
        padding_top="1em",
    )

