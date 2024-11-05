# navbar.py 파일 만들기
import reflex as rx

# 네비게이션 링크 모양을 재사용하기 위해 만든 컴포넌트
def navbar_link(text, url):
  return rx.link(rx.text(text, size="4", weight="medium"), href=url)

def logo(text):
  return rx.hstack(
    # assets 폴더에 logo로 사용할 이미지를 logo.png 이름으로 넣기(flaticon 사이트에서 다운로드)
    rx.image(
      src="/logo.png",
      height="2em",
    ),
    rx.heading(text, size="7", color_scheme="cyan"),
    align_items="center",
  ),

def navbar_comp():
  return rx.box(
    # hstack은 가로로 쌓는 레이아웃 컴포넌트
    rx.hstack(
      logo("송도고등학교 Reflex 튜토리얼"),
      rx.hstack(
        navbar_link("홈", "/#"),
        navbar_link("텍스트", "/text"),
        navbar_link("플렉스", "/flexpage"),
        navbar_link("그리드", "/gridpage"),
        navbar_link("폼", "/forms"),
        navbar_link("미디어", "/media"),
        navbar_link("그래프", "/graph"),
        navbar_link("컬러", "/color"),
        rx.color_mode.button(),
        justify="end",
        align="center",
        spacing="5",
      ),
      justify="between",
      align_items="center",
    ),
    bg=rx.color("indigo", 3), 
    padding="0.5em", 
    width="100%",
  )
  
def navbar(*arg,**kwarg):
  # fragment는 단순히 묶는 용도의 레이아웃 컴포넌트, 어떤 매개변수에도 영향 받지 않는 특징
  return rx.fragment(
    rx.text("Created by 차형준",position="absolute",bottom="10px",right="10px",color_scheme="gray"),
    navbar_comp(),
    rx.box(
      *arg,
      **kwarg,
      padding="1em",
    ),
  )