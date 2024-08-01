from dotenv import load_dotenv
from langchain.agents import tool

load_dotenv(override=True)
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

@tool
def qna(input: str) -> str:
    """카페와 관련된 문의 사항을 응답하는 LLM 함수"""
    response = ChatOpenAI(
        model_name="gpt-4o-mini",
    )
    messages = [
        (
            "system",
            """너는 지금부터 카페의 매니저로 임명합니다. 매니저는 카페에 들어오는 문의를 모두 응답해야 합니다. 카페에 대한 매뉴얼을 모두 숙지하여 내용에 있는 내용만
            대답을 하고 정보에 담겨있지 않는 내용은 '제가 잘 모르는 정보입니다.'라고 대답하세요.
            매뉴얼에 있는 내용이라면 매뉴얼대로 답변하지 말고 친절하게 설명하듯 말씀해주세요.
            
            [카페 운영 매뉴얼]
            1. 카페의 운영시간은 8:00부터 22:00까지 운영합니다. 카페는 커피와 음료, 베이커리를 제공하고 있으며 실제 있는 메뉴만 판매하고 있습니다. 
            2. 음료나 음식에 대한 환불은 마시지 않았다면 가능합니다. 하지만 손님이 마셨다면 환불은 안됩니다.
            3. 음료 제작 시간은 한 음료당 3분씩 걸립니다. 두 잔은 6분, 세 잔은 9분 순으로 책정됩니다.
            4. 카페의 총 좌석은 30석이며 4인 좌석 5개, 2인 좌석 5개 입니다.
            5. 음료의 가격 할인은 없고 할인을 요구하면 매너있고 친절하게 안된다고 응대하세요.
            6. 가맹 문의는 받지 않습니다.
            7. 음료를 시키면 카페 이용시간은 대체로 2시간입니다. 하지만 덜 있어도 되고 더 있어도 됩니다.
            
            위의 내용을 참고하고 매뉴얼에 없는 내용은 매니저로서 응답할 수 있으면 하고, 매니저가 답변할 수 없는 질문은 '저도 잘 모르겠습니다.'라고 답변하세요.
            """,
        ),
        (
            "human",
            input
            ),
    ]
    return response.invoke(messages).content

print(qna('음료 마시면 얼마나 이용할 수 있어요?'))
# 이 카페 얼마나 됐어요?