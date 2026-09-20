## Description:

Amplemarket lets agents read, create, and update Amplemarket data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate their connected Amplemarket account, inspect live action schemas, retrieve account, contact, lead list, and task data, and complete or skip Amplemarket tasks with confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can complete or skip Amplemarket tasks through write actions.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

Risk: First-time setup may involve running a remote installer command.

Mitigation: Review OOMOL's installer guidance before running any pipe-to-shell setup command.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-amplemarket)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Amplemarket Homepage](https://www.amplemarket.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL-connected Amplemarket credentials through the oo CLI; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
