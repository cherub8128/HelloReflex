import reflex as rx
import typing

class SliderState(rx.State):
    value : int = 10 # on_value_commit은 set 함수가 동작하지 않으므로 직접 만들어야함
    def set_end(self, value: list[typing.Union[int, float]]): 
        self.value = value[0]

    
def slider():
    return rx.vstack(
        rx.heading(
            SliderState.value,
            color=f"rgba(20,20,20,{SliderState.value/100})"
        ),
        rx.slider(
            default_value=SliderState.value,
            min=0,
            max=100,
            step=5,
            on_value_commit=SliderState.set_end,
            color_scheme="cyan"
        ),
        padding_top="1em"
    )