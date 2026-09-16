## Description:

Use this skill to read, create, update, and delete Formbricks data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Formbricks contacts and contact attribute keys through the oo CLI, including read, create, update, and delete actions with confirmation for state-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include an unverified remote installer for the oo CLI.

Mitigation: Review the installer path before use and prefer a signed, versioned, or package-manager installation when available.

Risk: The skill can create, update, and delete Formbricks data in a connected workspace.

Mitigation: Use only intended OOMOL and Formbricks workspaces, inspect the live action schema, and require explicit confirmation before create, update, or delete actions.

## Reference(s):

- [Formbricks homepage](https://formbricks.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Formbricks skill page](https://clawhub.ai/oomol/skills/oo-formbricks)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server evidence release version and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
