# 송도고등학교 정보 수업을 위한 Reflex 튜토리얼 예제

## 버전: 0.91v (2025-01-06 최종 수정)

## [실제 완성된 사이트 링크](https://helloreflex-aqua-orca.reflex.run)

## 사용 방법

1. Code(초록 버튼)  ➡️ Download Zip으로 다운로드 후 압축 풀기
2. 압축 풀 경로에 한글이 있으면 안됨
3. VSCode로 압축 푼 폴더 열기
4. 터미널 열기
5. pip install -r requirements.txt (또는 py -m pip install -r requirements.txt)
6. reflex init (또는 py -m reflex init)
7. reflex run (또는 py -m reflex run)
8. 코드와 화면을 보면서 코드 예제를 익힌다.

## 각 코드 설명

- helloreflex.py : 파일로 만든 페이지들을 불러와 홈페이지에 추가하는 기본 파일
- index.py : 홈페이지 처음에 보이는 페이지
- navbar.py : 홈페이지 맨 위 상단바 메뉴 컴포넌트
- text.py : 텍스트 컴포넌트 설명
- flexpage.py : box와 flex 레이아웃 컴포넌트 설명
- color.py : 컬러 사용법 페이지
- gridpage.py : card와 grid 레이아웃 컴포넌트 설명
- media.py : 이미지, 비디오, 음악 컴포넌트 설명
- form.py : 버튼, 체크박스, 인풋, 선택, 슬라이더, 스위치 state, event 기본 사용법 설명
- templete 폴더 : 버튼, 체크박스, 인풋, 선택, 슬라이더, 스위치를 모아둔 폴더

## 배우는 순서 (난이도)

1. helloreflex.py
2. text.py
3. flexpage.py
4. color.py (생략 가능, 참고용)
5. gridpage.py
6. media.py
7. navbar.py
8. form.py (templetes 폴더)
9. graph.py

## 주의사항

- reflex 홈페이지 이름(주소)을 바꾸고 싶다면 helloreflex 폴더 이름, helloreflex.py 이름, rxconfig.py 내부의 app_name을 모두 같은 이름으로 바꾼다.
- 이름은 반드시 소문자로만, 띄어쓰기 불가능.