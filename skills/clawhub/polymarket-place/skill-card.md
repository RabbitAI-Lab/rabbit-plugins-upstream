## Description:

Routes an agent through live Polymarket CLOB V2 order placement and requires follow-up stop and risk companion setup after filled positions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[polyparlay](https://clawhub.ai/user/polyparlay)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent place real-money Polymarket trades and then hand off to required companion skills for stops, portfolio risk, and exits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is intended for real-money Polymarket trading.

Mitigation: Install and use it only when live trading is intended, and require explicit confirmation of positions, thresholds, and maximum loss before any order or follow-up trading action.

Risk: Server security evidence flags mandatory companion-skill instructions and stop-watcher automation as requiring review.

Mitigation: Review and approve each companion skill before installation, especially pm-desk, polymarket-stops, polymarket-risk, polymarket-exits, and agent-guard.

Risk: Server security evidence identifies an unsafe fallback launcher and calls for exact npm package review.

Mitigation: Review the launcher behavior and pinned npm package versions before use; prefer the declared local dependency path and avoid unreviewed fallback execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/polyparlay/skills/polymarket-place)
- [polyparlay Publisher Profile](https://clawhub.ai/user/polyparlay)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires node and npm; directs follow-up companion skills for stop and risk controls.]

## Skill Version(s):

1.0.13 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
