import reflex as rx

class MyInput(rx.State):
    text1: str = ""  # 변수를 만들면 set_변수이름의 함수로 값을 설정할 수 있음
    text2: str = "폼을 나가면 바뀜" 

def my_input():
    return rx.vstack(
        rx.input(
            placeholder="placeholder 매개변수를 바꾸면 여기에 나타남", 
            max_length=20,
            width="21em",
        ),
        rx.divider(),
        rx.heading(MyInput.text1, color_scheme="plum"),
        # set_변수이름 함수는 직접 만들지 않았어도 이미 있음
        rx.input(
            placeholder="여기에 입력하면 위에 나타남",
            on_change=MyInput.set_text1
        ),
        rx.divider(),
        rx.heading(MyInput.text2, color_scheme="gold"),
        rx.input(
            placeholder="여기에 입력한 뒤 빠져나가면 바뀜",
            on_blur=MyInput.set_text2,
            max_length=30,
            width="31em",
        ),
        padding_top="1em",
    )