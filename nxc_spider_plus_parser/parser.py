#!/usr/bin/env python3
import csv
import json
import os
import sys
import shutil
import argparse
from typing import Any, Dict

HEADERS = ["file", "atime_epoch", "ctime_epoch", "mtime_epoch", "size"]

# Global toggle for ANSI color output (set from --no-color)
NO_COLOR = False

# ───────────────────────── ANSI helpers
class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"

    BLUE = "\033[34m"
    CYAN = "\033[36m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"

def color(text: str, *styles: str) -> str:
    """Return ANSI-colored text unless --no-color was set."""
    if NO_COLOR:
        return text
    return "".join(styles) + text + C.RESET

# ───────────────────────── Core helpers
def ensure_dict(v: Any, path: str) -> Dict[str, Any]:
    if not isinstance(v, dict):
        raise ValueError(f"Expected object at {path}, got {type(v).__name__}")
    return v

def write_csv(out_dir: str, share: str, entries: Dict[str, Any]) -> str:
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{share}.csv")

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HEADERS)
        w.writeheader()

        for file_name, meta in entries.items():
            meta = ensure_dict(meta, f"{share}.{file_name}")
            w.writerow({
                "file": file_name,
                "atime_epoch": meta.get("atime_epoch", ""),
                "ctime_epoch": meta.get("ctime_epoch", ""),
                "mtime_epoch": meta.get("mtime_epoch", ""),
                "size": meta.get("size", ""),
            })

    return out_path

def print_share_summary(share: str, entries: Dict[str, Any]) -> None:
    width = shutil.get_terminal_size(fallback=(100, 20)).columns
    sep = "─" * min(width, 80)

    print()
    print(color(share, C.BOLD, C.CYAN))
    print(color(sep, C.DIM))

    for file_name, meta in entries.items():
        size = meta.get("size", "") if isinstance(meta, dict) else ""
        print(f"  {color(file_name, C.BLUE)}")
        print(f"    {color('size:', C.DIM)} {color(size, C.GREEN)}")

# ───────────────────────── Main
def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert JSON share listings into per-share CSV files"
    )
    parser.add_argument("input", help="Input JSON file")
    parser.add_argument(
        "output_dir",
        nargs="?",
        default="csv_out",
        help="Output directory (default: csv_out)",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Suppress share/file stdout output (CSV written line still prints)",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable ANSI color output",
    )

    args = parser.parse_args()

    # Set global color behavior
    global NO_COLOR
    NO_COLOR = args.no_color

    try:
        with open(args.input, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print("ERROR: Invalid JSON", file=sys.stderr)
        print(e, file=sys.stderr)
        return 1
    except OSError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    try:
        data = ensure_dict(data, "root")
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    for share, entries in data.items():
        try:
            entries = ensure_dict(entries, f"root.{share}")
        except ValueError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            continue

        # Optional pretty stdout
        if not args.quiet:
            print_share_summary(share, entries)

        # Always write CSV
        out_path = write_csv(args.output_dir, share, entries)

        # Always print this line regardless of --quiet
        print(color(f"\n  → CSV written: {out_path}", C.DIM))

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
