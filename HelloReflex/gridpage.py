import reflex as rx
from .navbar import navbar

# card 레이아웃 컴포넌트를 재사용할 수 있도록 꾸미기
def mycard(text):
    return rx.card(
        rx.text(text,size="5"),
        height="100px",
        width="150px",
        margin="5px",
    )

def gridpage():
    return navbar(
        # https://yamoo9.gitbook.io/css-grid/grid-system 그리드 컴포넌트 가이드
        # 그리드 컴포넌트 가로 세로 나눌 칸 수를 정하고 배치
        rx.grid(
            mycard("1번"),
            mycard("2번"),
            mycard("3번"),
            mycard("4번"),
            mycard("5번"),
            mycard("6번"),
            rows="3",
            columns="2",
            flow="column", # 배치하는 순서 column은 세로로 먼저 배치, row는 가로로 배치
            spacing="3", # 그리드 사이 여백
            margin_bottom="10px",
            width="100%"
        ),
        rx.grid(
            mycard("1번"),
            mycard("2번"),
            mycard("3번"),
            mycard("4번"),
            mycard("5번"),
            mycard("6번"),
            rows="2", 
            flow="column", # row만 정하고 flow를 column으로 하면 자동배치하면서 세로 몇 줄로 만들지 고정
            gap="1em", # spacing과 같은 역할
            margin_bottom="10px",
            width="100%"
        ),
        rx.grid(
            mycard("첫번째 칸"),
            rx.card("마지막 칸", grid_area="5 / 4 / 6 / 5"),  # row시작/column시작/row끝/column끝
            rx.card(
                "그리드 연습",
                bg="#d2d2d2",
                grid_area="2 / 2 / 4 / 5", # row시작/column시작/row끝/column끝
            ),
            rows="5", 
            columns="4",
            flow="column", # row만 정하고 flow를 column으로 하면 자동배치하면서 세로 몇 줄로 만들지 고정
            gap="10px",
            margin_bottom="10px",
            padding="10px",
            width="100%",
        ),
    )