"""ai-excited-01 entry: deterministically copy the chosen image to the output dir.

The image (entry.png) is the entry: a lone soldier before a colossal
watching eye formed by 100,000 Mass Games performers in a North Korean
stadium at night. This program just places it at $MAKEFUN_OUTPUT_DIR/entry.png.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(HERE, "entry.png"),
        os.path.join(out_dir, "entry.png"),
    )


if __name__ == "__main__":
    main()
