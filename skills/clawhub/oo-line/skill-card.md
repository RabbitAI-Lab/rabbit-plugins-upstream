## Description:

LINE lets an agent operate a user's OOMOL-connected LINE account by inspecting connector schemas and running supported LINE actions through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to retrieve LINE bot or profile information and send text broadcasts, multicasts, or push messages through an OOMOL-connected LINE account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes pipe-to-shell installer commands from OOMOL-hosted URLs.

Mitigation: Use only when the publisher and installer source are trusted; prefer a verified installer or documented package source before local execution.

Risk: Broadcast, multicast, and push actions can send messages to LINE users or all friends of the Official Account.

Mitigation: Inspect the live action schema and confirm the exact payload, recipients, and effect with the user before running write actions.

## Reference(s):

- [ClawHub LINE skill page](https://clawhub.ai/oomol/skills/oo-line)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [LINE homepage](https://line.me)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions require explicit user confirmation; connector responses include data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
