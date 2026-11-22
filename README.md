# Gemini 3.1 Flash Lite 터미널 챗봇

Google GenAI Interactions API(`gemini-3.1-flash-lite`) 기반의 무상태(Stateless, 메모리 없음) 터미널 챗봇입니다.

## 빠른 시작

### 1. API 키 설정
`.env` 파일에 발급받은 Gemini API 키를 입력합니다.
```env
GEMINI_API_KEY="your_api_key_here"
```

### 2. 실행
```powershell
uv run python -m chatbot.cli
```
> 종료: `exit`, `quit` 또는 `q` 입력
