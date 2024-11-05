import reflex as rx
from typing import List

class SelectState(rx.State):
    fruit: str = ""
    fruit_options: List[str] = [
        "사과",
        "딸기",
        "바나나",
        "귤",
        "키위",
    ]

def radio():
    return rx.vstack(
        rx.heading(
            rx.match(
                SelectState.fruit,
                ("사과","사과잼"),
                ("딸기","딸기케이크"),
                ("바나나","바나나우유"),
                ("귤","감귤푸딩"),
                ("키위","키위소르베"),
                "없음"
            ),
            color_scheme=rx.match(
                SelectState.fruit,
                ("사과","red"),
                ("딸기","crimson"),
                ("바나나","yellow"),
                ("귤","orange"),
                ("키위","lime"),
                "gray"
            )  
        ),
        rx.radio(
            SelectState.fruit_options,
            placeholder="과일 고르기",
            label="과일",
            value=SelectState.fruit,
            on_change=SelectState.set_fruit,
        ),
        padding_top="1em"
    )