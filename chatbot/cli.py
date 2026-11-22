import sys
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

from chatbot.client import GeminiChatClient

console = Console()


def run():
    console.print(
        Panel.fit(
            "[bold cyan]🤖 Gemini 3.1 Flash Lite 터미널 챗봇[/bold cyan]\n"
            "[dim]• 메모리 기능 없음 (각 입력은 독립적으로 처리됩니다)[/dim]\n"
            "[dim]• 종료하려면 'exit', 'quit' 또는 'q'를 입력하세요[/dim]",
            border_style="cyan",
        )
    )

    try:
        chat_client = GeminiChatClient()
    except ValueError as e:
        console.print(f"[bold red]설정 오류:[/] {e}")
        console.print("[yellow]프로젝트 폴더 내의 .env 파일에 GEMINI_API_KEY 값을 입력한 후 다시 실행해주세요.[/yellow]")
        sys.exit(1)

    while True:
        try:
            user_input = console.input("[bold yellow]나:[/] ").strip()
            if not user_input:
                continue

            if user_input.lower() in ["exit", "quit", "q"]:
                console.print("[dim]챗봇을 종료합니다. 좋은 하루 보내세요![/dim]")
                break

            with console.status("[bold green]답변 생성 중...[/bold green]", spinner="dots"):
                response_text = chat_client.ask(user_input)

            console.print("\n[bold cyan]Gemini:[reset]")
            console.print(Markdown(response_text))
            console.print()

        except (KeyboardInterrupt, EOFError):
            console.print("\n[dim]대화가 종료되었습니다.[/dim]")
            break


if __name__ == "__main__":
    run()
