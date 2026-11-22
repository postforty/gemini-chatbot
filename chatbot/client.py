import os
from dotenv import load_dotenv
from google import genai
from google.genai import errors

# .env 파일 로드
load_dotenv()


class GeminiChatClient:
    """Gemini 3.1 Flash Lite 기반 무상태(Stateless) 챗봇 클라이언트."""

    def __init__(self, model_name: str = "gemini-3.1-flash-lite"):
        self.model_name = model_name
        self.api_key = os.getenv("GEMINI_API_KEY")

        if not self.api_key:
            raise ValueError(
                "GEMINI_API_KEY가 설정되지 않았습니다. .env 파일에 키를 입력해주세요."
            )

        # genai.Client는 GEMINI_API_KEY 환경변수를 기본으로 사용합니다.
        self.client = genai.Client(api_key=self.api_key)

    def ask(self, prompt: str) -> str:
        """단일 질문에 대해 답변을 생성합니다. (메모리/문맥 유지 없음)"""
        try:
            # Interactions API를 사용하여 독립된 단일 상호작용 생성
            interaction = self.client.interactions.create(
                model=self.model_name,
                input=prompt,
            )
            return interaction.output_text or "응답을 생성하지 못했습니다."
        except errors.APIError as e:
            return f"[API 오류] {e.message}"
        except Exception as e:
            return f"[오류 발생] {str(e)}"
