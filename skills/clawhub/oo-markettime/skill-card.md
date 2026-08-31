## Description:

MarketTime lets an agent search and read MarketTime catalog items, manufacturers, and orders through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to inspect MarketTime account data for catalog, manufacturer, and order lookup tasks without handling raw credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read data from the user's connected MarketTime account.

Mitigation: Install and invoke it only for explicit catalog, manufacturer, or order lookup tasks.

Risk: Broad MarketTime routing language may cause the agent to select the skill for loosely related requests.

Mitigation: Apply the skill only when the user is asking for MarketTime data or related account lookups.

Risk: Future connector actions could modify or delete MarketTime data if write or destructive actions are exposed.

Mitigation: Require user confirmation of the exact payload and expected effect before any write action, and explicit approval before any destructive action.

## Reference(s):

- [ClawHub MarketTime skill](https://clawhub.ai/oomol/skills/oo-markettime)
- [MarketTime homepage](https://www.markettime.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.1 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
