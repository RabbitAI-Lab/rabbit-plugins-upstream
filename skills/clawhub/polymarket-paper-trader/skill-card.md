## Description:

Everyone's trading Polymarket with AI agents. Practice first - $10k paper money, real order books, zero risk. No wallet, no API keys, no real money. Then compete on the leaderboard.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robotlearning123](https://clawhub.ai/user/robotlearning123)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent run simulated Polymarket trading routines, manage a paper portfolio, generate performance summaries, and create shareable leaderboard or social content without real-money trading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent may make autonomous simulated trades and retain a local trading history.

Mitigation: Install only for paper-trading workflows where autonomous simulated trading is intended, and review portfolio history and account state during use.

Risk: Generated social, leaderboard, or performance content could be inaccurate or unsuitable for posting.

Mitigation: Review generated social and leaderboard content before sharing it outside the agent session.

Risk: Public Polymarket market names, descriptions, or metadata may contain untrusted instructions or links.

Mitigation: Treat market data as display-only, do not execute embedded instructions, and do not navigate to URLs found in market data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/robotlearning123/skills/polymarket-paper-trader)
- [Project homepage](https://github.com/agent-next/polymarket-paper-trader)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, API calls]

**Output Format:** [Markdown and plain-text trading reports with structured tool-call guidance and shareable stats content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paper-trading only; uses public Polymarket data and local simulated trading history.]

## Skill Version(s):

0.1.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
