import reflex as rx
from .navbar import navbar
from PIL import Image
import requests

# 이미지는 url를 그냥 넣으면 불러와지지 않음
class ImageState(rx.State): # State는 버튼 페이지에서 자세히 설명
    url = f"https://picsum.photos/id/1/200/300"
    image = Image.open(requests.get(url, stream=True).raw)


def media():
    return navbar(
        # 세로로 쌓는 레이아웃 컴포넌트
        rx.vstack(
            # 에셋으로 이미지 컴포넌트 넣기
            rx.image(
                src="/myimage1.jpg",  # assets 폴더
                width="auto", # 세로 길이에 맞춰서 원래 비율로 가로 길이 맞춰 넣기
                height="500px"
            ),
            rx.image(
                src="/myimage2.jpg",  # assets 폴더
                width="500px",
                height="auto",
                border_radius="5px 10px 15px 20px",
                border="5px solid #d2d2d2"
            ),
            # url로 이미지 넣기. 반드시 Image용 State가 필요함
            rx.image(src=ImageState.image),
            # 에셋으로 동영상 넣기
            rx.video(
                url="https://youtu.be/N_g3AiXF-q8?feature=shared", # 외부 Url
                width="500px",
                height="400px",
            ),
            rx.video(url="/myVideo.mp4"), # assets 폴더 안에 있는 영상 파일 불러오기
            # url로 오디오 넣기
            rx.audio(
                url="https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3",
                width="400px",
                height="50px",
            ),
            rx.audio( url="/myAudio.mp3", height="50px"), # assets 폴더 안에 있는 음악 파일 불러오기
        ),
    )