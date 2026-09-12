## Description:

Miro lets an agent read, create, update, and delete Miro boards and board items through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill to operate Miro boards from an agent session, including board discovery, item inspection, content creation, updates, and deletion when explicitly confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands for the oo CLI.

Mitigation: Review the installer path before installing, prefer a pinned, signed, or package-manager-based installation, and avoid running remote scripts from an elevated shell.

Risk: Miro write and destructive actions can change or delete board content.

Mitigation: Confirm the board, item, action, and payload with the user before allowing write or destructive actions.

## Reference(s):

- [ClawHub Miro skill page](https://clawhub.ai/oomol/skills/oo-miro)
- [Miro homepage](https://miro.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions use oo CLI connector schemas and return JSON responses with data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
