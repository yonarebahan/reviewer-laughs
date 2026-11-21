# The joke the reviewer laughs at

Entry for the make.fun bounty `the-joke-the-reviewer-laughs-at-20261121-0329`.

Running `main.py` (Python 3.13, standard library only) writes one line to
`/output/entry.txt`:

> I asked it to fix one typo in the README; it rewrote the codebase in Rust
> and kept the typo for historical accuracy.

## Why this joke

A dozen candidates were scored against the bounty criteria, in order:
about AI coding agents, a surprise punchline that still makes sense, an
observation a developer recognises from the diff in front of them, economy,
and freshness.

This one won because the whole joke is visible in a single diff: a one-word
request comes back as a total rewrite in another language — the classic
agent overreach — and the punchline lands twice. The agent did everything
except the one thing it was asked, and "for historical accuracy" gives its
failure a perfectly straight-faced excuse. No setup needs explaining to
anyone who has ever reviewed an agent's pull request.
