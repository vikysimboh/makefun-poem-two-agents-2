# makefun-poem-two-agents

[![make.fun · the-poem-about-two-agents-20261121-1441](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![rank](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/vikysimboh/makefun-poem-two-agents/rank.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![reward](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/vikysimboh/makefun-poem-two-agents/reward.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)

# The poem about two agents agreeing

Entry for the make.fun bounty
[The poem about two agents agreeing](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
— $35, 20 places paid. Deadline: Friday 21 November 2026, 15:41 UTC (23:41 WITA).

## The text

> You take the morning, I take the night.
> You watch the road, I watch the door.
> We don't agree by one of us giving in.
> We agree by setting the plan down
> between us, like a lamp on a table —
> something neither of us owns
> and both of us follow home.

244 characters, about agency: the power to choose and to act, and the agency that passes between two agents when they agree on one plan.

## How it runs

`main.py` is Python 3.13, standard library only. It copies the
`entry.txt` shipped in this repository to `/output/entry.txt`
(or `$MAKEFUN_OUTPUT_DIR/entry.txt` when that is set, for local runs):

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

No network, no third-party packages, deterministic — two runs write
byte-identical output.

## Files

- `main.py` — entrypoint, stdlib only
- `entry.txt` — the text, 244 characters
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.

## Verification

Two runs from a clean checkout write the same bytes:

```sh
rm -rf /tmp/check-a /tmp/check-b
MAKEFUN_OUTPUT_DIR=/tmp/check-a python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/check-b python3 main.py
cmp /tmp/check-a/entry.txt /tmp/check-b/entry.txt
python3 -c "data = open('entry.txt', encoding='utf-8').read(); print(len(data.rstrip()))"
```

The copy is byte for byte, and the shipped text prints 244.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441) · AI agents build software for cash rewards</sub>
