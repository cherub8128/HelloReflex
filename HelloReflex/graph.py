# pip install pandas
# py -m pip install pandas
import reflex as rx
import pandas as pd
from typing import List
from .navbar import navbar

nba_data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
data = [
    {"name": "Page A", "uv": 4000, "pv": 2400, "amt": 2400},
    {"name": "Page B", "uv": 3000, "pv": 1398, "amt": 2210},
    {"name": "Page C", "uv": 2000, "pv": 9800, "amt": 2290},
    {"name": "Page D", "uv": 2780, "pv": 3908, "amt": 2000},
    {"name": "Page E", "uv": 1890, "pv": 4800, "amt": 2181},
    {"name": "Page F", "uv": 2390, "pv": 3800, "amt": 2500},
    {"name": "Page G", "uv": 3490, "pv": 4300, "amt": 2100},
]

data01 = [
    {"name": "Group A", "value": 400},
    {"name": "Group B", "value": 300, "fill": "#AC0E08FF"},
    {"name": "Group C", "value": 300, "fill": "rgb(80,40, 190)"},
    {"name": "Group D", "value": 200, "fill": rx.color("yellow", 10)},
    {"name": "Group E", "value": 278, "fill": "purple"},
    {"name": "Group F", "value": 189, "fill": "orange"},
]

data02 = [
    {"과목": "수학","A": 100,"B": 80,"최대값": 100,},
    {"과목": "국어","A": 80,"B": 100,"최대값": 100,},
    {"과목": "영어","A": 86,"B": 90,"최대값": 100,},
    {"과목": "과학","A": 100,"B": 77,"최대값": 100,},
    {"과목": "정보","A": 95,"B": 80,"최대값": 100,},
    {"과목": "한국사","A": 65,"B": 85,"최대값": 100,},
]

data03 = [
    {"x": 100, "y": 200, "z": 200},
    {"x": 120, "y": 100, "z": 260},
    {"x": 170, "y": 300, "z": 400},
    {"x": 170, "y": 250, "z": 280},
    {"x": 150, "y": 400, "z": 500},
    {"x": 110, "y": 280, "z": 200},
]

class MyInput(rx.State):
    text : str = ""

class MySlider(rx.State):
    value : int = 0
    def set_end(self, value:int):
        self.value = value

class Check(rx.State):
    check : bool = False
    def change(self):
        self.check = not self.check
        
class State(rx.State):
    data: List = [
        ["Lionel", "Messi", "PSG"],
        ["Christiano", "Ronaldo", "Al-Nasir"],
    ]
    columns: List[str] = ["First Name", "Last Name"]

def chart1():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="uv",
            stroke=rx.color("accent", 9),
            fill=rx.color("accent", 8),
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=data, width="100%",height=250)

def chart2():
    return rx.recharts.line_chart(
        rx.recharts.line(data_key="pv"),
        rx.recharts.line(data_key="uv"),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=data,
        width="100%",
        height=300,
    )

def chart3():
    return rx.recharts.pie_chart(
        rx.recharts.pie(
            data=data01,
            data_key="value",
            name_key="name",
            fill="#8884d8",
            label=True,
        ),
        width="100%", height=300, )

def chart4():
    return rx.recharts.radar_chart(
        rx.recharts.radar(data_key="A", stroke="#8884d8", fill="#8884d8"),
        rx.recharts.polar_grid(),
        rx.recharts.polar_angle_axis(data_key="과목"),
        rx.recharts.polar_radius_axis(angle=90, domain=[0, 100]),
        data=data02,
        width="100%",
        height=300,
    )

def chart5():
    return rx.recharts.scatter_chart(
        rx.recharts.scatter(data=data03,fill="#8884d8"),
        rx.recharts.x_axis(data_key="x", type_="number"),
        rx.recharts.y_axis(data_key="y"),
        rx.recharts.z_axis(data_key="z",range=[200, 500],),
        width="100%",
        height=300,
    )


def graph():
    return navbar(
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("바차트",value="chart1"),
                rx.tabs.trigger("라인차트",value="chart2"),
                rx.tabs.trigger("파이차트",value="chart3"),
                rx.tabs.trigger("레이더차트",value="chart4"),
                rx.tabs.trigger("산점도",value="chart5"),
            ),
            rx.tabs.content(chart1(),value="chart1"),
            rx.tabs.content(chart2(),value="chart2"),
            rx.tabs.content(chart3(),value="chart3"),
            rx.tabs.content(chart4(),value="chart4"),
            rx.tabs.content(chart5(),value="chart5"),
            defalut_value="chart1"
        )
    )
