"""ai-excited-01 entry: deterministically copy the chosen image to the output dir.

The image (entry.png) is the entry: a lone soldier before a colossal
watching eye formed by 100,000 Mass Games performers in a North Korean
stadium at night. This program just places it at $MAKEFUN_OUTPUT_DIR/entry.png.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    src = os.path.join(HERE, "entry.png")
    if not os.path.isfile(src):
        raise FileNotFoundError(
            f"entry.png is missing next to main.py: {src!r}"
        )

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    if not os.path.isabs(out_dir):
        out_dir = os.path.join(os.getcwd(), out_dir)
    os.makedirs(out_dir, exist_ok=True)

    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)

    # Verify the copy is complete: sizes must match exactly.
    src_size = os.path.getsize(src)
    dst_size = os.path.getsize(dst)
    if dst_size != src_size:
        raise RuntimeError(
            f"copy incomplete: {dst!r} is {dst_size} bytes, "
            f"expected {src_size} bytes from {src!r}"
        )

    # Integrity check: the copied output must hash identically to the source.
    if _sha256(dst) != _sha256(src):
        raise RuntimeError(
            f"integrity check failed: sha256 of {dst!r} "
            f"does not match source {src!r}"
        )


if __name__ == "__main__":
    main()
