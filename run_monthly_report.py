import subprocess
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
PYTHON = PROJECT_DIR / ".venv" / "Scripts" / "python.exe"

subprocess.run(
    [str(PYTHON), str(PROJECT_DIR / "report.py")],
    check=True
)