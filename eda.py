import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def run_eda():
    # 한글 폰트 설정
    font_path = 'C:/Windows/Fonts/gulim.ttc'
    font_name = fm.FontProperties(fname=font_path).get_name()
    plt.rc('font', family=font_name)

    st.subheader('인천버스 정류장별 승객 이용현황')

    st.text('데이터 프레임 보기 / 통계치 보기를 할 수 있습니다.')
    st.markdown('<p style="font-weight: bold;">※ 해당 데이터 셋의 최종 수정일은 2024-04-18 입니다.</p>', unsafe_allow_html=True)

    df = pd.read_csv('./data/(가공한)인천광역시_정류장별 이용승객 현황_2024-04-18.csv', encoding='euc-kr')

    radio_menu = ['데이터 프레임', '통계치']

    choice_radio = st.radio('선택하세요', radio_menu)
    
    if choice_radio == radio_menu[0]:
        st.dataframe(df)
    elif choice_radio == radio_menu[1]:
        st.dataframe(df.describe())
        
    # 최대/최소값 및 비례 관계 분석으로 수정
    st.text('컬럼을 선택하면, 각 컬럼별 최대/최소 데이터를 각각 5개씩 보여드립니다.')
    column_list = ['총 승차', '총 하차', '카드 승차', '카드 하차', '현금 승차', ' 일평균 승하차', '총 승차 대비 총 하차', '총 하차 대비 총 승차', '카드 승차 대비 카드 하차', '카드 하차 대비 카드 승차', '현금 승차 대비 카드 승차', '카드 승차 대비 현금 승차']
    choice_column = st.selectbox('컬럼을 선택하세요.', column_list)
    
    st.info(f'선택하신 {choice_column}의 최대 정류장은 다음과 같습니다.')
    st.dataframe(df.nlargest(5, choice_column))
    
    st.info(f'선택하신 {choice_column}의 최소 정류장은 다음과 같습니다.')
    st.dataframe(df.nsmallest(5, choice_column))

    st.subheader('비례 관계 분석')
    st.text('컬럼들을 2개 이상 선택하면, 컬럼들의 비례 관계를 보여드립니다.')

    corr_column_list = ['총 승차', '총 하차', '카드 승차', '카드 하차', '현금 승차', '일평균 승하차', '총 승차 대비 총 하차', '총 하차 대비 총 승차', '카드 승차 대비 카드 하차', '카드 하차 대비 카드 승차', '현금 승차 대비 카드 승차', '카드 승차 대비 현금 승차']
    selected_columns = st.multiselect('컬럼을 선택하세요.', corr_column_list)

    # 2개 이상 선택했을때와 그렇지 않을때로 개발
    if len(selected_columns) >= 2 : 
        # 산점도 그래프에 회귀선 추가
        scatter_plot = sb.lmplot(data=df, x=selected_columns[0], y=selected_columns[1], line_kws={'color': 'red'}, scatter_kws={'alpha': 0.5})
        st.pyplot(scatter_plot)

        # 비례 관계 분석
        st.text('선택하신 컬럼들을 갖고 비례 관계를 분석 중입니다...')
        st.write('비례 관계는 각 컬럼의 상관계수가 1에 가까울수록 높은 경향을 보입니다.')
        correlation_matrix = df[selected_columns].corr()
        proportional_relationships = correlation_matrix.style.background_gradient(cmap='coolwarm', axis=None).format("{:.2f}")  # 수정된 부분
        st.dataframe(proportional_relationships)
    
    else : 
        st.text('컬럼은 2개 이상 선택해야 합니다.')
    

if __name__ == "__main__":
    run_eda()
