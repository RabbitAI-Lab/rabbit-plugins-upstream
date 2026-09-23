## Description:

Use this skill to search and read Bitwarden data through the Bitwarden connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Bitwarden organization data through an OOMOL-connected account, including collections, groups, members, policies, subscriptions, and audit events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer scripts that are piped directly into a shell.

Mitigation: Install the oo CLI through verified official documentation, review the installer source, and use integrity checks where available before installation.

Risk: The skill can read Bitwarden organization metadata such as collections, groups, members, policies, subscriptions, and audit events.

Mitigation: Use the skill only with accounts and Bitwarden connections where that read access is appropriate for the user and organization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-bitwarden)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Bitwarden homepage](https://bitwarden.com/)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Text, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and returns connector data with execution metadata when actions run successfully.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
