## Description:

Helps agents simulate prediction-market trades using live Polymarket prices, track a paper portfolio, and share performance summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robotlearning123](https://clawhub.ai/user/robotlearning123)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users practice prediction-market strategies with simulated funds, review positions and performance, and optionally prepare shareable results or leaderboard submissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may autonomously place paper trades and retain a local trading history.

Mitigation: Install only if comfortable with autonomous simulation and local history; review trade activity regularly.

Risk: Leaderboard or social-sharing steps may expose performance data or use the user's GitHub CLI to publish it.

Mitigation: Require user confirmation before any leaderboard submission or public post, including GitHub issue creation.

Risk: Installing an unpinned package can change the trading tools between sessions.

Mitigation: Consider pinning the package version before installation.

## Reference(s):

- [Project homepage (listed in skill metadata)](https://github.com/agent-next/polymarket-paper-trader)
- [Agent integration guide](https://github.com/agent-next/polymarket-paper-trader/blob/main/docs/integrations.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Trading summaries, portfolio reports, and shareable text or Markdown cards]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Simulated trades and performance metrics; optional leaderboard entries]

## Skill Version(s):

0.4.5 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
