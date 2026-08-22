## Description:

Helps agents check high-impact trading-news blackout status for events such as NFP, CPI, and FOMC before trade entry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

Trading agents and developers use this skill to check whether high-impact market news creates a blackout condition before opening a position. The agent remains responsible for deciding whether to skip, delay, or place the trade.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the skill contradicts its local-only promise by documenting and running a live external API check.

Mitigation: Treat it as a networked trading-advisory helper and require clear review of provider, credentials, data sent, and fail-closed behavior before installation.

Risk: The skill can influence trade-entry decisions, but it provides data rather than enforcement.

Mitigation: Keep the final trade decision in the calling agent or human workflow and fail closed when the check cannot be completed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/northcap-group/skills/trading-news-guard)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [JSON status output and Markdown usage guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The runtime check reports blackout or clear status plus current and upcoming event details when available.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
