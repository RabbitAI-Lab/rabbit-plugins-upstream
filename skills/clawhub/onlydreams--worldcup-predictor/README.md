# World Cup Predictor Skill

Chinese version: [README_CN.md](README_CN.md)

An agent skill for structured World Cup and international football match analysis.

It guides an AI agent to combine market baseline, verified match data, team news, style matchup, match-state incentives, and post-match review instead of relying on a single signal such as odds, reputation, or recent scorelines.

## What It Does

- Builds match forecasts from layered evidence: market, data, news, context, and style matchup.
- Requires the agent to state which source layers were actually used.
- Routes full forecasts, quick first passes, live updates, post-match reviews, and rules/controversy analysis to the appropriate evidence workflow.
- Uses public odds and betting-market pages as baseline inputs, not final answers.
- Records an evidence cutoff and source state for time-sensitive odds, lineups, and live statistics.
- Checks player availability, role fitness, style matchup, group or knockout match-state incentives, and environmental factors.
- Supports knockout-specific reads, including 90-minute vs advancement forecasts, extra time, penalties, and bench depth.
- Supports card and discipline forecasts with referee profile, matchup fouls, game state, and reasonable card-count ranges.
- Produces compact predictions with score, backup score, separate result and exact-score confidence, failure mode, and missing-data notes.
- Supports context-bound post-match review and optional calibration records without inventing cross-session memory.

## Disclaimer

This skill is for informational football analysis only. Predictions are uncertain and can be wrong.

It does not provide betting advice, financial advice, guaranteed outcomes, or instructions to wager. Any odds, betting markets, or exchange prices discussed by the agent should be treated only as analytical inputs.

## Repository Structure

```text
worldcup-predictor/
├── SKILL.md
├── README.md
├── README_CN.md
├── LICENSE
├── agents/
│   └── openai.yaml
└── references/
    └── prediction-framework.md
```

## Installation

Copy or clone this repository into a skills directory supported by your agent runtime.

For Codex-style local skills, the directory is commonly:

```bash
~/.codex/skills/worldcup-predictor
```

The required entrypoint is:

```text
SKILL.md
```

## Usage

Invoke the skill when asking for World Cup or international football match analysis:

```text
Use $worldcup-predictor to analyze Spain vs Portugal using current team news, market baseline, recent match data, style matchup, and match-state incentives.
```

Useful request types include:

- Match forecast
- Exact-score prediction
- Betting-market comparison as an evidence layer
- Group qualification scenario
- Knockout advancement, extra-time, and penalty-shootout scenario
- Card and discipline forecast
- Player availability and lineup impact
- Style matchup analysis
- Post-match prediction review

## Source Discipline

The skill instructs the agent to clearly separate:

- confirmed facts
- reported information
- inferred judgments
- user-supplied data
- missing or unchecked data

The agent should not claim it used Sofascore, FotMob, FBref, Polymarket, Stake, official lineups, or any other source unless that source was directly read from a public page/API or supplied in the conversation.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
