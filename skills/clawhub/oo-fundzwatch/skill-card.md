## Description:

FundzWatch lets an agent use an OOMOL-connected FundzWatch account to retrieve lead intelligence, market signals, account usage, and watchlist data, and to add company domains to a watchlist after confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent retrieve FundzWatch lead intelligence, funding and hiring signals, benefits and lender directories, market briefs, usage data, and watchlist activity through the oo CLI. It can also add domains to the connected FundzWatch watchlist after the user confirms the exact payload and effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Adding domains to a watchlist changes state in the connected FundzWatch account.

Mitigation: Confirm the exact domains, payload, and expected effect with the user before running the watchlist write action.

Risk: The skill operates through the user's OOMOL-connected FundzWatch account and may access account-scoped lead, watchlist, usage, and event data.

Mitigation: Install and use it only when the user intends the agent to access that connected account; do not request or expose raw FundzWatch credentials.

## Reference(s):

- [ClawHub FundzWatch Skill](https://clawhub.ai/oomol/skills/oo-fundzwatch)
- [FundzWatch Homepage](https://fundzwatch.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
