## Description:

mymind (mymind.com) supports reading, creating, updating, organizing, and deleting mymind data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate mymind through an OOMOL-connected account, including reading, searching, creating, updating, organizing, and deleting mymind content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote shell and PowerShell installer pipelines without verification.

Mitigation: Install the oo CLI through a signed, versioned, or checksum-verified method before using the skill.

Risk: The skill can perform write and destructive mymind actions.

Mitigation: Approve write or destructive actions only after checking the exact target and payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mymind)
- [mymind homepage](https://mymind.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call oo connector actions that return JSON data and execution metadata.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
