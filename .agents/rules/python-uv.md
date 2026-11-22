---
trigger: model_decision
description: "Apply these guidelines whenever creating virtual environments, installing packages, or running Python scripts."
globs: "*.py"
---

# Python 및 패키지 관리 규칙

Python 관련 모든 작업은 시스템 전역 Python이나 `pip` 대신 반드시 **`uv`**를 사용합니다.

- **가상환경 생성**: `uv venv` 사용 (`python -m venv` 사용 금지)
- **패키지 관리**: `uv pip install` 또는 `uv add` 사용 (`pip install` 사용 금지)
- **스크립트 및 도구 실행**: `uv run` 사용
- **기본 Python 버전**: 특별한 요구사항이 없으면 Python 3.12 기준 (`uv venv --python 3.12`)
