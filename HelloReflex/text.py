# 텍스트 컴포넌트 연습

import reflex as rx
from .navbar import navbar

def text():
    return navbar(
        rx.vstack(
            rx.heading(
                "텍스트 컴포넌트 연습 - 제목 컴포넌트", # 넣을 문장
                size="9", # 폰트 사이즈 1~9
                weight="light", # bold, medium, regular, light
                color_scheme="indigo", # 색깔 https://www.radix-ui.com/colors
                high_contrast=True, # 고대비(색상 진하게) True, false
                trim="start", # 위아래 여백 줄이기 start, end, both, normal
            ),
            rx.text(
                "텍스트 컴포넌트", # 넣을 문장
                size="7",
                weight="bold",
                color_scheme="cyan",
            ),
            rx.link(
                "링크 텍스트",
                href = "http://songdo.icehs.kr/main.do",  # 이동할 링크
                is_external=True, # 외부 링크 새로운 창으로 띄우기
            ),
            rx.link(
                rx.button("홈으로🏠"), # 이모지는 '윈도우 + .' 키로, link 안에 버튼을 넣으면 버튼이 링크가 된다.
                href = "/flexpage",  # 내부 링크는 add_page에 넣은 함수명이 경로가 된다.
            ),
        )
    )