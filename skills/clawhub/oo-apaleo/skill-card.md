## Description:

apaleo enables agents to read, create, update, and delete apaleo data through an OOMOL-connected account using the `oo` CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate apaleo property and inventory workflows from an OOMOL-connected account, including reads plus confirmed write and destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run remote installer scripts directly in a shell.

Mitigation: Review the installer path before use and prefer a verified package or official guide with checksum or signature validation.

Risk: Write and destructive apaleo actions can change, delete, or overwrite account data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running any action marked write or destructive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-apaleo)
- [apaleo homepage](https://apaleo.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses `oo connector schema` before payload construction; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.5 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
