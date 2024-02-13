import sys
from pathlib import Path

import streamlit.web.cli as stcli


def main() -> None:
    main_path = Path(__file__).parent / "main.py"
    sys.argv = ["streamlit", "run", str(main_path), "--global.developmentMode=false"]
    sys.exit(stcli.main())


if __name__ == "__main__":
    main()
