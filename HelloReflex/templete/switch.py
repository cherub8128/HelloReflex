import reflex as rx

class SwitchState(rx.State):
    value: bool = False
        
def switch():
    return rx.vstack(
        rx.switch(
            default_checked=SwitchState.value,
            on_change=SwitchState.set_value
        ),
        rx.badge(SwitchState.value),
        rx.heading(
            f"스위치 버튼 {rx.cond(SwitchState.value,'켜짐','꺼짐')}"
        ),
        padding_top="1em"
    )