# flex 레이아웃 튜토리얼
import reflex as rx
from .navbar import navbar

# flex 레이아웃을 실험하기 위해 재사용하기 위한 박스 레이아웃 컴포넌트 만들기
# 반복해서 사용하는 스타일의 컴포넌트는 함수로 만들어서 재사용하면 코드를 줄여준다.
# text: 박스에 넣을 text
# w: 박스 가로 길이
# h: 박스 세로 길이
def mybox(text, w, h):
    return rx.box(
        rx.text(text, size="5", weight="medium", color_scheme="gold"),
        width=f"{w}px",
        height=f"{h}px",
        border = "solid 1px #d2d2d2",  # 윤곽선 선종류 두께 색깔(RGB Hex코드, 구글에 컬러피커 검색)
        margin = "0.5em", # 바깥 여백
        padding = "1em", # 안쪽 여백
        border_radius = "5px", # 모서리 둥글게 하기
        bg = "#f0f0f0", # 배경색
        # 그림자 x오프셋, y오프셋, 흐림 반경, 퍼짐 반경, 색(rgba a는 알파, 튜토리얼 컬러페이지 참고)
        box_shadow = "2px 2px 10px 2px rgba(200, 200, 200, .2)",
    )
def flexpage():
    return navbar(
        # 1차원 레이아웃 가로나 세로로 자동배치
        rx.flex(
            mybox("박스1",300,200),
            mybox("박스2",200,300),
            mybox("박스3",100,100),
            mybox("박스4",250,250),
            mybox("박스5",150,200),
            mybox("박스6",210,100),
            mybox("박스7",100,150),
            wrap = "wrap", # wrap을 할 경우 알아서 줄바꿈해서 배치, 안할 경우 강제로 줄여서 한 줄에 모두 배치
            direction = "row", # row, row-reverse, column, column-reverse  가로로 배치, 가로 역순, 세로 배치, 세로 역순
            justify="center", # row일 때 가로 기준 정렬
            align="center", # column일 때 세로 기준 정렬
            
        ),
    )