import streamlit as st

def run_home():
    st.subheader('인천버스 정류장별 이용현황을 분석 및 예측합니다')
    st.markdown("데이터 출처 - [공공데이터포털:인천광역시_정류장별 이용승객 현황](https://www.data.go.kr/data/15048264/fileData.do)")

    st.image('./image/인천_시내버스_수소버스_전자신문.jpg', use_column_width=True)
    st.text('인천버스 정류장별 이용현황(카드 이용, 현금 이용)을 알 수 있는 앱이며,')
    st.text('머신러닝을 이용해 트래픽도 예측해볼 수 있습니다.')

if __name__ == "__main__":
    run_home()
