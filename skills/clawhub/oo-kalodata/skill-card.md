## Description:

Kalodata helps agents search and read TikTok commerce analytics through OOMOL's Kalodata connector instead of calling the Kalodata API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve Kalodata analytics for TikTok categories, creators, livestreams, products, shops, and videos through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes Kalodata queries through OOMOL as an intermediary.

Mitigation: Review the OOMOL account, Kalodata connection, and any one-time CLI install or login step before installing or using the skill.

Risk: Authentication, missing scopes, expired credentials, app readiness, or billing issues can block connector calls.

Mitigation: Only start setup, reconnection, or billing troubleshooting after a command fails for that specific reason.

Risk: Connector action schemas may change over time.

Mitigation: Inspect the live `oo connector schema` for the selected Kalodata action before constructing each payload.

## Reference(s):

- [Kalodata on ClawHub](https://clawhub.ai/oomol/skills/oo-kalodata)
- [Kalodata homepage](https://www.kalodata.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before building action payloads.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
