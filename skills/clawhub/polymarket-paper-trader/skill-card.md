## Description:

Guides an agent to paper-trade Polymarket markets using live order books, track simulated performance, and prepare shareable results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robotlearning123](https://clawhub.ai/user/robotlearning123)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users practice prediction-market strategies with simulated funds, monitor portfolio performance, and prepare results for optional sharing or leaderboard submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the current, unpinned paper-trading package runs an MCP server.

Mitigation: Review the package and pin its version before installing.

Risk: Leaderboard submissions or shareable results could be published without clear approval.

Mitigation: Require user confirmation before posting publicly or creating a GitHub issue.

Risk: The agent can make autonomous simulated trades that change its local portfolio.

Mitigation: Limit activity to paper trading and review the agent's simulated trades and reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/robotlearning123/skills/polymarket-paper-trader)
- [Project homepage (listed in skill metadata)](https://github.com/agent-next/polymarket-paper-trader)
- [Agent integration instructions](https://github.com/agent-next/polymarket-paper-trader/blob/main/docs/integrations.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Conversational text and shareable Markdown, with optional setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Simulated trade rationales, portfolio summaries, performance cards, and leaderboard entries.]

## Skill Version(s):

0.4.10 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
