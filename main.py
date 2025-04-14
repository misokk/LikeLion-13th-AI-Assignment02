import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
#파일의 내용을 읽어와서 환경 변수로 등록

API_KEY = os.environ["API_KEY"]
SYSTEM_MESSAGE = os.environ["SYSTEM_MESSAGE"]
#.env에 저장된 API_KEY와 SYSTEM_MESSAGE를 가져오기

BASE_URL = "https://api.together.xyz"
MODEL = "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
#together.ai에서 제공하는 LLaMA 3.1 모델을 사용

messages = [
    {"role": "system", "content": SYSTEM_MESSAGE}
]

print("챗봇을 시작합니다! (종료하려면 'exit' 또는 'quit' 입력)")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("챗봇을 종료합니다.")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.3 #온도, 응답의 창의성 
    )

    chatbot_reply = response.choices[0].message.content
    print("Chatbot:", chatbot_reply)
    #응답만 출력

    messages.append({"role": "assistant", "content": chatbot_reply})
    #대화 흐름 저장 기억하게하는 코드

# --- 아이디어 작성 ---
# 이 챗봇을 어디에 응용할 수 있을까요?
# 건강 관리 챗봇을 만들 때 응용해보고 싶습니다. 
# 심리적인 부분만이 아닌 육체적인 건강도 함께 챙길 수 있는 것을 만들고 싶습니다!