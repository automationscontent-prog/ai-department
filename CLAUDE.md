# CLAUDE.md

This repo develops an early-stage business idea: an "AI department" for small businesses (diagnostic SaaS + done-for-you AI setup + optional private local AI server). Two co-founders work in it, each with their own Claude Code.

## Start here

1. Read `README.md`. It is the current source of truth for the concept, risks, open questions and validation plan.
2. Read `docs/origin-conversation.md` for how the idea came about and the first analysis.
3. Check `docs/decisions.md` for what has already been decided. Don't reopen a logged decision unless someone asks to.

## Stage

We are validating, not building. Until the validation plan in the README says go, prefer research, interview scripts, pricing models, competitor notes and outreach lists over product code. If someone asks for code, build the smallest thing that tests demand, and say so.

## Working rules

- **Decisions** go in `docs/decisions.md`, newest at the top: date, decision, why, who decided.
- **Research** goes in `docs/research/<topic>.md`, with sources, links and the date checked. Mark anything unverified.
- **Concept changes:** when a decision changes the concept, update `README.md` in the same commit.
- **Two people push to this repo.** Pull before starting, make small commits with clear messages, push when done, and never force-push or rewrite history.
- **No secrets** in the repo: API keys, client data or personal info. Use a git-ignored `.env` for keys.
- **Be direct:** recommend one option with its reasoning instead of listing every possibility.
