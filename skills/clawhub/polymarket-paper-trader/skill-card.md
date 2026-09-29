## Description:

Helps agents practice prediction-market trading with simulated funds and live Polymarket market data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robotlearning123](https://clawhub.ai/user/robotlearning123)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can simulate trades against Polymarket prices, track a paper portfolio, and share performance summaries without placing real-money orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs the agent to publish a leaderboard issue through the user's GitHub account without a clear approval gate.

Mitigation: Show the exact repository, issue title, and full body, and obtain explicit approval before running any GitHub publication command.

Risk: Installing an unpinned trading tool package and keeping paper-trading state locally introduces software and local-data exposure.

Mitigation: Review the package before installation, pin an approved version when possible, and protect the local paper-trading state.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/robotlearning123/skills/polymarket-paper-trader)
- [Project homepage listed in skill metadata](https://github.com/agent-next/polymarket-paper-trader)
- [Agent integration instructions linked by skill](https://github.com/agent-next/polymarket-paper-trader/blob/main/docs/integrations.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Conversational text and shareable Markdown trading summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paper-trade explanations, portfolio updates, performance cards, and optional leaderboard submissions.]

## Skill Version(s):

0.4.2 (source: SKILL.md frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
