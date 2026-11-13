# ai-joke-03 entry

One-line joke about AI coding agents, written by a Python 3.13 program with no
dependencies. The program writes the joke to `/output/entry.txt` (or to
`$MAKEFUN_OUTPUT_DIR` outside the grader's container).

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt

Deterministic: two runs write the same bytes. No network, no clock, no randomness.
