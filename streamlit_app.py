import io
from PIL import Image

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk


def main():
    st.set_page_config(page_title="Streamlit 요소 예제", layout="centered")

    st.title("Streamlit 한 페이지 예제 — UI 요소와 각주")
    st.write("아래는 한 개의 Streamlit 페이지에 넣을 수 있는 여러 요소들의 예시입니다. 각 요소 옆에 각주 번호가 붙어 있으며, 페이지 하단에 각주 설명이 있습니다.")

    # 준비 데이터
    df = pd.DataFrame({
        "A": np.random.randn(50),
        "B": np.random.randn(50) * 10 + 5,
        "lat": 37.76 + np.random.randn(50) * 0.02,
        "lon": -122.4 + np.random.randn(50) * 0.02,
    })

    footnotes = []
    counter = 1

    # 텍스트 계층
    st.header("텍스트 요소들")
    st.title("페이지 타이틀 예시")
    st.markdown(f"<sup>[{counter}]</sup>", unsafe_allow_html=True)
    footnotes.append((counter, "`st.title()` — 큰 제목을 표시합니다."))
    counter += 1

    st.subheader("서브헤더 예시")
    st.markdown(f"<sup>[{counter}]</sup>", unsafe_allow_html=True)
    footnotes.append((counter, "`st.subheader()` — 소제목을 표시합니다."))
    counter += 1

    st.write("보통 텍스트 출력: `st.write()`를 사용합니다.")
    st.markdown(f"<sup>[{counter}]</sup>", unsafe_allow_html=True)
    footnotes.append((counter, "`st.write()` — 다양한 타입(텍스트, 수치, 데이터프레임 등)을 스마트하게 표시합니다."))
    counter += 1

    st.caption("작은 보조 텍스트(캡션)")
    st.markdown(f"<sup>[{counter}]</sup>", unsafe_allow_html=True)
    footnotes.append((counter, "`st.caption()` — 보조 설명이나 출처 등 작은 글씨를 보여줍니다."))
    counter += 1

    # 입력 위젯
    st.header("입력 위젯")
    col1, col2, col3 = st.columns(3)
    with col1:
        n = st.number_input("숫자 입력", min_value=0, max_value=100, value=10)
        st.markdown(f"<sup>[{counter}]</sup>", unsafe_allow_html=True)
        footnotes.append((counter, "`st.number_input()` — 실수/정수 입력 필드입니다."))
        counter += 1
    with col2:
        s = st.slider("슬라이더", 0, 100, 25)
        st.markdown(f"<sup>[{counter}]</sup>", unsafe_allow_html=True)
        footnotes.append((counter, "`st.slider()` — 범위 선택 슬라이더입니다."))
        counter += 1
    with col3:
        opt = st.selectbox("선택박스", ["옵션 A", "옵션 B", "옵션 C"]) 
        st.markdown(f"<sup>[{counter}]</sup>", unsafe_allow_html=True)
        footnotes.append((counter, "`st.selectbox()` — 단일 선택 목록입니다."))
        counter += 1

    st.multiselect("다중 선택", ["a", "b", "c"])
    st.markdown(f"<sup>[{counter}]</sup>", unsafe_allow_html=True)
    footnotes.append((counter, "`st.multiselect()` — 복수 항목 선택이 가능한 위젯입니다."))
    counter += 1

    st.checkbox("체크박스 예시")
    st.markdown(f"<sup>[{counter}]</sup>", unsafe_allow_html=True)
    footnotes.append((counter, "`st.checkbox()` — 토글/옵션 활성화에 사용합니다."))
    counter += 1

    st.radio("라디오 버튼", ["1번", "2번"]) 
    st.markdown(f"<sup>[{counter}]</sup>", unsafe_allow_html=True)
    footnotes.append((counter, "`st.radio()` — 단일 선택 라디오 버튼입니다."))
    counter += 1

    st.text_input("텍스트 입력", value="안녕하세요")
    st.markdown(f"<sup>[{counter}]</sup>", unsafe_allow_html=True)
    footnotes.append((counter, "`st.text_input()` — 한 줄 텍스트 입력입니다."))
    counter += 1

    st.text_area("여러 줄 텍스트")
    st.markdown(f"<sup>[{counter}]</sup>", unsafe_allow_html=True)
    footnotes.append((counter, "`st.text_area()` — 긴 텍스트 입력(여러 줄)입니다."))
    counter += 1

    # 파일 업로더 및 미디어
    st.header("미디어 & 파일")
    st.file_uploader("파일 업로드")
    st.markdown(f"<sup>[{counter}]</sup>", unsafe_allow_html=True)
    footnotes.append((counter, "`st.file_uploader()` — 사용자 파일을 업로드할 때 사용합니다."))
    counter += 1

    # 이미지 (샘플 생성)
    img = Image.new("RGB", (200, 80), color=(73, 109, 137))
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    st.image(buf, caption="샘플 이미지")
    st.markdown(f"<sup>[{counter}]</sup>", unsafe_allow_html=True)
    footnotes.append((counter, "`st.image()` — 이미지 파일을 표시합니다."))
    counter += 1

    # 데이터 표시
    st.header("데이터 & 차트")
    st.dataframe(df.head())
    st.markdown(f"<sup>[{counter}]</sup>", unsafe_allow_html=True)
    footnotes.append((counter, "`st.dataframe()` — 인터랙티브한 데이터프레임 뷰입니다."))
    counter += 1

    st.table(df.describe())
    st.markdown(f"<sup>[{counter}]</sup>", unsafe_allow_html=True)
    footnotes.append((counter, "`st.table()` — 정적 테이블을 보여줍니다."))
    counter += 1

    st.line_chart(df[["A", "B"]])
    st.markdown(f"<sup>[{counter}]</sup>", unsafe_allow_html=True)
    footnotes.append((counter, "`st.line_chart()` — 간단한 라인차트 (내장)입니다."))
    counter += 1

    # Altair 차트
    chart = alt.Chart(df).mark_circle(size=60).encode(x="A", y="B", tooltip=["A", "B"]) 
    st.altair_chart(chart, use_container_width=True)
    st.markdown(f"<sup>[{counter}]</sup>", unsafe_allow_html=True)
    footnotes.append((counter, "`st.altair_chart()` — Altair 차트를 임베드합니다."))
    counter += 1

    # 지도 표시 (pydeck)
    st.map(df[["lat", "lon"]])
    st.markdown(f"<sup>[{counter}]</sup>", unsafe_allow_html=True)
    footnotes.append((counter, "`st.map()` — 간단한 지도 시각화를 지원합니다."))
    counter += 1

    st.subheader("고급: PyDeck 예시")
    deck = pdk.Deck(
        initial_view_state=pdk.ViewState(latitude=37.76, longitude=-122.4, zoom=11, pitch=50),
        layers=[pdk.Layer("HexagonLayer", data=df, get_position=["lon", "lat"], radius=200)],
    )
    st.pydeck_chart(deck)
    st.markdown(f"<sup>[{counter}]</sup>", unsafe_allow_html=True)
    footnotes.append((counter, "`st.pydeck_chart()` — PyDeck(3D/지도) 시각화를 포함합니다."))
    counter += 1

    # 레이아웃: 컬럼, 익스팬더, 사이드바
    st.header("레이아웃 및 상호작용")
    left, right = st.columns([2, 1])
    with left:
        with st.expander("추가 옵션 (Expander)"):
            st.write("여기에 상세 옵션을 넣을 수 있습니다.")
    with right:
        st.sidebar.write("사이드바에 별도 컨트롤을 배치할 수 있습니다.")

    st.markdown(f"<sup>[{counter}]</sup>", unsafe_allow_html=True)
    footnotes.append((counter, "`st.columns()`, `st.expander()`, `st.sidebar` — 레이아웃을 구성합니다."))
    counter += 1

    # 상태 메시지 및 진행
    st.header("상태 메시지")
    if st.button("작업 실행 (버튼)"):
        with st.spinner("작업 수행 중..."):
            import time

            for i in range(10):
                time.sleep(0.05)
        st.success("작업 완료")

    st.markdown(f"<sup>[{counter}]</sup>", unsafe_allow_html=True)
    footnotes.append((counter, "`st.button()`, `st.spinner()`, `st.progress()` 등 — 사용자에게 상태/피드백을 제공합니다."))
    counter += 1

    # 폼 예시
    st.header("폼(Form) 예시")
    with st.form("my_form"):
        name = st.text_input("이름")
        age = st.number_input("나이", min_value=0, max_value=120)
        submitted = st.form_submit_button("제출")
        if submitted:
            st.write(f"안녕하세요, {name}님 (나이: {age})")

    st.markdown(f"<sup>[{counter}]</sup>", unsafe_allow_html=True)
    footnotes.append((counter, "`st.form()` — 입력을 그룹화하고 한 번에 제출하게 합니다."))
    counter += 1

    # 각주 리스트 출력
    st.markdown("---")
    st.subheader("각주")
    for num, text in footnotes:
        st.markdown(f"**[{num}]** {text}")


if __name__ == "__main__":
    main()
