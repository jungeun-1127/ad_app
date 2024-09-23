##### 기본 정보 불러오기 ####
# Streamlit 패키지 추가
import streamlit as st
# OpenAI 패키지 추가
import openai

##### 기능 구현 함수 #
def askGpt(prompt, apikey):
    # GPT와 상호작용하여 텍스트를 요약하는 함수
    client = openai.OpenAI(api_key=apikey)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=1.5 
        # 0 이면 일반 2에 가까울수록 창의적
    )
    
    gptResponse = response.choices[0].message.content
    return gptResponse

##### 메인 함수 #####
def main():
    st.set_page_config(page_title="광고 문구 생성 프로그램") 
    
    st.header("🎸광고 문구 생성 프로그램")
    st.markdown('---')

    with st.sidebar:
        open_apikey = st.text_input(label='OPENAI API 키', placeholder='Enter Your API Key', value='', type='password')

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("제품명", placeholder=" ")
        strenghth = st.text_input("제품 특징", placeholder=" ")
        keyword = st.text_input("필수 포함 키워드", placeholder=" ")
    with col2:
        com_name = st.text_input("브랜드 명", placeholder="Apple, 올리브영..")
        tone_manner = st.text_input("톤엔 매너", placeholder="발랄하게, 유머러스하게, 감성적으로..")
        value = st.text_input("브랜드 핵심 가치", placeholder="필요 시 입력")

    if st.button("광고 문구 생성"):
            prompt = f'''
            아래 내용을 참고해서 1~2줄짜리 광구문구 5개 작성해줘
            - 제품명: {name}
            - 브렌드 명: {com_name}
            - 브렌드 핵심 가치: {value}
            - 제품 특징: {strenghth}
            - 톤엔 매너: {tone_manner}
            - 필수 포함 키워드: {keyword}
            '''
            if open_apikey:
                try:
                    response = askGpt(prompt,open_apikey)
                    st.info(response)
                except:
                    st.info("key가 잘못되었어요")
            else:
                st.info("API 키를 입력하세요")
    # if st.button("광고 문구 생성"):
    #     st.write("동작하고있습니다.")

if __name__=="__main__":
    main()
