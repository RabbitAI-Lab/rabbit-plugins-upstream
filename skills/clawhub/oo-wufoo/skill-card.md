## Description:

Use Wufoo through OOMOL's oo CLI connector to read forms, fields, entries, and counts, and to submit new form entries with user-confirmed payloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Wufoo form workflows from an agent session, including listing forms and fields, reading or counting entries, filtering entry lists, and submitting new entries after payload confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read Wufoo form and entry data through the connected OOMOL account.

Mitigation: Use it only with an OOMOL/Wufoo connection the user trusts and with access appropriate for the task.

Risk: The skill can submit new Wufoo entries when a write action is requested.

Mitigation: Confirm the exact JSON payload and expected effect with the user before running any write action.

Risk: First-time setup may require installing the oo CLI.

Mitigation: Review the install command before execution and run setup only when an auth, connection, or missing-CLI error requires it.

## Reference(s):

- [Wufoo Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-wufoo)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Wufoo Homepage](https://www.wufoo.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an OOMOL account with Wufoo connected; write actions require confirmation of the exact payload.]

## Skill Version(s):

1.0.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
