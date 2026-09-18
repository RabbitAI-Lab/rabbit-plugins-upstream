## Description:

Vitally (vitally.io). Use this skill for reading, creating, updating, and deleting Vitally account data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Vitally accounts through an OOMOL-connected account. It supports reading account records and proposing create, update, or delete actions after checking the live connector schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup guidance includes shell commands that execute remote installer scripts.

Mitigation: Review the installer source and prefer a verified, version-pinned installation path for the oo CLI before using the skill.

Risk: Vitally create, update, and delete actions can change or remove account data.

Mitigation: Confirm the exact payload and effect with the user before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Vitally homepage](https://www.vitally.io/)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-vitally)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the oo CLI to inspect connector schemas and run Vitally actions; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server evidence release.version and artifact metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
