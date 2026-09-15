## Description:

Fellow lets agents read, create, and update Fellow meeting notes and action items through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Fellow workspace data from an agent workflow, including retrieving users, listing and reading meeting notes, and completing, reopening, or archiving action items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can execute remote oo CLI installer scripts directly in a shell.

Mitigation: Review the installer before installation and prefer verified, versioned, or checksum-validated oo CLI installation methods.

Risk: Connecting Fellow grants OOMOL-mediated access to a Fellow workspace.

Mitigation: Connect Fellow only after confirming the user is comfortable with that mediated access and the requested scopes.

Risk: Write actions can change Fellow action item state.

Mitigation: Confirm the exact target, payload, and expected effect with the user before completing, reopening, or archiving an action item.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fellow)
- [Fellow homepage](https://fellow.app)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; connector actions return JSON data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions require user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
