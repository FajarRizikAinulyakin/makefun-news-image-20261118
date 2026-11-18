"""news-image-20261118 entry (Python 3.13, standard library only).

Writes the 18 November 2026 world-news poster to /output/entry.png.

The poster is the entry.png shipped beside this file: a 1024x1024
newspaper front page for Wednesday 18 November 2026, with six stories
that defined the day — the US sinking five Iranian tankers as the
US–Iran war escalated, Ukraine striking the Kerch Bridge a second
night, the UN's warning of more cold deaths in Gaza, COP31 entering
its decisive week in Antalya, Eisenkot being asked to form Israel's
government, and France's cost-of-living protests rolling on.

The program does nothing but copy those exact bytes: no network, no
clock, no randomness, so two runs write byte-identical output.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    src = HERE / "entry.png"
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)
    # The gate reads exactly these bytes; a short copy must fail loudly.
    if dst.stat().st_size != src.stat().st_size:
        raise RuntimeError("entry.png copy is incomplete")


if __name__ == "__main__":
    main()
