import random
import streamlit as st

# 웹앱 제목 및 설명 설정
st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("버튼을 누르면 오늘 먹을 점심 메뉴를 랜덤으로 골라드립니다!")

# 추천할 점심 메뉴 리스트 (원하는 메뉴를 자유롭게 추가/수정하세요)
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈까스",
    "비빔밥",
    "짜장면",
    "짬뽕",
    "국밥",
    "햄버거",
    "초밥",
    "파스타",
    "쌀국수",
    "떡볶이",
    "부대찌개",
]

# 버튼 생성 및 클릭 이벤트 처리
if st.button("🎲 오늘의 점심 추천받기"):
    selected_menu = random.choice(lunch_menus)
    st.success(f"오늘의 추천 메뉴는 **{selected_menu}**입니다! 맛있게 드세요! 😋")
    st.balloons()
