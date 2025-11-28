import streamlit as st

# 1. 페이지 설정
st.title("간단 Streamlit 채팅 앱")

# 2. 세션 상태(session_state) 초기화
# 채팅 기록을 저장할 리스트를 세션 상태에 초기화합니다.
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 3. 이전 채팅 기록 표시
# 저장된 메시지들을 순회하며 화면에 표시합니다.
for role, content in st.session_state["messages"]:
    with st.chat_message(role):
        st.markdown(content)

# 4. 사용자 입력 처리
# st.chat_input을 사용하여 사용자로부터 입력을 받습니다.
if prompt := st.chat_input("메시지를 입력하세요."):
    # 4-1. 사용자 메시지 화면에 표시 및 기록 저장
    # 사용자 메시지를 화면에 즉시 표시합니다.
    with st.chat_message("user"):
        st.markdown(prompt)
    # 세션 상태에 사용자 메시지 기록을 저장합니다.
    st.session_state["messages"].append(("user", prompt))

    # 4-2. 간단한 '봇' 응답 생성 및 표시
    # 여기서는 간단히 사용자 입력에 응답하는 예시를 만듭니다.
    response = f"당신이 입력한 내용: {prompt}"

    # 4-3. 봇 응답 화면에 표시 및 기록 저장
    # 봇의 응답을 화면에 표시합니다.
    with st.chat_message("assistant"):
        st.markdown(response)
    # 세션 상태에 봇 응답 기록을 저장합니다.
    st.session_state["messages"].append(("assistant", response))

# *참고: 실제 AI 챗봇 기능을 추가하려면 이 '봇' 응답 부분에 OpenAI나 다른 LLM API를 연동해야 합니다.
