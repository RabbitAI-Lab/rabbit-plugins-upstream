## Description:

SupportBee (supportbee.com). Use this skill for ANY SupportBee request -- reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Support and operations teams use this skill to work with SupportBee tickets, replies, comments, labels, teams, users, and customer groups through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path may pipe a remote oo CLI installer directly into a shell.

Mitigation: Review the installer path and prefer an official package manager or verified installer before allowing installation commands to run.

Risk: Write or destructive SupportBee actions can create, update, or remove desk data.

Mitigation: Require confirmation of the exact target, payload, and expected effect before running write or destructive actions.

## Reference(s):

- [SupportBee homepage](https://supportbee.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [SupportBee ClawHub release](https://clawhub.ai/oomol/skills/oo-supportbee)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
