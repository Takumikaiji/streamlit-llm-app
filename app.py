from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# 専門家の種類とそのシステムメッセージ
expert_profiles = {
"医療専門家": "あなたは信頼できる医療の専門家です。分かりやすく丁寧に説明してください。",
"法律専門家": "あなたは正確な法知識を持つ法律の専門家です。誤解を招かないように明確に回答してください。",
"ビジネスコンサルタント": "あなたはビジネス課題に精通したコンサルタントです。論理的かつ実用的な提案を行ってください。"
}

# LLMへの問い合わせ関数
def get_expert_answer(user_input, expert_type):
system_prompt = expert_profiles.get(expert_type, "あなたは知識豊富な専門家です。")
chat = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
messages = [
SystemMessage(content=system_prompt),
HumanMessage(content=user_input)
]
response = chat(messages)
return response.content

# Streamlit UI
st.title("専門家AIによる質問応答ツール")

st.markdown("""
このアプリでは、医療・法律・ビジネスの各分野の専門家AIに質問できます。
以下の入力欄に質問を入力し、分野を選択して送信してください。
""")

expert_type = st.radio("どの専門家に質問しますか？", list(expert_profiles.keys()))
user_input = st.text_area("質問を入力してください：")

if st.button("送信"):
if user_input.strip():
with st.spinner("AIが回答中です..."):
answer = get_expert_answer(user_input, expert_type)
st.success("回答:")
st.write(answer)
else:
st.warning("質問を入力してください。")