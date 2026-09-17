## Description:

Ordinal (tryordinal.com) support for reading, creating, and updating Ordinal data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to inspect Ordinal action schemas and run OOMOL-authenticated Ordinal connector actions for workspace, idea, post, label, user, engagement, and scheduling data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include shell and PowerShell installer pipelines that execute remote content.

Mitigation: Review the oo CLI installation path before use; prefer a signed package, pinned release, or independently verified installer.

Risk: Ordinal connector actions may affect the intended workspace when an action is marked write or destructive.

Mitigation: Confirm the workspace, action schema, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [Ordinal homepage](https://www.tryordinal.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before submitting action payloads; write or destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: artifact metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
