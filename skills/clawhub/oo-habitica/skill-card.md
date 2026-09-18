## Description:

Enables an agent to manage Habitica tasks, tags, scoring, and user profile data through an OOMOL-connected oo CLI Habitica connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to read and manage their Habitica tasks and tags through an OOMOL-connected account. It supports routine Habitica operations while requiring confirmation before actions that write, delete, or otherwise change account data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may direct users to execute remote installer scripts directly.

Mitigation: Review the oo CLI installation path before use and prefer an official, version-pinned installer or package manager flow with checksum or signature verification.

Risk: Write and destructive actions can change or delete Habitica account data.

Mitigation: Confirm the exact payload, effect, and target with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Habitica Skill](https://clawhub.ai/oomol/skills/oo-habitica)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Habitica homepage](https://habitica.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads/results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before requests; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
