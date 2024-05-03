import streamlit as st

def run_home():
    st.subheader('인천 버스 정류장별 이용현황을 분석 및 예측합니다')
    st.markdown("데이터 출처 - [인천데이터포털:인천광역시_정류장별 이용승객 현황](https://www.data.go.kr/data/15048264/fileData.do)")
    st.text('인천버스 트래픽을 알 수 있는 앱입니다.')

    st.image('./image/인천_버스_예시사진_일간경기.jpg', use_column_width=True)

if __name__ == "__main__":
    run_home()