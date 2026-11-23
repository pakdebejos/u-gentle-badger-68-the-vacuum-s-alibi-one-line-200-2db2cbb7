"""The Crumb Surrendered: a robot vacuum's alibi, one line.

The program writes one funny line - a single line of at most 200
characters (124 characters) - to entry.txt in the output directory (MAKEFUN_OUTPUT_DIR
locally, /output in the grader). The text is a fixed constant with no
trailing newline, so both of the grader's runs write byte-identical output.
"""
import os

LINE = "Log 04:12: the crumb was holding a tiny white flag. I respect a surrender when I see one. Resuming route in 3... 2... never."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
