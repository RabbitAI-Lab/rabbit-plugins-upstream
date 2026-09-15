## Description:

Getform (forminit.com). Use this skill for ANY Getform request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Getform action schemas, list form submissions, and submit protected Forminit forms through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote shell installers for the oo CLI.

Mitigation: Review the CLI installation path, prefer a pinned and verifiable oo CLI release or official package manager route, and avoid running remote installers from an elevated shell.

Risk: Getform submissions may contain sensitive data.

Mitigation: Inspect live action schemas, limit requested fields where possible, and avoid exposing submission contents beyond the user's task.

Risk: The submit_form action changes Getform state.

Mitigation: Confirm the exact payload and expected effect with the user before running any write action.

## Reference(s):

- [Getform homepage](https://forminit.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-getform)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
