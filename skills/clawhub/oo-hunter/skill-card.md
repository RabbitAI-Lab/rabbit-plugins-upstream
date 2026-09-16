## Description:

Hunter (hunter.io) lets an agent use OOMOL's Hunter connector for account, enrichment, search, verification, discovery, and lead-management workflows instead of calling the Hunter API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Hunter through the OOMOL-connected oo CLI for email discovery, enrichment, verification, and lead-list operations. It supports read workflows plus confirmed write and destructive lead-management actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer execution for the oo CLI.

Mitigation: Review the installer source and prefer a verified or package-manager installation path before using the skill.

Risk: Hunter write and destructive actions can create, update, or delete lead data.

Mitigation: Confirm the exact action, target, and payload with the user before running write or destructive actions.

Risk: Inline shell-quoted JSON payloads can mishandle user-supplied values.

Mitigation: Use @file JSON payloads for user-supplied data and validate them against the live connector schema before execution.

## Reference(s):

- [Hunter homepage](https://hunter.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-hunter)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect live connector schemas before building action payloads and to use JSON responses from the oo CLI.]

## Skill Version(s):

1.0.4 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
