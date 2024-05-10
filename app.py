import streamlit as st
from home import run_home
from eda import run_eda

def main():
    st.title('인천버스 분석 및 예측 앱')

    menu = ['메인', '분석 및 통계']

    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0] :
        run_home() 
    elif choice == menu[1] :
        run_eda()

if __name__ == '__main__' :
    main()